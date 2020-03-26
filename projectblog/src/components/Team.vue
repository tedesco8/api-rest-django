<template>
    <v-container>
        <h2 class="text-center">Nuestro Equipo</h2>
        <v-row>
            <v-col 
                cols="4"
                v-for="item in items" 
                :key="item.id"
            >
                <v-card
                flat
                class="mx-auto"
                >
                    <v-img
                        class="white--text align-end img-circle"
                        :src="item.src"
                        cycle
                    >
                    </v-img>

                    <v-card-text class="text--primary text-center">
                        <h4>{{item.name}}</h4>
                        <p>{{item.title}}</p>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>
<script>
    export default {
        name: 'Slider',
            data() {
                return {
                    items: [
                        {
                            id: 1,
                            src: require('../assets/Carrousel/LogoNMC.jpg'),
                            name: 'Fernando Machado',
                            title: 'Founder'
                        },
                        {
                            id: 2,
                            src: require('../assets/Carrousel/LogoNMC.jpg'),
                            name: 'David Pereira',
                            title: 'Co-Founder'
                        },
                        {
                            id: 3,
                            src: require('../assets/Carrousel/LogoNMC.jpg'),
                            name: 'Jose estevez',
                            title: 'Partner'
                        },
                    ],
                }
            }
    }
</script>
<style scoped>
    .img-circle {
        border-radius: 100%;
    }
</style>