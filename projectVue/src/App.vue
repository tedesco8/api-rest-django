<template>
  <v-app id="app">
    <v-navigation-drawer
      v-model="drawer"
      :clipped="$vuetify.breakpoint.lgAndUp"
      app
      v-if="logueado"
    >
      <v-list dense>
        <!-- HOME -->
        <template>
          <v-list-item :to="{name: 'home'}">
            <v-list-item-action>
              <v-icon>home</v-icon>
            </v-list-item-action>
            <v-list-item-title>
              Inicio
            </v-list-item-title>
          </v-list-item>
        </template>

        <!-- CONTENEDORES -->
        <template>
          <v-list-group>
            <v-list-item slot="activator">
              <v-list-item-content>
                <v-list-item-title>
                  Contenedores
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: 'contenedores'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Activos
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: ''}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Reciclados
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </template>

        <!-- USUARIOS -->
        <template>
          <v-list-group>
            <v-list-item slot="activator">
              <v-list-item-content>
                <v-list-item-title>
                  Usuarios
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: 'usuario'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Administradores
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: 'colaboradores'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Colaboradores
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: 'usuarios'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Usuarios
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </template>
        
        <!-- REPORTES -->
        <template>
          <v-list-group>
            <v-list-item slot="activator">
              <v-list-item-content>
                <v-list-item-title>
                  Reportes
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: 'reporteIngresos'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Consulta Compras
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
            <v-list-item :to="{name: 'reporteVentas'}">
              <v-list-item-action>
                <v-icon>table_chart</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>
                  Consulta Ventas
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </template>   
      </v-list>
    </v-navigation-drawer>

  <!-- HEADER -->
    <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="teal darken-1"
      dark
    >
      <v-toolbar-title
        style="width: 300px"
        class="ml-0 pl-3"
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        <span class="hidden-sm-and-down">SGRC</span>
      </v-toolbar-title>
      
      <v-spacer></v-spacer>
      <v-btn @click="salir()" icon v-if="logueado">
        <v-icon>logout</v-icon>
      </v-btn>
      <v-btn :to="{name: 'login'}" icon v-else>
        <v-icon>apps</v-icon>
      </v-btn>
    </v-app-bar>
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
    <v-footer height="auto">
      <v-layout justify-center>
        <v-flex text-center>
          <v-card flat title color="primary" class="white--text">
            <v-card-text class="white--text pt-0">
              Developed By Outboxdev &copy;2019
            </v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-footer>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      drawer: true,
    }
  },
  computed:{
    logueado(){
      return this.$store.state.usuario;
    }
  },
  created(){
    this.$store.dispatch("autoLogin");
  },
  methods: {
    salir(){
      this.$store.dispatch("salir");
    }
  }
};
</script>
