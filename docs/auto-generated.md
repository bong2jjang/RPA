# AI 기반 다국어 자동관리 웹시스템 - 자동 생성 문서

**생성 일시:** 2025-10-31 17:31:59

---

## 📘 Backend (FastAPI)


### be\app\main.py

**@BE:** FastAPI Main Application
AI 기반 다국어 자동관리 웹시스템 - Backend Entry Point

**@BE:** 루트 엔드포인트
    API 서버 기본 정보 제공

**@BE:** 헬스 체크 엔드포인트
    시스템 상태 확인용

**@BE:** API 정보 엔드포인트
    사용 가능한 API 정보 제공


### be\app\__init__.py

**@BE:** Backend Application Package
FastAPI 애플리케이션 패키지


### be\core\config.py

**@BE:** Configuration Module
환경 변수 기반 설정 관리

**@BE:** 애플리케이션 설정 클래스
    환경 변수를 통해 설정 값을 로드

**@BE:** 설정 객체 반환
    의존성 주입에 사용


### be\core\__init__.py

**@BE:** Core Module
Backend 핵심 설정 및 유틸리티 모듈

---

## 💻 Frontend (Vue3)


### fe\src\main.js

**@FE:** Vue3 Application Entry Point
 * AI 기반 다국어 자동관리 웹시스템 - Frontend Main


### fe\src\router\index.js

**@FE:** Vue Router Configuration
 * 애플리케이션 라우팅 설정


### fe\src\store\index.js

**@FE:** Pinia Store Configuration
 * 전역 상태 관리

**@FE:** 애플리케이션 메인 스토어
 * 전역 설정 및 상태 관리

**@FE:** 프로젝트 관리 스토어
 * 번역 프로젝트 상태 관리


### fe\src\App.vue

**@FE:** Main Application Layout
  Header, Sidebar, RouterView 구조

**@FE:** App Component Script
 * 애플리케이션 메인 레이아웃 로직


### fe\src\views\DashboardView.vue

**@FE:** Dashboard View
  대시보드 페이지 - 시스템 개요 및 통계

**@FE:** Dashboard Component Script
 * 대시보드 데이터 로드 및 표시


### fe\src\views\ProjectListView.vue

**@FE:** Project List View
  프로젝트 목록 페이지

**@FE:** Project List Component Script
 * 프로젝트 목록 관리


### fe\src\views\SettingsView.vue

**@FE:** Settings View
  시스템 설정 페이지

**@FE:** Settings Component Script
 * 시스템 설정 관리

---

## 📚 Documentation Scripts


### scripts\generate_docs.py

**@DOC:** Documentation Auto-Generation Script
FE/BE 코드의 주석을 파싱하여 자동으로 문서 생성

사용법:
    python scripts/generate_docs.py

출력:
    docs/auto-generated.md

**@DOC:** 문서 생성 클래스
    코드 파일에서 @FE, @BE, @DOC 주석을 추출하여 마크다운 문서 생성

**@DOC:** 파일 파싱 메서드
        Python, JavaScript, Vue 파일에서 주석 추출

**@DOC:** 디렉토리 스캔 메서드
        지정된 확장자 파일들을 재귀적으로 검색

**@DOC:** 마크다운 생성 메서드
        추출된 주석을 마크다운 형식으로 변환

**@DOC:** 문서 저장 메서드
        생성된 마크다운을 파일로 저장

**@DOC:** 메인 실행 함수
    스크립트 실행 시 호출

