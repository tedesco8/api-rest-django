<template>
  <v-app>
    <!-- HEADER -->
    <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="teal primary"
      dark
    >
      <v-toolbar-title
        style="width: 300px"
        class="ml-0 pl-3"
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <span class="hidden-sm-and-down">No Más Colillas Uruguay</span>
      </v-toolbar-title>
      
      <v-spacer></v-spacer>
      <v-btn @click="salir()" icon v-if="logueado">
        <v-icon>logout</v-icon>
      </v-btn>
      <v-btn :to="{name: 'login'}" icon v-else>
        <v-icon>apps</v-icon>
      </v-btn>
    </v-app-bar>
    <!-- MENU -->
    <v-navigation-drawer
      v-model="drawer"
      app
      temporary dark
      :clipped="$vuetify.breakpoint.lgAndUp"
    >
      <v-list dense>
        <template>
          <v-list-item :to="{name: 'Home'}">
            <v-list-item-action>
              <v-icon>home</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Inicio
            </v-list-item-title>
          </v-list-item>
        </template>
        <template>
          <v-list-item :to="{name: 'Blog'}">
            <v-list-item-action>
              <v-icon>assignment</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Blog
            </v-list-item-title>
          </v-list-item>
        </template>
        <template>
          <v-list-item :to="{name: 'About'}">
            <v-list-item-action>
              <v-icon>all_out</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Quienes Somos
            </v-list-item-title>
          </v-list-item>
        </template>
        <template>
          <v-list-item :to="{name: 'Contact'}">
            <v-list-item-action>
              <v-icon>contact_mail</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Contacto
            </v-list-item-title>
          </v-list-item>
        </template>
      </v-list>
    </v-navigation-drawer>
    <!-- CONTENIDO -->
    <v-content>
      <v-container
        fluid
        fill-height
      >
        <v-slide-y-transition mode="out-in">
          <router-view/>
        </v-slide-y-transition>
      </v-container>
    </v-content>
    <!-- FOOTER -->
  <v-footer
    dark
    padless
  >
    <v-card
      class="flex"
      flat
      tile
    >
      <v-card-title color="primary" class="teal">
        <strong class="subheading">No te olvides de seguirnos en nuestras redes sociales!</strong>

        <v-spacer></v-spacer>

        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4"
          dark
          icon
        >
          <v-icon size="24px">{{ icon }}</v-icon>
        </v-btn>
      </v-card-title>

      <v-card-text class="py-2 white--text text-center">
        &copy; {{ new Date().getFullYear() }} <strong>No Más Colillas Uruguay</strong>
      </v-card-text>
    </v-card>
  </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      drawer: false,
      icons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-google-plus',
        'fab fa-linkedin',
        'fab fa-instagram',
      ],
    }
  }
};
</script>
