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
   import axios from 'axios';
   import Map from '../components/Map.vue'
    export default {
        name: 'Maps',
        data() {
            return {
                //es brew
                cont: []
            }
        },
         components: {
            Map
        },
        mounted: function () {
          axios.get('api/coordenadas/coordenadas/?activo=true')
            .then( r => {
              this.cont = r.data.results;
            })
        }
    }
</script>
<style>

</style>