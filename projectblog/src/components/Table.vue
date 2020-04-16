<template>
    <v-container fluid>
        <v-data-table :headers="headers" :items="contenedores" :search="search" class="elevation-1">
        </v-data-table>
    </v-container>
</template>
<script>
    export default {
        props: {
            headers: Array,
            contenedores: Array
        }
    }
</script>