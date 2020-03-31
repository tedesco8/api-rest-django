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
        <v-form ref="form" v-model="valid" >
            <v-container>
                <v-row>
                    <v-col
                        cols="12"
                        md="6"
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
                        md="6"
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
                        md="6"
                    >
                        <v-text-field
                            v-model="subject"
                            :rules="nameRules"
                            :counter="10"
                            label="Asunto"
                            required
                        ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                        md="6"
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
                      :disabled="!valid"
                      @click="sendEmail">Enviar</v-btn>
                </v-row>
            </v-container>
        </v-form>
  </v-content>
</template>
<script>
import swal from 'sweetalert';
import emailjs from 'emailjs-com';

(function(){
    emailjs.init(process.env.VUE_APP_MY_ENV_VARIABLE);
})();

export default {
  data: () => ({
    valid: false,
    firstname: '',
    lastname: '',
    subject: '',
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
  methods: {
    /* eslint-disable no-debugger */
      sendEmail() {
        var data 	= {
          from_name: this.firstname + this.lastname,
          from_email: this.email,
          message: this.comment,
          subject: this.subject
        }
        emailjs.send('gmail', 'nmcu', data)
        .then(() => {
          swal({
            title: "Buen trabajo!",
            text: "Usuario editado exitosamente",
            icon: "success"
          });
        }).catch( () => {
          swal({
            title: "Lo siento",
            text: "Ocurrio un problema con el servidor",
            icon: "error"
          });
        })
      }
      /* eslint-enable no-debugger */
  }
}
</script>