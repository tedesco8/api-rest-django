<template>
  <card class="card" title="Acceso al Sistema">
    <div>
      <form @submit.prevent>
        <div class="row">
          <div class="col-md-5">
          <div class="col-md-3">
            <fg-input type="text"
                      label="Username"
                      placeholder="Username"
                      v-model="username">
            </fg-input>
          </div>
          <div class="col-md-4">
            <fg-input type="email"
                      label="Email"
                      placeholder="Email"
                      v-model="email">
            </fg-input>
          </div>
        </div>
        <div class="text-center">
          <p-button type="info"
                    round
                    @click.native.prevent="inicarSesion()">
            Iniciar Sesión
          </p-button>
        </div>
        <div class="clearfix"></div>
      </form>
    </div>
  </card>
</template>

<script>
export default {
    data() {
        return {
            email: '',
            password: '',
            errorM:null
        }
    },
    methods: {
        inicarSesion(){
            axios.post('usuario/login',{email: this.email, password: this.password})
            .then(respuesta =>{
                return respuesta.data;
            })
            .then(data =>{
                this.$store.dispatch("guardarToken", data.tokenReturn);
                this.$router.push({name: 'dashboard'});
            })
            .catch(error =>{
                //console.log(error);
                this.errorM=null;
                if (error.response.status == 404){
                    this.errorM='No exíste el usuario o las credenciales son incorrectas';
                } else {
                    this.errorM='Ocurrió un error con el servidor';
                }
            });
        }
    }
}
</script>