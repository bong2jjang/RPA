/**
 * @FE Pinia Store Configuration
 * 전역 상태 관리
 */

import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import axios from 'axios'

/**
 * @FE 애플리케이션 메인 스토어
 * 전역 설정 및 상태 관리
 */
export const useAppStore = defineStore('app', () => {
  // State
  const isLoading = ref(false)
  const sidebarOpen = ref(true)
  const user = ref(null)
  const apiBaseUrl = ref('http://localhost:8000')

  // Getters
  const isAuthenticated = computed(() => user.value !== null)

  // Actions
  function toggleSidebar() {
    sidebarOpen.value = !sidebarOpen.value
  }

  function setLoading(status) {
    isLoading.value = status
  }

  async function checkHealth() {
    try {
      const response = await axios.get(`${apiBaseUrl.value}/health`)
      return response.data
    } catch (error) {
      console.error('Health check failed:', error)
      return null
    }
  }

  function setUser(userData) {
    user.value = userData
  }

  function logout() {
    user.value = null
  }

  return {
    // State
    isLoading,
    sidebarOpen,
    user,
    apiBaseUrl,
    // Getters
    isAuthenticated,
    // Actions
    toggleSidebar,
    setLoading,
    checkHealth,
    setUser,
    logout
  }
})

/**
 * @FE 프로젝트 관리 스토어
 * 번역 프로젝트 상태 관리
 */
export const useProjectStore = defineStore('project', () => {
  // State
  const projects = ref([])
  const currentProject = ref(null)

  // Actions
  function setProjects(projectList) {
    projects.value = projectList
  }

  function setCurrentProject(project) {
    currentProject.value = project
  }

  function addProject(project) {
    projects.value.push(project)
  }

  return {
    projects,
    currentProject,
    setProjects,
    setCurrentProject,
    addProject
  }
})
