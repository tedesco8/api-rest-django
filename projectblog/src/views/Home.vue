<template>
  <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
  <v-container fluid>
    <!--Layout funciona como el row de bootstrap, para trabajar con una fila y el sistema. Wrap es para que no se pise y respete el sistema-->
    <v-layout class = "secondary" justify-center align-center style="height:300px">
      <v-flex class="info" md3>
        <h2>Centrado</h2>
      </v-flex>
      <v-flex class="success" md3>
        <h2>Centrado</h2>
      </v-flex>
    </v-layout>
    <v-layout wrap>
      <v-flex class="pink lighten" md6>
          <h1>
            Probando grilla
          </h1>
      </v-flex>
      <v-flex class="purple darken-4" md6>
        <h1>
            Probando grilla
          </h1>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>

export default {
 
}
</script>
