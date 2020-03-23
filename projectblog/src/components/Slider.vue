<template>
    <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
    <v-container fluid>
        <!--Layout funciona como el row de bootstrap, para trabajar con una fila y el sistema. Wrap es para que no se pise y respete el sistema-->
        <v-layout class = "secondary" justify-center align-center style="height:300px">
          <v-flex class="info" xs3>
            <h2 class="text-sm-center">Centrado</h2>
          </v-flex>
          <v-flex class="success" xs3>
            <h2 class="text-sm-center">Centrado</h2>
          </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
    export default {
        name: 'Slider'
    }
</script>
<style>

</style>