<template>
  <v-container fluid>
    <!--SLIDER-->
      <Slider />
    <!--MAPA-->
      <Map />
    <!--CARDS-->
      <Card />
  </v-container>
</template>

<script>
  import Map from '../components/Maps.vue'
  import Slider from '../components/Slider.vue'
  import Card from '../components/Cards.vue'

  export default {
    components: {
      Map,
      Slider,
      Card
    }
  
  }
</script>
