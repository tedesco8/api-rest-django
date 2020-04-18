<template>
    <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
    <v-container fluid>
        <v-layout row mt-2 wrap style="height:450px">
          <v-flex class="purple darken-4" md12>
            <Map :contenedores="contenedores"/>
          </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
/* eslint-disable no-debugger */
   import Map from '../components/Map.vue'
    export default {
        name: 'Maps',
        data() {
            return {
                //es brew
                cont: [],
                user: 13
            }
        },
        props: {
            contenedores: Array
        },
        components: {
            Map
        }
    }
/* eslint-disable no-debugger */
</script>
<style>
    .container {
        z-index: 0;
    }
</style>