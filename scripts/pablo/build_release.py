#!/usr/bin/env python3
"""Build versioned full source, hash-checked update bundle and Git patch from HEAD."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile


def git(*args): return subprocess.check_output(['git', *args])
def sha(data): return hashlib.sha256(data).hexdigest()
def tree(ref):
    return {x.split('\t')[1]:x.split()[0] for x in git('ls-tree','-rz',ref).decode().rstrip('\0').split('\0')}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base',required=True);p.add_argument('--also-base',action='append',default=[]);p.add_argument('--out',required=True,type=Path)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    version=git('show','HEAD:VERSION').decode().strip();head=git('rev-parse','HEAD').decode().strip()
    old=tree(a.base);new=tree('HEAD');extra=[(ref,tree(ref)) for ref in a.also_base];manifest={'schema':1,'project':'pablo-design','version':version,'commit':head,'base':a.base,'files':{}}
    bundle=a.out/f'pablo-design-{version}-update.zip'
    with zipfile.ZipFile(bundle,'w',zipfile.ZIP_DEFLATED) as z:
        for name in sorted(old.keys()|new.keys()):
            data=git('show','HEAD:'+name) if name in new else None
            before=git('show',a.base+':'+name) if name in old else None
            previous=[sha(before) if before is not None else None]
            for ref, inventory in extra:
                previous.append(sha(git('show',ref+':'+name)) if name in inventory else None)
            manifest['files'][name]={'sha256':sha(data) if data is not None else None,'previous':list(dict.fromkeys(previous)),'mode':int(new.get(name,'100644'),8)&0o777}
            if data is not None:z.writestr('payload/'+name,data)
        z.writestr('manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2))
    full=a.out/f'pablo-design-{version}.zip'
    subprocess.run(['git','archive','--format=zip','--prefix=pablo-design/','-o',str(full),'HEAD'],check=True)
    (a.out/f'pablo-design-{version}-from-298f248.patch').write_bytes(git('diff','--binary',a.base,'HEAD'))
    (a.out/'apply_update.py').write_bytes(git('show','HEAD:scripts/pablo/apply_update.py'))
    paths=[bundle,full,a.out/f'pablo-design-{version}-from-298f248.patch',a.out/'apply_update.py']
    (a.out/'SHA256SUMS').write_text(''.join(f'{sha(x.read_bytes())}  {x.name}\n' for x in paths))
    print(head,version, len(new),'files',str(a.out))


if __name__=='__main__':main()
