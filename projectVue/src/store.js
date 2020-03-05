import Vue from 'vue'
import Vuex from 'vuex'
import decode from 'jwt-decode'
import router from './router'

Vue.use(Vuex)

const getTokenVar = (accessToken,varname)=>{
  const tokenBody = accessToken.split('.')[1];
  debugger;
  const tokenObject = JSON.parse(atob(tokenBody));
  return tokenObject[varname];
}

export default new Vuex.Store({
  state: {
    tokens: null,
    usuario: null
  },
  mutations: {
    setTokens(state,tokens){
      state.tokens=tokens;
    },
    setUsuario(state,usuario){
      state.usuario=usuario;
    }
  },
  actions: {
    guardarToken({commit}, tokens){
      commit("setTokens", tokens);
      const user = getTokenVar(tokens.access,'user_id');
      commit("setUsuario",{id:user});
      localStorage.setItem("access_token", tokens.access)
      localStorage.setItem("refresh_token", tokens.refresh)
    },
    autoLogin({commit}){
      let token = localStorage.getItem("token");
      if(token) {
        commit("setTokens", token);
        const user = getTokenVar(tokens.accessToken,'user_id');
        commit("setUsuario",{id:user});        
      }
      router.push({name: 'home'});
    },
    salir({commit}){
      commit("setTokens", null);
      commit("setUsuario", null);
      localStorage.removeItem("access_tokens");
      localStorage.removeItem("refresh_tokens");
      router.push({name: 'login'});
    }
  }
})
