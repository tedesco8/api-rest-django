import Vue from 'vue'
import Router from 'vue-router'
import store from './store'
import Home from './views/Home.vue'
import Contenedores from './components/Contenedores.vue'
import Login from './components/Login.vue'
import Usuario from './components/Usuario.vue'
import Articulo from './components/Articulo.vue'
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
        administrador: true,
        almacenero: true,
        vendedor: true
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
      path: '/usuario',
      name: 'usuario',
      component: Usuario,
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
