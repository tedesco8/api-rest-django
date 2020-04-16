<template>
    <v-container fluid>
        <v-layout>
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
                </v-toolbar>
                <v-data-table :headers="headers" :items="contenedores" :search="search" class="elevation-1">
                    <template v-slot:item.opciones="{item}">
                        <v-tooltip v-model="show" top>
                            <template v-slot:activator="{ on }">
                                <v-icon v-on="on" small class="mr-2" @click="editItem(item)">edit</v-icon>
                            </template>
                            <span>Editar</span>
                        </v-tooltip>
                        <!--Activar/Desactivarr-->
                        <div v-if="item.activo">
                            <v-tooltip v-model="show" top>
                            <template v-slot:activator="{ on }">
                                <v-icon v-on="on" small @click="activarDesactivarMostrar(2,item)">block</v-icon>
                            </template>
                            <span>Desactivar</span>
                            </v-tooltip>
                        </div>
                        <div v-else>
                            <v-tooltip v-model="show" top>
                            <template v-slot:activator="{ on }">
                                <v-icon v-on="on" small @click="activarDesactivarMostrar(1,item)">check</v-icon>
                            </template>
                            <span>Desactivar</span>
                            </v-tooltip>
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
                </v-data-table>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
export default {
    data() {
        return {
            search: "",
            id: "",
            colaborador: "",
            descripcion: "",
            peso: "",
            lat: "",
            lng: "",
            adModal: 0,
            adAccion: 0,
            selectedItem: "",
        }
    },
    props: {
        headers: Array,
        contenedores: Array
    },
    methods: {
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
    }
}
</script>