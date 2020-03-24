<template>
        <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
        <v-container grid-list-md>
            <v-layout row wrap>
                <v-flex xs12 sm6 md3>
                    <v-card v-for="(item, index) in post" v-bind:key="item">
                        <v-img>
                           {{index}}. {{post.cover}}
                        </v-img>
                        <v-card-title>
                            <h2>{{post.title}}</h2>
                        </v-card-title>
                        <v-card-text>
                            <p>{{post.description}}</p>
                        </v-card-text>
                        <v-card-actions>
                        
                        </v-card-actions>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
</template>

<script>
    export default {
        name: 'Cards',
        data() {
            return {
                post: [
                    {
                        title: 'Fotos que nos llegan desde el Este!',
                        description: 'Personas comprometidas con las playas, que depositan sus colillas en los ceniceros de @teko.uy',
                        cover: require('../assets/NMC1.png')
                    },
                    {
                        title: 'Hoy cubrimos nuestro primer evento en Montevideo',
                        description: 'Teniendo como resultado la recolección de más de 1000 colillas de cigarros que se encontraban en el Parque Rodó'
                    }
                ]
            }
        }
    }
</script>

<style>

</style>