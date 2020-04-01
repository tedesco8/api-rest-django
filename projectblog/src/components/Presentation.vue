<template>
        <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
         <section
        id="features"
        class="white"
      >
        <div class="py-12"></div>

        <v-container class="text-center">
          <!-- <h2 class="display-2 font-weight-bold mb-3">VUETIFY FEATURES</h2> -->

          <!-- <v-responsive
            class="mx-auto mb-12"
            width="56"
          >
            <v-divider class="mb-1"></v-divider>

            <v-divider></v-divider>
          </v-responsive> -->

          <v-row>
            <v-col
              v-for="({ icon, title, text }, i) in features"
              :key="i"
              cols="12"
              md="4"
            >
              <v-card
                class="py-12 px-4"
                color="grey lighten-4"
                flat
              >
                <v-theme-provider dark>
                  <div>
                    <v-avatar
                      color="primary"
                      size="88"
                    >
                      <v-icon
                        large
                        v-text="icon"
                      ></v-icon>
                    </v-avatar>
                  </div>
                </v-theme-provider>

                <v-card-title
                  class="justify-center font-weight-black text-uppercase"
                  v-text="title"
                ></v-card-title>

                <v-card-text
                  class="headline"
                  v-text="text"
                >
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-container>

        <div class="py-12"></div>
      </section>
</template>

<script>
    export default {
        name: 'Presentation',
        data() {
            return {
                features: [
          {
            icon: 'fingerprint',
            title: 'Consciencia Ecológica',
            text: 'Juntos podemos revertir el impacto en el medio ambiente, acompañanos en esta aventura dejando tu huella.',
          },
          {
            icon: 'public',
            title: 'Vision Global',
            text: 'Somos una comunidad global y coordinada trabajando en conjunto para cumplir un mimso objetivo.',
          },
          {
            icon: 'people_outline',
            title: 'Comunidad Activa',
            text: 'La movilizacion atravez de la conscientizacion ciuidadana es clave para acabar con el problema de las colillas.',
          },
        ]
            }
        }
    }
</script>

<style>

</style>