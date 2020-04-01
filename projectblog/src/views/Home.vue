<template>
  <v-container fluid>
    <!--SLIDER-->
      <Slider />
    <!--PRESENTATION-->
      <Presentation />
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
  import Presentation from '../components/Presentation.vue'

  export default {
    components: {
      Map,
      Slider,
      Card,
      Presentation
    }
  
  }
</script>
