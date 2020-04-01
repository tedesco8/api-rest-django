<template>
  <v-container fluid>
    <!--SLIDER-->
      <Slider />
    <!--MAPA-->
      <Map />
      <Parallax />
    <!--CARDS-->
      <Card />
  </v-container>
</template>

<script>
  import Map from '../components/Maps.vue'
  import Slider from '../components/Slider.vue'
  import Card from '../components/Cards.vue'
  import Parallax from '../components/Parallax.vue'

  export default {
    components: {
      Map,
      Slider,
      Card,
      Parallax
    }
  
  }
</script>
