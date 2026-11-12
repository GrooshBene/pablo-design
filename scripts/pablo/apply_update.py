#!/usr/bin/env python3
"""Apply a trusted Pablo release bundle after checking every managed file.

Runtime folders, outputs, credentials and Git metadata are never included.
Run without --apply for a dry run. Root symlinks are resolved; nested symlinks
are rejected. Local edits cause an abort before any managed file is changed.
"""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import tempfile
import zipfile


def digest(data):
    return hashlib.sha256(data).hexdigest()


def update(archive, target, apply=False):
    root = Path(target).expanduser().resolve(strict=True)
    if not root.is_dir() or not (root / 'SKILL.md').is_file():
        raise ValueError('Target must be an existing Pablo skill root')
    protected = {'.git', '.venv', '.pablo', '.env', '.env.local', 'node_modules', 'outputs', '.agents', '.codex'}
    with zipfile.ZipFile(archive) as z:
        manifest = json.loads(z.read('manifest.json'))
        if manifest.get('project') != 'pablo-design' or manifest.get('schema') != 1:
            raise ValueError('Unsupported release manifest')
        entries = manifest['files']
        pending = []
        for name, item in entries.items():
            rel = PurePosixPath(name)
            if rel.is_absolute() or '..' in rel.parts or not rel.parts or rel.parts[0] in protected or '\\' in name:
                raise ValueError('Unsafe managed path: ' + name)
            dest = root.joinpath(*rel.parts)
            for parent in [dest, *dest.parents]:
                if parent == root: break
                if parent.is_symlink(): raise ValueError('Nested symlink: ' + name)
            if dest.exists() and not dest.is_file(): raise ValueError('Not a regular file: ' + name)
            current = digest(dest.read_bytes()) if dest.exists() else None
            wanted = item['sha256']
            data = z.read('payload/' + name) if wanted else None
            if data is not None and digest(data) != wanted: raise ValueError('Corrupt payload: ' + name)
            if current == wanted: continue
            if current not in item['previous']: raise ValueError('Local edit or unsupported version: ' + name)
            pending.append((name, data, item.get('mode', 420)))
        print(f'Validated {len(entries)} managed paths; {len(pending)} changes for {manifest["version"]}')
        if not apply or not pending: return
        backup_home = Path.home() / '.pablo-design' / 'update-backups'
        backup_home.mkdir(parents=True, exist_ok=True)
        backup = Path(tempfile.mkdtemp(prefix='pablo-', dir=backup_home))
        changed = []
        try:
            for name, data, mode in pending:
                dest = root / name
                old = backup / name
                existed = dest.exists()
                if existed:
                    old.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(dest, old)
                changed.append((dest, old, existed))
                if data is None:
                    dest.unlink()
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    with tempfile.NamedTemporaryFile(dir=dest.parent, delete=False) as f:
                        f.write(data); staging = Path(f.name)
                    try:
                        staging.chmod(mode & 0o777); staging.replace(dest)
                    finally:
                        staging.unlink(missing_ok=True)
            (backup / 'update-record.json').write_text(json.dumps({'version':manifest['version'],'target':str(root),'changed':[x[0] for x in pending]}, indent=2))
        except Exception:
            for dest, old, existed in reversed(changed):
                if existed: shutil.copy2(old, dest)
                else: dest.unlink(missing_ok=True)
            raise
        print('Applied. Backup: ' + str(backup))
        print('Run the updated skill setup/doctor if dependencies are missing. Restart the host if metadata is stale.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('archive', type=Path)
    p.add_argument('--target', required=True)
    p.add_argument('--apply', action='store_true')
    a = p.parse_args()
    try: update(a.archive, a.target, a.apply)
    except (ValueError, OSError, KeyError, zipfile.BadZipFile) as e: p.exit(1, str(e) + '\n')


if __name__ == '__main__': main()
