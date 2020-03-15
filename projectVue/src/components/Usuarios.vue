<template>
  <v-layout align-start>
    <v-flex>
      <v-toolbar text color="white">
        <v-toolbar-title>Usuarios</v-toolbar-title>
        <v-divider class="mx-2" inset vertical></v-divider>
        <v-spacer></v-spacer>
        <v-text-field
          class="text-xs-center"
          v-model="search"
          append-icon="search"
          label="Búsqueda"
          single-line
          hide-details
        ></v-text-field>
        <v-spacer></v-spacer>
        <!--Modal agregar o editar usuario-->
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on }">
            <v-btn color="primary" dark class="mb-2" v-on="on">Nuevo</v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">{{ formTitle }}</span>
            </v-card-title>
            <v-card-text>
              <v-container grid-list-md>
                <v-layout wrap>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.username" label="Username"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.email" label="Email"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm12 md12>
                    <v-text-field type="password" v-model="password" label="Password"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm12 md12>
                    <v-text-field type="password" v-model="password_repeat" label="Repetir password"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.first_name" label="Nombre"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.last_name" label="Apellido"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.profile.dni" label="DNI"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.profile.phone" label="Telefono"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="user.profile.address" label="Dirección"></v-text-field>
                  </v-flex>
                   <v-flex xs12 sm6 md6>
                    <v-select v-model="rol" :items="roles" label="Rol"></v-select>
                  </v-flex>
                  <!-- <v-flex xs12 sm6 md6>
                    <v-select v-model="user.profile.city" :items="cities" label="Cities"></v-select>
                  </v-flex>                   -->
                  <v-flex xs12 sm4 md4>
                    <v-checkbox v-model="user.is_active" label="Es activo"></v-checkbox>
                  </v-flex>
                  <v-flex xs12 sm4 md4>
                    <v-checkbox v-model="user.is_staff" label="Es staff"></v-checkbox>
                  </v-flex>
                  <v-flex xs12 sm4 md4>
                    <v-checkbox v-model="user.is_superuser" label="Es admin"></v-checkbox>
                  </v-flex>

                  <v-flex xs12 sm12 md12 v-show="valida">
                    <div class="red--text" v-for="v in validaMensaje" :key="v" v-text="v"></div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="blue darken-1" text @click="close">Cancelar</v-btn>
              <v-btn color="blue darken-1" text @click="guardar">Guardar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!--Modal activar o desactivar-->
        <v-dialog v-model="adModal" max-width="290">
          <v-card>
            <v-card-title class="headline" v-if="adAccion==1">Activar Item</v-card-title>
            <v-card-title class="headline" v-if="adAccion==2">Desactivar Item</v-card-title>
            <v-card-text>
              Estás a punto de
              <span v-if="adAccion==1">activar</span>
              <span v-if="adAccion==2">desactivar</span>
              el item {{adNombre}}
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn @click="activarDesactivarCerrar()" color="green darken-1" text="text">Cancelar</v-btn>
              <v-btn
                v-if="adAccion==1"
                @click="activar()"
                color="orange darken-4"
                text="text"
              >Activar</v-btn>
              <v-btn
                v-if="adAccion==2"
                @click="desactivar()"
                color="orange darken-4"
                text="text"
              >Desactivar</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-toolbar>
      <!--Tabla-->
      <v-data-table :headers="headers" :items="usuarios" :search="search" class="elevation-1">
        <template v-slot:item.groups="{item}">
        <div v-if="item.groups.length>0">
          <span v-for="group in item.groups" :key="group">{{ " " + group.name }}</span>
        </div>
        </template>
        <!--Editar-->
        <template v-slot:item.opciones="{item}">
          <v-icon small class="mr-2" @click="editItem(item)">edit</v-icon>
          <div v-if="item.estado">
            <v-icon small @click="activarDesactivarMostrar(2,item)">block</v-icon>
          </div>
          <div v-else>
            <v-icon small @click="activarDesactivarMostrar(1,item)">check</v-icon>
          </div>
        </template>
        <!--Estado-->
        <template v-slot:item.is_active="{item}">
          <div v-if="item.is_active">
            <span class="blue--text">Activo</span>
          </div>
          <div v-else>
            <span class="red--text">Inactivo</span>
          </div>
        </template>
        <!--Resetear-->
        <template v-slot:no-data>
          <v-btn color="primary" @click="listar()">Resetear</v-btn>
        </template>
      </v-data-table>
    </v-flex>
  </v-layout>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      dialog: false,
      search: "",
      usuarios: [],
      headers: [
        { text: "Id", value: "id", sortable: true },
        { text: "Username", value: "username", sortable: true },        
        { text: "Nombre", value: "first_name", sortable: false },
        { text: "Apellido", value: "last_name", sortable: false },
        // { text: "Dirección", value: "direccion", sortable: false },
        // { text: "DNI", value: "profile", sortable: false },
        // { text: "Teléfono", value: "profile", sortable: false },
        { text: "Email", value: "email", sortable: false },
        { text: "Rol", value:"groups", sortable: true },        
        { text: "Estado", value: "is_active", sortable: false },
        { text: "Opciones", value: "opciones", sortable: false }
      ],
      editedIndex: -1,
      _id: "",
      user:{
        id:null,
        first_name:null,
        last_name:null,
        email:null,        
        username:null,
        is_staff:false,
        is_active:false,
        is_superuser:false,
        groups:[],
        profile:{}
      },
      cities:[],
      rol: "",
      roles: [
        {
          text:"Usuario",
          value:2
        },
        {
          text:"Colaborador",
          value:1
        }
      ],

      valida: 0,
      validaMensaje: [],
      adModal: 0,
      adAccion: 0,
      adNombre: "",
      adId: "",
      password: "",
      password_repeat:"",
    };
  },
  computed: {
    formTitle() {
      return this.editedIndex === -1 ? "Nuevo registro" : "Editar registro";      
    }
  },
  watch: {
    dialog(val) {
      val || this.close();
    }
  },
  created() {
    this.listar();
    this.selectCiudades();
  },
  methods: {
    selectCiudades(){
      let me = this;
      let token = this.$store.state.tokens;
      const access = token.access;
      let cuerpoHeader = `Bearer ${access}`;
      let header = { Authorization: cuerpoHeader };
      let configuracion = { headers: header }; 
      axios
        .get("/api/usuarios/cities/?no_paginate=1", configuracion)
        .then(function(response) {          
          //me.cities = response.data;
          me.cities = response.data.map(city=>{
            return{
              ...city,
              ...{text:city.name,value:city.id}
            }
          })
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    listar() {
     let me = this;
      let token = this.$store.state.tokens;
      const access = token.access;
      let cuerpoHeader = `Bearer ${access}`;
      let header = { Authorization: cuerpoHeader };
      let configuracion = { headers: header }; 
      axios
        .get("/api/usuarios/users?no_paginate=1", configuracion)
        .then(function(response) {
          //me.usuarios = response.data.results;
          me.usuarios = response.data;
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    limpiar() {
      this.user = {
        id:null,
        first_name:null,
        last_name:null,
        email:null,        
        username:null,
        is_staff:false,
        is_active:false,
        is_superuser:false,
        groups:[],
        profile:{},
      }
      this.rol = undefined;
      this.password = "";
      this.valida = 0;
      this.validaMensaje = [];
      this.editedIndex = -1;
    },
    validar() {
      this.valida = 0;      
      this.validaMensaje = [];
      return 0;
      // if (!this.rol) {
      //   this.validaMensaje.push("Seleccione un rol.");
      // }
      if (this.user.first_name.length < 1 || this.user.first_name.length > 50) {
        this.validaMensaje.push(
          "El nombre del usuario debe tener entre 1-50 caracteres."
        );
      }
      if (this.email.length < 1 || this.nombre.length > 50) {
        this.validaMensaje.push(
          "El email del usuario debe tener entre 1-50 caracteres."
        );
      }
      if (this.password.length < 1 || this.nombre.length > 64) {
        this.validaMensaje.push(
          "El password del usuario debe tener entre 1-64 caracteres."
        );
      }
      // if (this.profile.length > 20) {
      //   this.validaMensaje.push(
      //     "El documento no debe tener más de 20 caracteres."
      //   );
      // }
      // if (this.profile.length > 70) {
      //   this.validaMensaje.push(
      //     "La dirección no debe tener más de 70 caracteres."
      //   );
      // }
      // if (this.profile.length > 20) {
      //   this.validaMensaje.push(
      //     "El teléfono no debe tener más de 20 caracteres."
      //   );
      // }
      if (this.validaMensaje.length) {
        this.valida = 1;
      }
      return this.valida;
    },
    guardar() {
      let me = this;
      let token = this.$store.state.tokens;
      const access = token.access;
      let cuerpoHeader = `Bearer ${access}`;
      let header = { Authorization: cuerpoHeader };
      let configuracion = { headers: header };
      if (this.validar()) {
        return;
      }
      if (this.editedIndex > -1) {
        //Código para editar
        if(this.user.groups &&this.user.groups.length>0){
          const groups = this.user.groups;
          this.user.groups=[];
          groups.forEach(g=>{
            this.user.groups.push(g.id);
          });
        }
        if(this.rol){
          this.user.groups=[];
          this.user.groups.push(this.rol);
        }
        axios
          .put(
            `api/usuarios/users/${this.user.id}/`,
            this.user,
            configuracion
          )
          .then(function(response) {
            swal({
              title: "Buen trabajo!",
              text: "Usuario editado exitosamente",
              icon: "success"
            });
            me.limpiar();
            me.close();
            me.listar();
          })
          .catch(function(error) {
            console.log(error);
          });
      } else {
        //Código para guardar
        this.user.password=this.password;
        this.user.groups=[];
        if(this.rol){
          this.user.groups.push(this.rol);
        }
        axios
          .post(
            `api/usuarios/users/`,
            this.user,
            configuracion
          )
          .then(function(response) {
            swal({
              title: "Buen trabajo!",
              text: "Usuario agregado exitosamente",
              icon: "success"
            });
            me.limpiar();
            me.close();
            me.listar();
          })
          .catch(function(error) {
            console.log(error);
          });
      }
    },
    editItem(item) {      
      this.user=item;
      this.rol=this.user.groups[0] ? this.user.groups[0].id : undefined;
      this.dialog = true;
      this.editedIndex = 1;
    },
    activarDesactivarMostrar(accion, item) {
      this.adModal = 1;
      this.adNombre = item.nombre;
      this.adId = item._id;
      if (accion == 1) {
        this.adAccion = 1;
      } else if (accion == 2) {
        this.adAccion = 2;
      } else {
        this.adModal = 0;
      }
    },
    activarDesactivarCerrar() {
      this.adModal = 0;
    },
    activar() {
      let me = this;
      let header = { Token: this.$store.state.token };
      let configuracion = { headers: header };
      axios
        .put("usuario/activate", { _id: this.adId }, configuracion)
        .then(function(response) {
          swal({
              title: "Buen trabajo!",
              text: "Usuario activado exitosamente",
              icon: "success"
            });
          me.adModal = 0;
          me.adAccion = 0;
          me.adNombre = "";
          me.adId = "";
          me.listar();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    desactivar() {
      let me = this;
      let header = { Token: this.$store.state.token };
      let configuracion = { headers: header };
      axios
        .put("usuario/deactivate", { _id: this.adId }, configuracion)
        .then(function(response) {
          swal({
              title: "Buen trabajo!",
              text: "Usuario desactivado exitosamente",
              icon: "success"
            });
          me.adModal = 0;
          me.adAccion = 0;
          me.adNombre = "";
          me.adId = "";
          me.listar();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    close() {
      this.dialog = false;
      this.limpiar();
    }
  }
};
</script>