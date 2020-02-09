<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de Artículos</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="articulos" :fields="fields">
                        <template v-slot:cell(action)="data">
                            <b-button size="sm" variant="primary">Editar</b-button>
                            <b-button size="sm" variant="danger">Eliminar</b-button>
                        </template>
                    </b-table>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import  axios from "axios";
export default {
    data () {
        return {
            fields: [
                {key: 'id', label: 'ID'},
                {key: 'descripcion', label: 'Descripción'},
                {key: 'fecha_creado', label: 'Creado'},
                {key: 'vendido', label: 'Vendido'},
                {key: 'subcategoria', label: 'Subcategoría'},
                {key: 'action', label: ''}
            ],
            articulos: []
        }
    },
    methods: {
        getArticulos() {
            const path = 'http://localhost:8000/api/v1/productos'
            axios.get(path)
            .then( response => {
                this.articulos = response.data
            })
            .catch(error => console.log(error))
        }
    },
    created(){
        this.getArticulos();
    }
}
</script>
<style lang="css" scoped>

</style>