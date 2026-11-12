# Pablo 3.3.1 업데이트

현재 배포 기준 `298f248`에서 3.3.1으로 업데이트한다. 새 버전의 제작 도구와 자료를 반영하며 Pablo의 도움말, 조건부 3안 탐색, 선택 후 피드백 흐름을 유지한다. 전체 원본 스킬을 덮어쓰는 업데이트가 아니다.

## Git 설치

로컬 변경을 먼저 커밋하거나 별도로 보관한 뒤 릴리즈 태그를 받는다.

```bash
git fetch origin --tags
git checkout v3.3.1
./pablo doctor
```

동일 기준에서 변경 패치만 적용하려면 릴리즈의 `pablo-design-3.3.1-from-298f248.patch`를 내려받아 저장소 루트에서 실행한다. 이미 태그로 업데이트했다면 패치를 다시 적용하지 않는다.

```bash
git apply --check /absolute/path/pablo-design-3.3.1-from-298f248.patch
git apply /absolute/path/pablo-design-3.3.1-from-298f248.patch
```

## 전역 스킬·복사 설치

릴리즈에서 `apply_update.py`, `pablo-design-3.3.1-update.zip`, `SHA256SUMS`를 내려받는다. 같은 다운로드 폴더에서 체크섬을 확인한다. SHA256SUMS에는 전체 소스 ZIP과 Git 패치도 포함되므로 전체 자산을 받거나 받은 파일의 항목만 검사한다.

```bash
shasum -a 256 -c SHA256SUMS
python3 apply_update.py pablo-design-3.3.1-update.zip --target "$HOME/.agents/skills/pablo"
python3 apply_update.py pablo-design-3.3.1-update.zip --target "$HOME/.agents/skills/pablo" --apply
"$HOME/.agents/skills/pablo/pablo" doctor
```

`--apply`가 없으면 검사만 한다. 실제 설치 위치가 다르면 `--target`을 바꾼다. Claude의 스킬 폴더가 위 경로의 심볼릭 링크라면 한 번만 업데이트한다. 독립 복사본이면 각 경로에 따로 적용한다. 루트 심볼릭 링크는 실제 폴더로 해석하며 내부 심볼릭 링크는 거부한다.

업데이터는 기준 버전과 현재 릴리즈의 파일 해시만 허용한다. 로컬 수정이나 미지원 구버전은 덮어쓰지 않고 중단한다. `.env`, `.venv`, `.pablo`, `node_modules`, `outputs`, Git 메타데이터는 관리 대상에서 제외한다. 적용 전 `~/.pablo-design/update-backups/`에 백업을 만든다. 실패하면 변경 파일을 복구하며, 프로세스 강제 종료 시에는 표시된 백업을 이용해 복구한다. 새로 생긴 빈 폴더는 남을 수 있다.

의존성이 없으면 실제 설치 폴더의 `pablo setup`을 실행한다. 호스트가 이전 메타데이터를 표시하면 다시 시작한다. 새 설치는 기존 `npx skills add grooshbene/pablo-design` 경로도 유지한다. 이 릴리즈는 npm 레지스트리에 별도 게시하지 않는다.

## 검증 범위

한글 폰트를 명시한 로컬 HTML/PPTX/PDF 검사와 변환기 회귀 테스트를 사용한다. 폰트 임베딩이나 모든 기기에서의 PowerPoint 표시까지 보장하지 않는다. 최신 원본의 별도 라이선스 샘플은 해당 폴더의 고지를 따른다.

---

# Updating to Pablo 3.3.1

The release supports the previous `298f248` distribution. Git users can fetch and check out `v3.3.1`, or apply the binary patch after `git apply --check`. Do not use both methods.

For copied/global skill folders, download the release assets, verify `SHA256SUMS`, then run the updater commands above with the actual installation root. Without `--apply`, it is a dry run. The updater validates all managed files, rejects local edits and unsupported versions, preserves runtime/configuration/output directories, and creates a backup outside skill discovery under `~/.pablo-design/update-backups/`. Root symlinks are resolved; update a shared Codex/Claude target only once. Separate copies require separate updates.

Run the installed `pablo doctor` afterwards; use `pablo setup` only if dependencies are missing. Restart the host if it still shows old metadata. The existing skills installer route remains available for fresh installs. No npm registry publication is included.

Pablo keeps its help, conditional concept exploration, refinement and branding rules. This is an adapted upstream tool/reference update, not a replacement with the upstream workflow. Font embedding and rendering in every external viewer are not guaranteed. Third-party samples retain their own license notices.
