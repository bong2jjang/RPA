<!--
  @FE Project List View
  프로젝트 목록 페이지
-->

<template>
  <div class="projects">
    <div class="page-header">
      <h1>프로젝트 관리</h1>
      <button @click="showCreateModal = true" class="btn-primary">
        + 새 프로젝트
      </button>
    </div>

    <div class="projects-grid" v-if="projects.length > 0">
      <div
        v-for="project in projects"
        :key="project.id"
        class="project-card"
      >
        <h3>{{ project.name }}</h3>
        <p class="project-description">{{ project.description }}</p>
        <div class="project-meta">
          <span class="meta-item">🌍 {{ project.languages }} 언어</span>
          <span class="meta-item">📝 {{ project.keys }} 키</span>
        </div>
        <div class="project-actions">
          <button class="btn-small">편집</button>
          <button class="btn-small">번역</button>
        </div>
      </div>
    </div>

    <div v-else class="empty-state">
      <p>아직 프로젝트가 없습니다.</p>
      <p>새 프로젝트를 만들어 시작하세요.</p>
      <button @click="showCreateModal = true" class="btn-primary">
        + 첫 프로젝트 만들기
      </button>
    </div>

    <!-- Create Modal (Placeholder) -->
    <div v-if="showCreateModal" class="modal-overlay" @click="showCreateModal = false">
      <div class="modal-content" @click.stop>
        <h2>새 프로젝트 만들기</h2>
        <p>프로젝트 생성 폼은 추후 구현됩니다.</p>
        <button @click="showCreateModal = false">닫기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
/**
 * @FE Project List Component Script
 * 프로젝트 목록 관리
 */
import { ref, onMounted } from 'vue'
import { useProjectStore } from '@/store'

const projectStore = useProjectStore()
const projects = ref([])
const showCreateModal = ref(false)

onMounted(() => {
  // TODO: API에서 프로젝트 목록 로드
  projects.value = projectStore.projects
})
</script>

<style scoped>
.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

h1 {
  font-size: 32px;
  color: #2c3e50;
  margin: 0;
}

.btn-primary {
  background: #3498db;
  color: white;
  border: none;
  padding: 12px 24px;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
  transition: background 0.2s;
}

.btn-primary:hover {
  background: #2980b9;
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 24px;
}

.project-card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.project-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.project-card h3 {
  font-size: 20px;
  color: #2c3e50;
  margin-bottom: 12px;
}

.project-description {
  color: #7f8c8d;
  margin-bottom: 16px;
  min-height: 40px;
}

.project-meta {
  display: flex;
  gap: 16px;
  margin-bottom: 16px;
  font-size: 14px;
  color: #95a5a6;
}

.project-actions {
  display: flex;
  gap: 8px;
}

.btn-small {
  flex: 1;
  padding: 8px 16px;
  border: 1px solid #ddd;
  background: white;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-small:hover {
  background: #ecf0f1;
  border-color: #3498db;
  color: #3498db;
}

.empty-state {
  background: white;
  border-radius: 8px;
  padding: 60px 40px;
  text-align: center;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.empty-state p {
  color: #7f8c8d;
  font-size: 18px;
  margin-bottom: 16px;
}

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  border-radius: 8px;
  padding: 32px;
  max-width: 500px;
  width: 90%;
}

.modal-content h2 {
  margin-bottom: 16px;
  color: #2c3e50;
}
</style>
