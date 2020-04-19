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
                     <!--Modal agregar o editar Contenedores-->
                    <v-dialog v-model="dialog" max-width="500px">
                        <v-card>
                            <v-card-title>
                            <span class="headline">Gestion del Contenedor</span>
                            </v-card-title>
                            <v-card-text>
                                <v-container grid-list-md>
                                    <v-layout wrap>
                                        <v-flex xs12 sm12 md12>
                                            <v-img src="../assets/contenedor.png" aspect-ratio="1.7"></v-img>
                                        </v-flex>
                                        <v-flex xs12 sm12 md12>
                                            <h2>ID: {{_id}}</h2>
                                        </v-flex>
                                        <v-flex xs12 sm12 md12>
                                            <v-text-field v-model="descripcion" label="Descripción"></v-text-field>
                                        </v-flex>
                                        <v-flex xs12 sm12 md12>
                                            <v-slider v-model="errorCount" label="Capacidad" min="0" max="4"></v-slider>
                                        </v-flex>
                                        <v-textarea
                                            v-model="comment"
                                            :rules="commentRules"
                                            label="Incidencias"
                                        ></v-textarea>
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
                </v-toolbar>
                <v-data-table :headers="headers" :items="contenedores" :search="search" class="elevation-1">
                    <template v-slot:item.opciones="{item}">
                        <v-tooltip v-model="show" top>
                            <template v-slot:activator="{ on }">
                                <v-icon v-on="on" small class="mr-2" @click="editItem(item)">edit</v-icon>
                            </template>
                            <span>Editar</span>
                        </v-tooltip>
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
            dialog: false,
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
            errorCount: 1,
        }
    },
    props: {
        headers: Array,
        contenedores: Array
    },
    watch: {
        dialog(val) {
            val || this.close();
        }
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
        close() {
            this.dialog = false;
        }
    }
}
</script>