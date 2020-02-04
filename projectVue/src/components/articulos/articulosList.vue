<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado de Artículos</h2>
                <div class="col-md-12">
                    <b-table striped hover :items="articulos" :fields="fields">
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
                {key: 'title', label: 'Título'},
                {key: 'description', label: 'Descripción'},
                {key: 'action', label: 'Acción'}
            ],
            articulos: []
        }
    },
    methods: {
        getArticulos() {
            const path = 'localhost:8000/api/v1/productos'
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