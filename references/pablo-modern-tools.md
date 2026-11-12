# Pablo 3.3 제작 도구 연결

요청 해석·도움말·시안 수·선택·고도화·권한은 SKILL.md와 pablo-design-dialogue.md가 기준이다. 아래 모듈은 제작 기법과 검증에만 사용한다. 원본의 자동 설치·홍보·별도 승인 절차를 추가하지 않는다.

| 작업 | 기술 자료 |
|---|---|
| UI·웹 | modules/web.md |
| 발표자료 | modules/deck.md |
| 구조·정보 시각화 | modules/infographic.md |
| 영상·인터랙션 | modules/motion.md |
| 모바일 | app-prototype.md |

- `scripts/capabilities.py`: 필요한 도구의 존재 확인. 탐지 실패와 실제 사용 불가를 구분한다.
- `scripts/ref_board.py`: 제공되거나 승인된 참고 자료를 비교할 때 사용한다.
- `scripts/polish.py`와 `references/polish-loop.md`: 실제 화면 캡처 → 관찰 → 수정 → 재검증에 사용한다. 자동 점수를 시각 검증으로 대체하지 않는다.
- `scripts/design_lint.py`: 가독성·반복 패턴 점검 보조. 브랜드 예외와 실제 렌더를 함께 판단한다.
- `references/steady-track.md`: 환경 제약이 있을 때 참고한다. 미완성 시안을 완성된 세 안으로 보고하지 않는다.
- `scripts/learn.py`와 외관 기록은 선택 기능이다. 개인 기록은 `PABLO_DESIGN_HOME` 또는 `~/.pablo-design/`에 저장한다. 기록 전에 사용자에게 저장 내용을 알리고 허용된 범위만 저장한다. 다른 스킬의 기록은 자동으로 가져오지 않는다.

## 한국어 산출물

스킬 폴더에 폰트 파일이 있다는 사실만으로 출력 폰트가 설정된 것은 아니다. HTML은 `meta charset="utf-8"`와 한국어 글리프가 있는 폰트를 명시하고, 다운로드된 `NotoSansCJKkr-Regular.otf`를 사용할 때는 실제 파일의 절대 URL을 `@font-face`로 연결한다. 배포 HTML은 폰트를 산출물 폴더에 라이선스와 함께 복사하고 상대 URL로 연결한다. 사용자 컴퓨터의 절대 경로를 배포물에 남기지 않는다.

`document.fonts.ready`와 실제 한국어 렌더를 확인한다. PPTX는 한국어 글꼴을 명시하고, 좌표 기반 변환은 `--font-latin "Noto Sans CJK KR" --font-ea "Noto Sans CJK KR"`처럼 지정한다. 폰트 선택이 폰트 임베딩을 의미하지는 않는다. PDF와 PPTX 렌더를 각각 확인하며 다른 기기의 PowerPoint 표시까지 검증했다고 말하지 않는다.
