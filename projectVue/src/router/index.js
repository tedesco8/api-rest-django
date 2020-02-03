import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import ArticulosList from '@/components/articulos/articulosList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/articulos',
      name: 'ArticulosList',
      component: ArticulosList
    }
  ],
  mode:"history"
})
