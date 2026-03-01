# Honux Profile Page

레트로 픽셀 테마의 개인 프로필 페이지입니다. Python + Jinja2 기반의 정적 사이트 생성기로 빌드됩니다.

🌐 **[honux77.github.io](https://honux77.github.io)**

## 기술 스택

- **빌드**: Python + Jinja2 템플릿 엔진
- **데이터**: YAML (`data/site.yaml`)
- **스타일**: 커스텀 CSS (레트로 8비트 테마)
- **호스팅**: GitHub Pages
- **OG 이미지**: Pillow (PIL)

## 프로젝트 구조

```
.
├── build.py           # 빌드 스크립트
├── generate_og.py     # OG 이미지 생성 스크립트
├── requirements.txt   # Python 의존성
├── data/
│   └── site.yaml      # 사이트 콘텐츠 데이터
├── templates/
│   └── index.html     # Jinja2 템플릿
├── css/
│   └── style.css      # 스타일시트
├── js/
│   └── script.js      # JavaScript
├── static/            # 정적 파일 (이미지 등)
└── _site/             # 빌드 결과물 (gitignore)
```

## 시작하기

### 의존성 설치

```bash
pip install -r requirements.txt
```

### 빌드

```bash
python build.py
```

빌드 결과물은 `_site/` 디렉터리에 생성됩니다.

### OG 이미지 생성

```bash
pip install Pillow
python generate_og.py
```

`static/img/og.png`에 저장됩니다.

## 콘텐츠 수정

`data/site.yaml` 파일을 수정하여 콘텐츠를 업데이트합니다.

```yaml
profile:
  class: "소프트웨어 개발자 / 부트캠프 운영"

projects:
  - title: "프로젝트명"
    url: "https://..."
    description: "설명"
```

## 배포

GitHub Pages를 통해 `master` 브랜치의 `_site/` 또는 루트에서 서비스됩니다.

```bash
python build.py
# _site/ 내용을 배포 브랜치에 푸시
```
