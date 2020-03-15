<template>
  <v-layout align-start>
    <v-flex>
      <v-toolbar text color="white">
        <v-toolbar-title>Contenedores</v-toolbar-title>
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
        <!--Modal agregar o editar Contenedores-->
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
                    <v-select v-model="colaborador" :items="colaboradores" label="Colaborador"></v-select>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="peso" label="Peso"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm12 md12>
                    <v-text-field v-model="descripcion" label="Descripción"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="lat" label="Latitud"></v-text-field>
                  </v-flex>
                  <v-flex xs12 sm6 md6>
                    <v-text-field v-model="lng" label="Longitud"></v-text-field>
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
              el contenedor {{selectedItem?selectedItem.nombre:""}}
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
      <v-data-table :headers="headers" :items="contenedores" :search="search" class="elevation-1">
        <!--Editar-->
        <template v-slot:item.opciones="{item}">
          <v-icon small class="mr-2" @click="editItem(item)">edit</v-icon>
          <!--Activar/Desactivarr-->
          <div v-if="item.activo">
            <v-icon small @click="activarDesactivarMostrar(2,item)">block</v-icon>
          </div>
          <div v-else>
            <v-icon small @click="activarDesactivarMostrar(1,item)">check</v-icon>
          </div>
        </template>
        <!--Activar o desactivar-->
        <template v-slot:item.activo="{item}">
          <div v-if="item.activo">
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
      contenedores: [],
      headers: [
        { text: "Id", value: "id", sortable: true },
        { text: "Colaborador", value: "colaborador", sortable: true },
        { text: "Descripción", value: "descripcion", sortable: false },
        { text: "Peso", value: "weight", sortable: true },
        { text: "Latitud", value: "lat", sortable: false },
        { text: "Longitud", value: "lng", sortable: false },
        { text: "Estado", value: "activo", sortable: false },
        { text: "Opciones", value: "opciones", sortable: false }
      ],
      editedIndex: -1,
      _id: "",
      colaborador: "",
      colaboradores: [],
      descripcion: "",
      peso: "",
      lat: "",
      lng: "",
      valida: 0,
      validaMensaje: [],
      adModal: 0,
      adAccion: 0,
      selectedItem: "",
      adNombre: "",
      adId: ""
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
    this.listar(), this.selectColaboradores();
  },
  methods: {
    listar(){      
      let me = this;
      let token = this.$store.state.tokens;
      const access = token.access;
      let cuerpoHeader = `Bearer ${access}`;
      let header = { Authorization: cuerpoHeader };
      let configuracion = { headers: header };      
      axios
      .get("/api/contenedores/contenedores/", configuracion)
      .then(function(response) {        
        me.contenedores = response.data.results;        
      })
      .catch(function(error) {
        alert(error.toString());
        console.log(error);
      });      
    },
    selectColaboradores() {
      let me = this;
      let colaboradoresArray = [];
      let token = this.$store.state.tokens;
      const access = token.access;
      let cuerpoHeader = `Bearer ${access}`;
      let header = { Authorization: cuerpoHeader };
      let configuracion = { headers: header };
      axios
        .get("/api/usuarios/users/?no_paginate=1&roles=colaborador", configuracion)
        .then(function(response) {
          colaboradoresArray = response.data;
          /*colaboradoresArray.forEach(function(x) {
            me.colaboradores.push({ text: x.username, value: x.id });
          });*/
          me.colaboradores=colaboradoresArray.map(c=>{return {text:c.username,value:c.id}});
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    limpiar() {
      this._id = "";
      this.colaborador = "";
      this.descripcion = "";
      this.peso = "";
      this.lat = "";
      this.lng= "";
      this.valida = 0;
      this.validaMensaje = [];
      this.editedIndex = -1;
    },
    validar() {
      this.valida = 0;
      this.validaMensaje = [];
      if (this.descripcion.length > 255) {
        this.validaMensaje.push(
          "La descripción del Contenedor no debe tener más de 100 caracteres."
        );
      }
      if (this.peso.length > 255) {
        this.validaMensaje.push(
          "El peso del contenedor es obligatorio, su unidad de medida es en kg"
        );
      }
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
        //PUT
        axios
          .put(
            `/api/contenedores/contenedores/${this._id}/`,
            {
              id: this._id,
              colaborador: this.colaborador,
              descripcion: this.descripcion,
              weight: this.peso,
              lat: this.lat,
              lng: this.lng
            },
            configuracion
          )
          .then(function(response) {
            swal({
              title: "Buen trabajo!",
              text: "Contenedor editado exitosamente",
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
        //POST
        axios
          .post(
            "/api/contenedores/contenedores/",
            { 
              colaborador: this.colaborador,
              descripcion: this.descripcion,
              weight: this.peso,
              lat: this.lat,
              lng: this.lng
            },
            configuracion
          )
          .then(function(response) {
            swal({
              title: "Buen trabajo!",
              text: "Contenedor agregado exitosamente",
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
      this._id = item.id;
      this.colaborador = item.colaborador;
      this.descripcion = item.descripcion;
      this.peso = item.weight;
      this.lat = item.lat;
      this.lng = item.lng;
      this.dialog = true;
      this.editedIndex = 1;
    },
    activarDesactivarMostrar(accion, item) {
      this.adModal = 1;            
      this.selectedItem = item;
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
      let header = { Authorization: `Bearer ${this.$store.state.tokens.access}` };
      let configuracion = { headers: header };
      axios
        .put(`/api/contenedores/contenedores/${this.selectedItem.id}/activate/`,{},configuracion)
        .then(function(response) {
          const item = response.data;
          swal({
              title: "Buen trabajo!",
              text: "Contenedor activado exitosamente",
              icon: "success"
            });
          me.adModal = 0;
          me.adAccion = 0;
          me.selectedItem = item;
          me.listar();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    desactivar() {
      let me = this;      
      let header = { Authorization: `Bearer ${this.$store.state.tokens.access}` };
      let configuracion = { headers: header };
      axios
        .put(`/api/contenedores/contenedores/${this.selectedItem.id}/deactivate/`,{},configuracion)
        .then(function(response) {
          const item = response.data;
          swal({
              title: "Buen trabajo!",
              text: "Contenedor desactivado exitosamente",
              icon: "success"
            });
          me.adModal = 0;
          me.adAccion = 0;
          me.selectedItem = item;
          me.listar();
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    close() {
      this.dialog = false;
    }
  }
};
</script>