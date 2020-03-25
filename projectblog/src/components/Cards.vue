<template>
        <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
        <v-container grid-list-md fluid>
            <v-layout row wrap>
                <v-flex 
                v-for="item in post" 
                v-bind:key="item"
                xs12 sm6 md3
                >
                    <v-card>
                        <v-img :src="item.cover">
                        </v-img>
                        <v-card-title>
                            <h5>{{item.title}}</h5>
                        </v-card-title>
                        <v-card-text>
                            <p>{{item.description}}</p>
                        </v-card-text>
                        <v-card-actions>
                            <v-btn color="info" flat>Ver más</v-btn>
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
                        description: 'Fotos que nos llegan de personas comprometidas con las playas, que depositan sus colillas en los ceniceros de @teko.uy',
                        cover: require('../assets/NMC1.png')
                    },
                    {
                        title: 'Hoy cubrimos nuestro primer evento en Montevideo',
                        description: 'Teniendo como resultado la recolección de más de 1000 colillas de cigarros que se encontraban en el Parque Rodó',
                        cover: require('../assets/NMC2.png')
                    },
                    {
                        title: 'Entre todos, reducir la contaminación es posible!',
                        description: 'Este cuarto contenedor lo podrán encontrar en frente a OVO, sobre playa mansa (Punta del Este, Maldonado)',
                        cover: require('../assets/NMC3.png')
                    },
                    {
                        title: 'Creando consciencia y accionando',
                        description: 'Creando consciencia junto a un grupo de voluntarios y personas dispuestas a cambiar el planeta, pasando de las ganas a la acción',
                        cover: require('../assets/NMC4.png')
                    }
                ]
            }
        }
    }
</script>

<style>

</style>