<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <v-flex xs12>
        <v-img
          :src="require('../assets/SGRC.png')"
          class="my-3"
          contain
          height="200"
        ></v-img>
      </v-flex>

      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">
          Bienvenido a SGRC
        </h1>
        <h3>
          Sistema de Gestión de Recolección de Colillas
        </h3><br>
        <p class="subheading font-weight-regular">
          Este es un sistema pensado y desarrollado por el grupo OutboxDev para el emprendimiento Ecológista
           <a href="https://www.instagram.com/nomascolillas_uy/?hl=es-la" target="_blank">No más Colillas Uruguay</a> 
          <br>en el marco del proyecto final de primer año en Programa b_IT - CUTI / INEFOP.
          <br>Por más información puede visitar el sitio web de
          <a href="https://www.cuti.org.uy/public/common/b-it/" target="_blank">Programa b_IT</a>
        </p>
      </v-flex>

      <v-flex
        mb-5
        xs12
      >
        <h2 class="headline font-weight-bold mb-3">¿Quiénes somos?</h2>

        <p>Somos un grupo de estudiantes abocados a diferentes especialidades, el complemento ideal para formar el mejor equipo y brindar las mejores soluciones.
          <br>Ponte en contacto con <a href="http://outboxdev.net/" target="_blank">OutboxDev</a>
          </p>
      </v-flex>

      
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    ecosystem: [
      {
        text: 'vuetify-loader',
        href: 'https://github.com/vuetifyjs/vuetify-loader',
      },
      {
        text: 'github',
        href: 'https://github.com/vuetifyjs/vuetify',
      },
      {
        text: 'awesome-vuetify',
        href: 'https://github.com/vuetifyjs/awesome-vuetify',
      },
    ],
    importantLinks: [
      {
        text: 'Documentation',
        href: 'https://vuetifyjs.com',
      },
      {
        text: 'Chat',
        href: 'https://community.vuetifyjs.com',
      },
      {
        text: 'Made with Vuetify',
        href: 'https://madewithvuejs.com/vuetify',
      },
      {
        text: 'Twitter',
        href: 'https://twitter.com/vuetifyjs',
      },
      {
        text: 'Articles',
        href: 'https://medium.com/vuetify',
      },
    ],
    whatsNext: [
      {
        text: 'Explore components',
        href: 'https://vuetifyjs.com/components/api-explorer',
      },
      {
        text: 'Select a layout',
        href: 'https://vuetifyjs.com/layout/pre-defined',
      },
      {
        text: 'Frequently Asked Questions',
        href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
      },
    ],
  }),
};
</script>
