<template>
    <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
    <v-container fluid>
        <v-layout row mt-2 wrap style="height:450px">
          <v-flex class="purple darken-4" md12>
            <Map :cont="cont"/>
          </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
/* eslint-disable no-debugger */
   import axios from 'axios';
   import Map from '../components/Map.vue'
    export default {
        name: 'Maps',
        data() {
            return {
                //es brew
                cont: [],
                user: 8
            }
        },
        props: {
            control: Boolean
        },
        components: {
            Map
        },
        mounted: function () {
          debugger;
          let me = this;
          if(me.props.control) {
            axios.get(`api/coordenadas/coordenadas/?colaborador=${this.user}`)
            .then( r => {
              this.cont = r.data.results;
            })
            .catch(function(error) {
              console.log(error);
            })
          } else {
            axios.get('api/coordenadas/coordenadas/?activo=true')
            .then( r => {
              this.cont = r.data.results;
            })
            .catch(function(error) {
              console.log(error);
            })
          }
        }
    }
/* eslint-disable no-debugger */
</script>
<style>

</style>