"""
@BE FastAPI Main Application
AI 기반 다국어 자동관리 웹시스템 - Backend Entry Point
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# FastAPI 인스턴스 생성
app = FastAPI(
    title="AI Multilingual Management System",
    description="AI 기반 다국어 자동관리 웹시스템 API",
    version="1.0.0"
)

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],  # Vue 개발 서버
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    @BE 루트 엔드포인트
    API 서버 기본 정보 제공
    """
    return {
        "message": "AI Multilingual Management System API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    """
    @BE 헬스 체크 엔드포인트
    시스템 상태 확인용
    """
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "ai-multilang-backend"
    }


@app.get("/api/v1/info")
async def api_info():
    """
    @BE API 정보 엔드포인트
    사용 가능한 API 정보 제공
    """
    return {
        "api_version": "v1",
        "endpoints": {
            "health": "/health",
            "projects": "/api/v1/projects",
            "translations": "/api/v1/translations",
            "settings": "/api/v1/settings"
        },
        "documentation": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
