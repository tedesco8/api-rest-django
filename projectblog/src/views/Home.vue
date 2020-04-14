<template>
  <v-container fluid>
    <!--SLIDER-->
      <Slider />
    <!--PRESENTATION-->
      <Presentation />
      <!--PARALLAX-->
      <Parallax />
    <!--MAPA-->
      <Maps :control="control"/>
      
    <!--CARDS-->
      <Card />
  </v-container>
</template>

<script>
  import Maps from '../components/Maps.vue'
  import Slider from '../components/Slider.vue'
  import Card from '../components/Cards.vue'
  import Presentation from '../components/Presentation.vue'
  import Parallax from '../components/Parallax.vue'

  export default {
    data() 
    {
        return {
            control: false
        }
    },
    components: {
      Maps,
      Slider,
      Card,
      Presentation,
      Parallax
    }
  
  }
</script>
