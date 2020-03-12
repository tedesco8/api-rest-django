import Vue from 'vue'
import Router from 'vue-router'
import store from './store'
import Home from './views/Home.vue'

import Login from './components/Login.vue'

import Contenedores from './components/Contenedores.vue'
import Articulo from './components/Articulo.vue'

import Administradores from './components/Administradores.vue'
import Colaboradores from './components/Colaboradores.vue'
import Usuarios from './components/Usuarios.vue'

import ReporteVentas from './components/ReporteVentas.vue'
import ReporteIngresos from './components/ReporteIngresos.vue'

Vue.use(Router)

var router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        libre: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        libre: true
      }
    },
    {
      path: '/contenedores',
      name: 'contenedores',
      component: Contenedores,
      meta: {
        libre: true
      }
    },
    {
      path: '/articulo',
      name: 'articulo',
      component: Articulo,
      meta: {
        libre: true
      }
    },
    {
      path: '/administradores',
      name: 'administradores',
      component: Administradores,
      meta: {
        libre: true
      }
    },
    {
      path: '/colaboradores',
      name: 'colaboradores',
      component: Colaboradores,
      meta: {
        libre: true
      }
    },
    {
      path: '/usuarios',
      name: 'usuarios',
      component: Usuarios,
      meta: {
        libre: true
      }
    },
    {
      path: '/reporteVentas',
      name: 'reporteVentas',
      component: ReporteVentas,
      meta: {
        libre: true
      }
    },
    {
      path: '/reporteIngresos',
      name: 'reporteIngresos',
      component: ReporteIngresos,
      meta: {
        libre: true
      }
    }
  ]
})
router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.libre)){
      next();
  } else {
    next({name: 'login'});
  }
})
export default router
