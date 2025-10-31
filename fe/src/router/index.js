/**
 * @FE Vue Router Configuration
 * 애플리케이션 라우팅 설정
 */

import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '@/views/DashboardView.vue'
import ProjectListView from '@/views/ProjectListView.vue'
import SettingsView from '@/views/SettingsView.vue'

const routes = [
  {
    path: '/',
    name: 'dashboard',
    component: DashboardView,
    meta: { title: '대시보드' }
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectListView,
    meta: { title: '프로젝트 목록' }
  },
  {
    path: '/settings',
    name: 'settings',
    component: SettingsView,
    meta: { title: '설정' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 페이지 타이틀 자동 설정
router.beforeEach((to, from, next) => {
  document.title = to.meta.title
    ? `${to.meta.title} - AI 다국어 관리`
    : 'AI 다국어 관리'
  next()
})

export default router
