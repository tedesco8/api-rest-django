<template>
  <v-container fluid>
    <!--SLIDER-->
      <Slider />
    <!--PRESENTATION-->
      <Presentation />
      <!--PARALLAX-->
      <Parallax />
    <!--MAPA-->
      <Maps :contenedores="contenedores"/>
      
    <!--CARDS-->
      <Card />
  </v-container>
</template>

<script>
  import axios from "axios";
  import Maps from '../components/Maps.vue'
  import Slider from '../components/Slider.vue'
  import Card from '../components/Cards.vue'
  import Presentation from '../components/Presentation.vue'
  import Parallax from '../components/Parallax.vue'

  export default {
    data() 
    {
        return {
            contenedores: []
        }
    },
    components: {
      Maps,
      Slider,
      Card,
      Presentation,
      Parallax
    },
    mounted: function () {
      axios.get('api/coordenadas/coordenadas/?activo=true')
      .then( r => {
        this.contenedores = r.data.results;
      })
      .catch(function(error) {
        console.log(error);
      })
    }
  
  }
</script>
