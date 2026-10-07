<p align="right"><strong>한국어</strong> · <a href="README.en.md">English</a></p>

![Pablo — From context to design](assets/banner.svg)

# Pablo

**맥락을 이해하고, 디자인을 완성합니다.**

자료를 건네고 한 문장으로 요청하세요. Pablo가 목적과 독자를 파악하고, 디자인 방향을 결정한 뒤 제작·검증·납품까지 진행합니다. IR Deck, UI 목업, 시스템 아키텍처, PPT 개선, 브랜드 적용을 하나의 자연어 흐름으로 처리하는 에이전트 스킬입니다.

```text
Pablo로 이 내용 10장짜리 IR Deck 만들어줘
Pablo로 이 화면 UI 목업 만들어줘
Pablo로 이 시스템 아키텍처 시각화해줘
Pablo가 이 PPT 디자인 리뷰하고 수정해줘
Pablo로 이 디자인을 회사 브랜드에 맞춰 다시 만들어줘
```

[인터랙티브 데모](demos/pablo-demo.html) · [로컬 설치](#로컬-설치) · [작업 지침](SKILL.md)

![Pablo 인터랙티브 데모](assets/pablo-demo.png)

데모는 다섯 요청 유형과 결과의 **설명용 예시**입니다. AI 서버에 연결하거나 실제 파일을 생성하지 않습니다. 다운로드한 `demos/pablo-demo.html`을 브라우저에서 열면 작동하며, 외부 라이브러리나 계정이 필요하지 않습니다.

## 무엇을 만들 수 있나요?

| 요청 | 기본 결과 |
|---|---|
| IR Deck | 지정 장수의 편집 가능한 PPTX + PDF 미리보기 |
| UI 목업 | HTML/CSS 또는 React 소스 + 미리보기 |
| 아키텍처 시각화 | Mermaid 또는 SVG 소스 + 렌더링 결과 |
| PPT 리뷰·수정 | 슬라이드별 리뷰 + 수정 PPTX + 미리보기 |
| 브랜드 적용 | 원본 형식의 수정본 + 브랜드 적용 요약 |

“파블로”로 요청해도 됩니다. “회사 브랜드로 10장짜리 IR Deck”처럼 조건을 결합하거나, “3번째 슬라이드만 수정해줘”로 이어갈 수 있습니다. 지정한 형식·템플릿·장수와 기존 사실관계를 유지합니다.

## 어떻게 진행하나요?

1. **맥락 파악** — 첨부, 지정 파일, 앞선 대화에서 대상·목적·독자를 확인합니다.
2. **구조와 디자인 결정** — 메시지와 정보량에 맞는 방향을 선택합니다. 시안 비교를 요청했을 때만 선택을 기다립니다.
3. **제작과 수정** — 원본을 보존하면서 작업합니다. “리뷰하고 수정”은 수정본 제작까지 포함합니다.
4. **검증과 납품** — 최종 파일의 장수·내용·렌더링을 확인하고 결과와 제한을 전달합니다.

이미 확인할 수 있는 정보는 다시 묻지 않습니다. 대상 자료가 없거나 중요한 내용이 모호할 때만 필요한 질문을 합니다. 근거 없는 사업 수치나 시스템 구성을 만들어 넣지 않습니다.

## 로컬 설치

Node.js와 Python 3가 있는 환경에서 저장소를 내려받습니다.

```bash
git clone https://github.com/grooshbene/pablo-design.git
cd pablo-design
./pablo setup
./pablo doctor
```

설치는 프로젝트 내부에 Node 의존성, Python 가상환경, Chromium, 한글 폰트를 준비합니다. 패키지 서버와 공식 폰트 저장소에 접속하며 사용자 문서는 전송하지 않습니다. 다운로드한 폰트는 체크섬을 검증합니다.

| 기능 | 추가 조건 |
|---|---|
| macOS의 기존 HTML→PPTX 변환 | Google Chrome |
| PPTX→PDF·이미지 렌더링 | LibreOffice의 `soffice` |
| 영상 처리 | FFmpeg / FFprobe |
| 선택적 클라우드 TTS·영상 리뷰 | 해당 서비스의 API 키와 전송 동의 |

LibreOffice가 자동 검색되지 않으면 실행 파일을 지정하세요.

```bash
export PABLO_SOFFICE="/Applications/LibreOffice.app/Contents/MacOS/soffice"
```

에이전트에서 이 저장소를 열고 자료와 함께 “Pablo로 …”라고 요청하면 됩니다. `AGENTS.md`가 작업 지침으로 연결합니다. 터미널의 `./pablo`는 설치·변환·검증 도구이며 자연어를 처리하는 별도 AI 서비스가 아닙니다.

### 스킬로 설치

스킬을 지원하는 에이전트에서는 다음 설치 경로도 사용할 수 있습니다.

```bash
npx skills add grooshbene/pablo-design
```

스킬 이름은 `pablo`입니다. 설치 위치에 `SKILL.md`와 함께 `references/`, `assets/`, `scripts/`, `pablo`, 의존성 파일이 포함됐는지 확인하고, 그 폴더에서 `./pablo setup`을 실행하세요. 스킬 설치와 로컬 제작 환경 설치는 별개입니다.

## 실행 확인

```bash
./pablo smoke
```

환경 검증용 한글 2장 덱을 생성하고 PPTX·PDF 출력, PPTX 렌더링, 텍스트를 보존한 서식 수정, 일부 슬라이드 변환 실패 차단을 검사합니다. 결과는 `outputs/pablo-smoke-*/`에 저장됩니다. 실제 디자인 품질은 최종 이미지를 보고 확인해야 합니다.

직접 만든 HTML 덱은 다음과 같이 변환합니다.

```bash
./pablo export-deck --slides ./my-slides --out ./outputs/my-deck --expected-slides 10
./pablo inspect-pptx ./outputs/my-deck/deck.pptx
./pablo render-pptx ./outputs/my-deck/deck.pptx --out ./outputs/my-deck-rendered
```

슬라이드 폴더에는 `01.html`처럼 정렬 가능한 이름의 슬라이드만 넣습니다. 기존 HTML→PPTX 변환 제약을 따라야 하며, 오류·장수 불일치·텍스트 불일치가 있으면 납품 출력을 중단합니다. 기존 출력 폴더는 덮어쓰지 않습니다.

## 결과물과 범위

- 기본 저장 위치는 `outputs/<작업명>/`이며 지정한 위치가 있으면 그곳을 사용합니다.
- 고객·회사 납품물에는 **Pablo 또는 원본 도구의 홍보 워터마크를 기본으로 넣지 않습니다.** 제작자 표시를 요청하면 `Made with Pablo`를 사용합니다.
- 기존 PPTX의 복잡한 차트·애니메이션·마스터는 도구에 따라 보존이 제한될 수 있습니다. 원본을 남기고 실제 보존 여부를 확인합니다.
- LibreOffice와 PowerPoint/Keynote의 렌더링은 다를 수 있습니다. HTML에서 만든 PDF는 최종 PPTX의 시각 검증을 대신하지 않습니다.
- `.venv/`, `.pablo/`, `node_modules/`, `outputs/`는 Git에서 제외됩니다.
- 전체 워크플로는 에이전트가 수행합니다. 이 저장소는 독립적인 채팅 웹 서비스나 운영용 백엔드를 제공하지 않습니다.

## 출처와 라이선스

Pablo는 Huashu Design의 디자인 자료와 제작 도구를 활용합니다. 원저작자 고지와 MIT 라이선스는 보존하며, 브랜드 표시는 이를 대체하지 않습니다. [출처 안내](ATTRIBUTION.md) · [LICENSE](LICENSE) · [데이터 전송 안내](SECURITY.md)
