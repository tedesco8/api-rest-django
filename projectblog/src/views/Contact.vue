<template>
  <v-content class="pt-0">
      <v-img style="height:300px" src="../assets/QSM.jpg">
        <v-row align="end" class="lightbox white--text pa-2 fill-height">
          <v-col>
            <v-container>
              <div>Contacto</div>
            </v-container>
          </v-col>
        </v-row>
      </v-img>
        <v-container>
            <p class="text-center">Nuestro objetivo es reducir el impacto negativo de las colillas de cigarro
            en el medio ambiente, a través de la concientización y la recolección
            </p>
            <p class="text-center">Ante cualquier duda o consulta, no dude en escribirnos.
                Puede rellenar este formulario y uno de nuestros asistentes se comunicarà
                con usted a la brevedad.
            </p>
        </v-container>
        <v-form v-model="valid" @submit.prevent="sendEmail">
            <v-container>
                <v-row>
                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-text-field
                            v-model="firstname"
                            :rules="nameRules"
                            :counter="10"
                            label="Nombre"
                            required
                        ></v-text-field>
                    </v-col>
        
                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-text-field
                            v-model="lastname"
                            :rules="nameRules"
                            :counter="10"
                            label="Apellido"
                            required
                        ></v-text-field>
                    </v-col>
        
                    <v-col
                        cols="12"
                        md="4"
                    >
                        <v-text-field
                            v-model="email"
                            :rules="emailRules"
                            label="E-mail"
                            required
                        ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        md="12"
                    >
                        <v-textarea
                            v-model="comment"
                            :rules="commentRules"
                            label="Comentarios"
                            required
                        ></v-textarea>
                    </v-col>
                    <v-btn 
                      block 
                      color="secondary" 
                      dark 
                      type="submit" 
                      value="Send">Enviar</v-btn>
                </v-row>
            </v-container>
        </v-form>
  </v-content>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    firstname: '',
    lastname: '',
    nameRules: [
      v => !!v || 'Nombre y apellido requerido',
      v => v.length <= 15 || 'El nombre o apellido debe tener menos de 15 caracteres',
    ],
    email: '',
    emailRules: [
      v => !!v || 'E-mail es requerido',
      v => /.+@.+/.test(v) || 'El E-mail no es valido',
    ],
    comment: '',
    commentRules: [
      v => !!v || 'Debe ingresar un comentario, pregunta o problema',
      v => v.length <= 100 || 'Escriba al menos 100 caracteres',
    ],
  }),
}
</script>