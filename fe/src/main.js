/**
 * @FE Vue3 Application Entry Point
 * AI 기반 다국어 자동관리 웹시스템 - Frontend Main
 */

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import router from './router'
import App from './App.vue'
import './assets/style.css'

// Vue 앱 인스턴스 생성
const app = createApp(App)

// Pinia 스토어 플러그인 등록
const pinia = createPinia()
app.use(pinia)

// Vue Router 플러그인 등록
app.use(router)

// 앱 마운트
app.mount('#app')
