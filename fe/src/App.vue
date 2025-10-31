<!--
  @FE Main Application Layout
  Header, Sidebar, RouterView 구조
-->

<template>
  <div id="app" :class="{ 'sidebar-closed': !appStore.sidebarOpen }">
    <!-- Header -->
    <header class="app-header">
      <button @click="appStore.toggleSidebar" class="menu-toggle">
        ☰
      </button>
      <h1 class="app-title">AI 다국어 자동관리 시스템</h1>
      <div class="header-actions">
        <span class="status-indicator" :class="healthStatus">
          {{ healthStatus === 'healthy' ? '✓' : '○' }}
        </span>
      </div>
    </header>

    <div class="app-container">
      <!-- Sidebar -->
      <aside class="app-sidebar" v-show="appStore.sidebarOpen">
        <nav class="sidebar-nav">
          <router-link to="/" class="nav-item">
            <span class="nav-icon">📊</span>
            <span class="nav-label">대시보드</span>
          </router-link>
          <router-link to="/projects" class="nav-item">
            <span class="nav-icon">📁</span>
            <span class="nav-label">프로젝트</span>
          </router-link>
          <router-link to="/settings" class="nav-item">
            <span class="nav-icon">⚙️</span>
            <span class="nav-label">설정</span>
          </router-link>
        </nav>
      </aside>

      <!-- Main Content -->
      <main class="app-main">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup>
/**
 * @FE App Component Script
 * 애플리케이션 메인 레이아웃 로직
 */
import { ref, onMounted } from 'vue'
import { useAppStore } from '@/store'

const appStore = useAppStore()
const healthStatus = ref('unknown')

// 헬스 체크
onMounted(async () => {
  const health = await appStore.checkHealth()
  healthStatus.value = health?.status || 'unhealthy'
})
</script>

<style scoped>
.app-header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: #2c3e50;
  color: white;
  display: flex;
  align-items: center;
  padding: 0 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 100;
}

.menu-toggle {
  background: transparent;
  color: white;
  border: none;
  font-size: 24px;
  margin-right: 20px;
  padding: 5px 10px;
}

.app-title {
  flex: 1;
  font-size: 20px;
  font-weight: 600;
  margin: 0;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 15px;
}

.status-indicator {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: bold;
}

.status-indicator.healthy {
  background: #27ae60;
  color: white;
}

.status-indicator.unhealthy {
  background: #e74c3c;
  color: white;
}

.status-indicator.unknown {
  background: #95a5a6;
  color: white;
}

.app-container {
  display: flex;
  margin-top: 60px;
  min-height: calc(100vh - 60px);
}

.app-sidebar {
  width: 250px;
  background: #34495e;
  color: white;
  padding: 20px 0;
  transition: all 0.3s ease;
}

#app.sidebar-closed .app-sidebar {
  margin-left: -250px;
}

.sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px;
  color: white;
  text-decoration: none;
  transition: background 0.2s;
}

.nav-item:hover {
  background: rgba(255, 255, 255, 0.1);
}

.nav-item.router-link-active {
  background: rgba(255, 255, 255, 0.2);
  border-left: 4px solid #3498db;
}

.nav-icon {
  font-size: 20px;
}

.nav-label {
  font-size: 16px;
}

.app-main {
  flex: 1;
  padding: 30px;
  background: #ecf0f1;
  overflow-y: auto;
}
</style>
