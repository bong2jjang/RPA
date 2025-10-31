<!--
  @FE Settings View
  시스템 설정 페이지
-->

<template>
  <div class="settings">
    <h1>설정</h1>

    <div class="settings-sections">
      <!-- API 설정 -->
      <section class="settings-section">
        <h2>🤖 AI API 설정</h2>
        <div class="form-group">
          <label>AI API 키</label>
          <input
            v-model="settings.aiApiKey"
            type="password"
            placeholder="API 키를 입력하세요"
            class="form-input"
          />
        </div>
        <div class="form-group">
          <label>AI 모델</label>
          <select v-model="settings.aiModel" class="form-select">
            <option value="gpt-4">GPT-4</option>
            <option value="gpt-3.5-turbo">GPT-3.5 Turbo</option>
            <option value="claude-3">Claude 3</option>
          </select>
        </div>
      </section>

      <!-- 번역 설정 -->
      <section class="settings-section">
        <h2>🌍 번역 설정</h2>
        <div class="form-group">
          <label>기본 소스 언어</label>
          <select v-model="settings.defaultSourceLang" class="form-select">
            <option value="ko">한국어</option>
            <option value="en">English</option>
            <option value="ja">日本語</option>
          </select>
        </div>
        <div class="form-group">
          <label class="checkbox-label">
            <input
              v-model="settings.autoTranslate"
              type="checkbox"
            />
            자동 번역 활성화
          </label>
        </div>
      </section>

      <!-- 시스템 설정 -->
      <section class="settings-section">
        <h2>⚙️ 시스템 설정</h2>
        <div class="form-group">
          <label>백엔드 URL</label>
          <input
            v-model="settings.backendUrl"
            type="text"
            placeholder="http://localhost:8000"
            class="form-input"
          />
        </div>
        <div class="form-group">
          <label class="checkbox-label">
            <input
              v-model="settings.debugMode"
              type="checkbox"
            />
            디버그 모드
          </label>
        </div>
      </section>

      <!-- 저장 버튼 -->
      <div class="settings-actions">
        <button @click="saveSettings" class="btn-primary">
          저장
        </button>
        <button @click="resetSettings" class="btn-secondary">
          초기화
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
/**
 * @FE Settings Component Script
 * 시스템 설정 관리
 */
import { ref, onMounted } from 'vue'
import { useAppStore } from '@/store'

const appStore = useAppStore()

const settings = ref({
  aiApiKey: '',
  aiModel: 'gpt-4',
  defaultSourceLang: 'ko',
  autoTranslate: false,
  backendUrl: 'http://localhost:8000',
  debugMode: false
})

onMounted(() => {
  // TODO: 로컬 스토리지 또는 API에서 설정 로드
  console.log('Settings loaded')
})

function saveSettings() {
  // TODO: 설정 저장 로직
  alert('설정이 저장되었습니다.')
}

function resetSettings() {
  if (confirm('설정을 초기화하시겠습니까?')) {
    settings.value = {
      aiApiKey: '',
      aiModel: 'gpt-4',
      defaultSourceLang: 'ko',
      autoTranslate: false,
      backendUrl: 'http://localhost:8000',
      debugMode: false
    }
  }
}
</script>

<style scoped>
h1 {
  font-size: 32px;
  margin-bottom: 30px;
  color: #2c3e50;
}

.settings-sections {
  max-width: 800px;
}

.settings-section {
  background: white;
  border-radius: 8px;
  padding: 24px;
  margin-bottom: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.settings-section h2 {
  font-size: 20px;
  margin-bottom: 20px;
  color: #2c3e50;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 500;
  color: #555;
}

.form-input,
.form-select {
  width: 100%;
  padding: 10px 12px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

.form-input:focus,
.form-select:focus {
  outline: none;
  border-color: #3498db;
}

.checkbox-label {
  display: flex !important;
  align-items: center;
  gap: 8px;
  cursor: pointer;
}

.checkbox-label input[type="checkbox"] {
  width: auto;
  cursor: pointer;
}

.settings-actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.btn-primary,
.btn-secondary {
  padding: 12px 32px;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-primary {
  background: #3498db;
  color: white;
}

.btn-primary:hover {
  background: #2980b9;
}

.btn-secondary {
  background: #ecf0f1;
  color: #555;
}

.btn-secondary:hover {
  background: #d5dbdb;
}
</style>
