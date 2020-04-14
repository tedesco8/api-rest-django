<template>
    <v-container fluid>
         <Maps :control="control" />
    </v-container>
</template>
<script>
import Maps from '../components/Maps.vue'

export default {
   data() 
    {
        return {
            control: true
        }
    },
    components: {
      Maps
    }
}
</script>
<style lang="sass">

</style>