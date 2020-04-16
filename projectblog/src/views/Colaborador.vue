<template>
    <v-container fluid>
        <v-toolbar>
            <v-tabs
                dark
                background-color="secondary"
                grow
            >
                <v-tab>
                    <v-badge
                        color="pink"
                        dot
                    >
                        Llenos
                    </v-badge>
                    
                </v-tab>
        
                <v-tab>
                <v-badge
                    color="green"
                    content="6"
                >
                    Activos
                </v-badge>
                </v-tab>
        
                <v-tab>
                <v-badge
                    color="deep-purple accent-4"
                    icon="mdi-vuetify"
                >
                    Resultados
                </v-badge>
                </v-tab>
            </v-tabs>
        </v-toolbar>
         <Maps :contenedores="contenedores" />
         <Table :headers="headers" :contenedores="contenedores" />
    </v-container>
</template>
<script>
import axios from "axios";
import Maps from '../components/Maps.vue'
import Table from '../components/Table.vue'

export default {
   data() 
    {
        return {
            user: 13,
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
            ]
        };
    },
    components: {
      Maps,
      Table
    },
    mounted: function () {
        axios.get(`api/coordenadas/coordenadas/${this.user}/propios/`)
        .then( r => {
            this.contenedores = r.data;
        })
        .catch(function(error) {
            console.log(error);
        })
    }
}
</script>