"""Release updater invariants; never uses the real skill installation."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec=importlib.util.spec_from_file_location('pablo_update',Path(__file__).resolve().parents[1]/'pablo/apply_update.py')
u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)

class UpdateTest(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.base=Path(self.tmp.name);self.root=self.base/'skill';self.root.mkdir()
        home_patch=patch.object(u.Path, 'home', return_value=self.base/'home')
        home_patch.start();self.addCleanup(home_patch.stop)
        (self.root/'SKILL.md').write_bytes(b'old')
        (self.root/'.env').write_bytes(b'private')
        (self.root/'outputs').mkdir();(self.root/'outputs/user.txt').write_bytes(b'keep')
        self.archive=self.base/'update.zip'
    def bundle(self, name='SKILL.md', content=b'new', previous=b'old'):
        m={'schema':1,'project':'pablo-design','version':'3.3.0','files':{name:{'sha256':u.digest(content),'previous':[u.digest(previous)],'mode':420}}}
        with zipfile.ZipFile(self.archive,'w') as z:
            z.writestr('manifest.json',json.dumps(m));z.writestr('payload/'+name,content)
    def test_dry_run_preserves_files(self):
        self.bundle();u.update(self.archive,self.root);self.assertEqual((self.root/'SKILL.md').read_bytes(),b'old')
    def test_apply_preserves_private_files_and_is_idempotent(self):
        self.bundle();u.update(self.archive,self.root,True);u.update(self.archive,self.root,True)
        self.assertEqual((self.root/'SKILL.md').read_bytes(),b'new')
        self.assertEqual((self.root/'.env').read_bytes(),b'private')
        self.assertEqual((self.root/'outputs/user.txt').read_bytes(),b'keep')
        self.assertEqual(len(list((self.base/'home/.pablo-design/update-backups').glob('pablo-*'))),1)
    def test_local_edit_rejected(self):
        self.bundle();(self.root/'SKILL.md').write_bytes(b'edited')
        with self.assertRaises(ValueError):u.update(self.archive,self.root,True)
        self.assertEqual((self.root/'SKILL.md').read_bytes(),b'edited')
    def test_protected_path_rejected(self):
        self.bundle('.env',b'changed',b'private')
        with self.assertRaises(ValueError):u.update(self.archive,self.root,True)
    def test_traversal_rejected(self):
        self.bundle('../outside')
        with self.assertRaises(ValueError):u.update(self.archive,self.root,True)
    def test_nested_symlink_rejected(self):
        (self.root/'link').symlink_to(self.base,target_is_directory=True);self.bundle('link/file')
        with self.assertRaises(ValueError):u.update(self.archive,self.root,True)
    def test_root_symlink_supported(self):
        link=self.base/'alias';link.symlink_to(self.root,target_is_directory=True)
        self.bundle();u.update(self.archive,link,True);self.assertEqual((self.root/'SKILL.md').read_bytes(),b'new')
    def test_corrupt_payload_rejected(self):
        self.bundle()
        with zipfile.ZipFile(self.archive) as z:m=json.loads(z.read('manifest.json'))
        with zipfile.ZipFile(self.archive,'w') as z:
            z.writestr('manifest.json',json.dumps(m));z.writestr('payload/SKILL.md',b'bad')
        with self.assertRaises(ValueError):u.update(self.archive,self.root,True)
    def test_error_rolls_back(self):
        self.bundle()
        original=Path.write_text
        def fail_record(p,*args,**kwargs):
            if p.name=='update-record.json':raise OSError('simulated write failure')
            return original(p,*args,**kwargs)
        with patch.object(Path,'write_text',fail_record):
            with self.assertRaises(OSError):u.update(self.archive,self.root,True)
        self.assertEqual((self.root/'SKILL.md').read_bytes(),b'old')

if __name__=='__main__':unittest.main()
