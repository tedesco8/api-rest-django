<template>
    <!--Container centra todo nuestro contenido, con el atributo fluid se pega mas a los bordes-->
    
    <v-carousel>
      <v-carousel-item
        v-for="(item,i) in items"
        :key="i"
        :src="item.src"
        reverse-transition="fade-transition"
        transition="fade-transition"
      ></v-carousel-item>
    </v-carousel>

</template>
<script>
    export default {
        name: 'Slider',
        data() {
            return {
              items: [
                {
                  src: require('../assets/Carrousel/1.jpg'),
                },
                {
                  src: require('../assets/Carrousel/2.jpg'),
                },
                {
                  src: require('../assets/Carrousel/3.jpg'),
                },
                {
                  src: require('../assets/Carrousel/4.jpg'),
                },
                {
                  src: require('../assets/Carrousel/5.jpg'),
                },
              ],
          }
        }
    }
</script>
<style>

</style>