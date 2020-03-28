<template>
    <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
    <v-container fluid>
        <v-layout row mt-2 wrap style="height:450px">
          <v-flex class = "lighten" md4>
            <v-card
              heigth="100%"
              class="mx-auto"
              fluid
            >
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title class="headline">Salvemos el planeta</v-list-item-title>
                  <v-list-item-subtitle>by Kurt Wagner</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
          
              <v-img
                :src="require('../assets/salvar-planeta.jpg')"
                height="194"
              ></v-img>
          
              <v-card-text>
                  Quieres transformarte en colaborador? Unete a la
                  comunidad mas grande de latinoamerica en reciclaje de colillas      
              </v-card-text>
          
              <v-card-actions>
                <v-btn
                  text
                  color="deep-purple accent-4"
                >
                  Unirse
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon>mdi-heart</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>mdi-share-variant</v-icon>
                </v-btn>
              </v-card-actions>
    </v-card>
              <!-- <p class = "text-sm-center">
                Busque los contenedores mas cercanos. Haga click sobre uno de ellos y 
                se le informara los datos para coordinar con el colaborador.
              </p>
              <p class="text-sm-center">Quieres transformarte en colaborador? Unete a la
                comunidad mas grande de latinoamerica en reciclaje de colillas
              </p>
              <v-btn color = "secundary">
                <v-icon left>forum</v-icon>
                  Quiero Colaborar
              </v-btn> -->
          </v-flex>
          <v-flex class="purple darken-4" md8>
            <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d26175.6067641435!2d-56.190242775252905!3d-34.907683038461066!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x959f81cb78209d13%3A0xfaf367ad3024da1c!2sIntendencia%20de%20Montevideo!5e0!3m2!1ses-419!2suy!4v1584736945626!5m2!1ses-419!2suy" width="100%" height="100%" frameborder="0" style="border:0;" allowfullscreen="" aria-hidden="false" tabindex="0"></iframe>
          </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
    export default {
        name: 'Maps'
    }
</script>
<style>

</style>