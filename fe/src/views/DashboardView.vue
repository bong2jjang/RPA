<!--
  @FE Dashboard View
  대시보드 페이지 - 시스템 개요 및 통계
-->

<template>
  <div class="dashboard">
    <h1>대시보드</h1>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-icon">📁</div>
        <div class="stat-info">
          <h3>전체 프로젝트</h3>
          <p class="stat-value">{{ projectCount }}</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🌍</div>
        <div class="stat-info">
          <h3>지원 언어</h3>
          <p class="stat-value">{{ languageCount }}</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">✅</div>
        <div class="stat-info">
          <h3>번역 완료</h3>
          <p class="stat-value">{{ translationCount }}</p>
        </div>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🤖</div>
        <div class="stat-info">
          <h3>AI 번역률</h3>
          <p class="stat-value">{{ aiPercentage }}%</p>
        </div>
      </div>
    </div>

    <div class="recent-activity">
      <h2>최근 활동</h2>
      <div class="activity-list">
        <p class="empty-state">아직 활동 내역이 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
/**
 * @FE Dashboard Component Script
 * 대시보드 데이터 로드 및 표시
 */
import { ref, onMounted } from 'vue'

const projectCount = ref(0)
const languageCount = ref(5)
const translationCount = ref(0)
const aiPercentage = ref(0)

onMounted(() => {
  // TODO: API에서 실제 데이터 로드
  console.log('Dashboard mounted')
})
</script>

<style scoped>
.dashboard {
  max-width: 1200px;
}

h1 {
  font-size: 32px;
  margin-bottom: 30px;
  color: #2c3e50;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.stat-card {
  background: white;
  border-radius: 8px;
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.stat-icon {
  font-size: 48px;
}

.stat-info h3 {
  font-size: 14px;
  color: #7f8c8d;
  margin-bottom: 8px;
  font-weight: 500;
}

.stat-value {
  font-size: 32px;
  font-weight: 700;
  color: #2c3e50;
  margin: 0;
}

.recent-activity {
  background: white;
  border-radius: 8px;
  padding: 24px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.recent-activity h2 {
  font-size: 20px;
  margin-bottom: 20px;
  color: #2c3e50;
}

.empty-state {
  text-align: center;
  color: #95a5a6;
  padding: 40px;
  font-size: 16px;
}
</style>
