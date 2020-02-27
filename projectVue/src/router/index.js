import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/Home'
import Contenedores from '../components/contenedores/Contenedores'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/contenedores',
      name: 'Contenedores',
      component: Contenedores
    }
  ],
  mode:"history"
})
