# AI 기반 다국어 자동관리 웹시스템

AI를 활용한 다국어 번역 관리 웹 애플리케이션입니다.

## 🚀 주요 기능

- 다국어 번역 프로젝트 관리
- AI 기반 자동 번역
- 실시간 협업 및 버전 관리
- 자동화된 문서 생성

## 🛠 기술 스택

### Backend
- **FastAPI** - 고성능 Python 웹 프레임워크
- **SQLAlchemy** - ORM
- **Pydantic** - 데이터 검증
- **Redis** - 캐싱

### Frontend
- **Vue 3** - 프로그레시브 JavaScript 프레임워크
- **Vite** - 빠른 빌드 도구
- **Pinia** - 상태 관리
- **Vue Router** - 라우팅

## 📦 설치 및 실행

### Backend

```bash
cd be
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

백엔드 서버: http://localhost:8000

### Frontend

```bash
cd fe
npm install
npm run dev
```

프론트엔드 서버: http://localhost:5173

## 📚 API 문서

FastAPI 자동 생성 문서:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🔧 환경 변수 설정

`be/.env.example`을 복사하여 `be/.env` 파일을 생성하고 필요한 값을 설정하세요:

```env
DB_URL=sqlite:///./ai_multilang.db
REDIS_URL=redis://localhost:6379/0
AI_API_KEY=your-api-key-here
SECRET_KEY=your-secret-key-here
```

## 📖 문서 자동 생성

코드 주석을 기반으로 자동 문서를 생성합니다:

```bash
python scripts/generate_docs.py
```

생성된 문서: `docs/auto-generated.md`

## 📁 프로젝트 구조

```
ai-multilang/
├── be/                     # Backend (FastAPI)
│   ├── app/               # 애플리케이션 코드
│   ├── core/              # 핵심 설정
│   └── requirements.txt   # Python 의존성
├── fe/                     # Frontend (Vue3)
│   ├── src/               # 소스 코드
│   │   ├── views/        # 페이지 컴포넌트
│   │   ├── router/       # 라우팅
│   │   └── store/        # 상태 관리
│   └── package.json       # Node 의존성
├── docs/                   # 문서
└── scripts/                # 자동화 스크립트
```

## 🎯 개발 현황

- ✅ Step 1: 프로젝트 초기 구조 및 기본 기능 구현
- ⏳ Step 2: 핵심 기능 개발 (CRUD, 번역, 인증)
- ⏳ Step 3: 통합, 테스트, QA

## 📝 라이센스

MIT License

## 👥 기여

프로젝트에 기여하고 싶으시다면 Pull Request를 보내주세요!
