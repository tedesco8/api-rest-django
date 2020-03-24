<template>
  <v-fragment>
    <!--SLIDER-->
      <Slider />
    <!--MAPA-->
      <Map />
    <!--CARDS-->
      <Card />
  </v-fragment>
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
