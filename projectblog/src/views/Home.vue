<template>
  <!--SLIDER-->
    <Slider />
  <!--MAPA-->
    <Map />
  <!--CARDS-->
    <Card />
</template>

<script>
  import Map from './Maps'
  import Slider from './Slider'
  import Card from './Cards'

  export default {
    components: {
      Map,
      Slider,
      Card
    }
  
  }
</script>
