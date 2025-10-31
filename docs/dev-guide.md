# AI 기반 다국어 자동관리 웹시스템 - 개발 가이드

## 📋 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [시스템 요구사항](#시스템-요구사항)
3. [프로젝트 구조](#프로젝트-구조)
4. [Backend 설정 (FastAPI)](#backend-설정-fastapi)
5. [Frontend 설정 (Vue3)](#frontend-설정-vue3)
6. [문서 자동화](#문서-자동화)
7. [개발 워크플로우](#개발-워크플로우)
8. [트러블슈팅](#트러블슈팅)

---

## 프로젝트 개요

AI 기반 다국어 자동관리 웹시스템은 FastAPI 백엔드와 Vue3 프론트엔드로 구성된 풀스택 웹 애플리케이션입니다.

**주요 기능:**
- 다국어 번역 프로젝트 관리
- AI 기반 자동 번역
- 실시간 협업 및 버전 관리
- 자동화된 문서 생성

---

## 시스템 요구사항

### Backend
- Python 3.9 이상
- pip (Python 패키지 관리자)

### Frontend
- Node.js 18.0 이상
- npm 9.0 이상

### 선택사항
- Redis (캐싱용)
- PostgreSQL (프로덕션 DB)

---

## 프로젝트 구조

```
ai-multilang/
├── be/                     # Backend (FastAPI)
│   ├── app/
│   │   └── main.py        # FastAPI 애플리케이션 엔트리 포인트
│   ├── core/
│   │   └── config.py      # 환경 변수 설정
│   └── requirements.txt    # Python 의존성
│
├── fe/                     # Frontend (Vue3)
│   ├── src/
│   │   ├── assets/        # CSS, 이미지 등
│   │   ├── router/        # Vue Router 설정
│   │   ├── store/         # Pinia 상태 관리
│   │   ├── views/         # 페이지 컴포넌트
│   │   ├── App.vue        # 루트 컴포넌트
│   │   └── main.js        # 애플리케이션 엔트리 포인트
│   ├── package.json       # Node 의존성
│   └── vite.config.js     # Vite 빌드 설정
│
├── docs/                   # 문서
│   ├── dev-guide.md       # 이 파일
│   └── auto-generated.md  # 자동 생성 API 문서
│
└── scripts/                # 자동화 스크립트
    └── generate_docs.py   # 문서 자동 생성
```

---

## Backend 설정 (FastAPI)

### 1. 가상환경 생성 및 활성화

**Windows:**
```bash
cd be
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
cd be
python3 -m venv venv
source venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정

`.env.example`을 복사하여 `.env` 파일 생성:

```bash
cp .env.example .env
```

`.env` 파일 수정:
```env
DB_URL=sqlite:///./ai_multilang.db
REDIS_URL=redis://localhost:6379/0
AI_API_KEY=your-api-key-here
SECRET_KEY=your-secret-key-here
```

### 4. 서버 실행

```bash
uvicorn app.main:app --reload
```

서버가 실행되면 다음 주소에서 확인 가능:
- API: http://localhost:8000
- 대화형 문서: http://localhost:8000/docs
- 헬스 체크: http://localhost:8000/health

### 5. 주요 엔드포인트

| 엔드포인트 | 메서드 | 설명 |
|----------|-------|------|
| `/` | GET | API 정보 |
| `/health` | GET | 헬스 체크 |
| `/api/v1/info` | GET | API 버전 정보 |
| `/docs` | GET | Swagger UI |

---

## Frontend 설정 (Vue3)

### 1. 의존성 설치

```bash
cd fe
npm install
```

### 2. 개발 서버 실행

```bash
npm run dev
```

개발 서버가 실행되면: http://localhost:5173

### 3. 빌드

프로덕션 빌드:
```bash
npm run build
```

빌드 미리보기:
```bash
npm run preview
```

### 4. 주요 페이지

| 경로 | 컴포넌트 | 설명 |
|-----|---------|------|
| `/` | DashboardView | 대시보드 (통계 및 개요) |
| `/projects` | ProjectListView | 프로젝트 목록 |
| `/settings` | SettingsView | 시스템 설정 |

### 5. 상태 관리

Pinia 스토어 사용:

```javascript
import { useAppStore } from '@/store'

const appStore = useAppStore()
appStore.checkHealth() // 헬스 체크
```

---

## 문서 자동화

### 자동 문서 생성

코드의 `@FE`, `@BE`, `@DOC` 주석을 파싱하여 문서 자동 생성:

```bash
python scripts/generate_docs.py
```

출력 파일: `docs/auto-generated.md`

### 주석 작성 규칙

**Python (Backend):**
```python
"""
@BE 함수 설명
기능 상세 내용
"""
def my_function():
    pass
```

**JavaScript/Vue (Frontend):**
```javascript
/**
 * @FE 컴포넌트 설명
 * 컴포넌트 역할 설명
 */
```

---

## 개발 워크플로우

### 1. 개발 환경 시작

**터미널 1 - Backend:**
```bash
cd be
venv\Scripts\activate  # Windows
uvicorn app.main:app --reload
```

**터미널 2 - Frontend:**
```bash
cd fe
npm run dev
```

### 2. 코드 작성

- Backend: `be/app/` 디렉토리에서 작업
- Frontend: `fe/src/` 디렉토리에서 작업
- 주석에 `@FE`, `@BE` 태그 추가

### 3. 문서 생성

```bash
python scripts/generate_docs.py
```

### 4. 테스트

Backend:
```bash
# API 테스트
curl http://localhost:8000/health
```

Frontend:
```bash
# 브라우저에서 확인
# http://localhost:5173
```

---

## 트러블슈팅

### Backend 이슈

**문제: 포트가 이미 사용 중**
```bash
# 다른 포트로 실행
uvicorn app.main:app --reload --port 8001
```

**문제: 모듈을 찾을 수 없음**
```bash
# 가상환경이 활성화되었는지 확인
pip list
pip install -r requirements.txt
```

### Frontend 이슈

**문제: npm 의존성 오류**
```bash
# node_modules 삭제 후 재설치
rm -rf node_modules
npm install
```

**문제: CORS 에러**
- `be/app/main.py`에서 CORS 설정 확인
- 프론트엔드 주소가 `allow_origins`에 포함되어 있는지 확인

### 일반적인 이슈

**문제: 경로 오류**
- Windows에서 경로 구분자는 `\` 사용
- 스크립트에서는 `Path` 객체 사용 권장

---

## 추가 리소스

- [FastAPI 공식 문서](https://fastapi.tiangolo.com/)
- [Vue 3 공식 문서](https://vuejs.org/)
- [Pinia 공식 문서](https://pinia.vuejs.org/)
- [Vite 공식 문서](https://vitejs.dev/)

---

**작성일:** 2025-10-31
**버전:** 1.0.0
