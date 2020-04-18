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
    /* eslint-disable no-debugger */
    mounted: function () {
      debugger;
      axios.get(`api/coordenadas/coordenadas/True/activos/`)
      .then( r => {
        this.contenedores = r.data;
      })
      .catch(function(error) {
        console.log(error);
      })
    }
    /* eslint-disable no-debugger */
  
  }
</script>
