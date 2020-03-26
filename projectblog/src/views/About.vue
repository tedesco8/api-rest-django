<template>
  <v-content>
      <v-img style="height:300px" src="../assets/QSM.jpg">
        <v-row align="end" class="lightbox white--text pa-2 fill-height">
          <v-col>
            <v-container>
              <div>Quienes Somos</div>
            </v-container>
          </v-col>
        </v-row>
      </v-img>
    <div class="block">
      <v-container>
        <p class="text-center">Nuestro objetivo es reducir el impacto negativo de las colillas de cigarro
          en el medio ambiente, a través de la concientización y la recolección
        </p>
      </v-container>
    </div>
    <Team />
  </v-content>
</template>
<script>
import Team from '../components/Team.vue'
export default {
  components: {
    Team
  }
}
</script>