"""Download the SIL OFL Korean font to the private project runtime, verifying bytes."""
import hashlib
from pathlib import Path
import requests

ROOT = Path(__file__).resolve().parents[2]
FILES = {
    'NotoSansCJKkr-Regular.otf': (
        'https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/OTF/Korean/NotoSansCJKkr-Regular.otf',
        '6bcb2a0703aa137e874fc2dffa85f6c21ba9a67fa329e81b8c801663af7e992a'),
    'LICENSE': (
        'https://raw.githubusercontent.com/notofonts/noto-cjk/main/Sans/LICENSE',
        '6a73f9541c2de74158c0e7cf6b0a58ef774f5a780bf191f2d7ec9cc53efe2bf2'),
}


def main():
    folder = ROOT / '.pablo/fonts'
    folder.mkdir(parents=True, exist_ok=True)
    for name, (url, expected) in FILES.items():
        target = folder / name
        if target.exists() and hashlib.sha256(target.read_bytes()).hexdigest() == expected:
            continue
        response = requests.get(url, timeout=90)
        response.raise_for_status()
        if hashlib.sha256(response.content).hexdigest() != expected:
            raise RuntimeError(f'Font source changed: {name}. Review before updating the recorded digest.')
        temporary = target.with_suffix('.download')
        temporary.write_bytes(response.content)
        temporary.replace(target)
    print('OK Korean font and SIL OFL license')


if __name__ == '__main__':
    main()
