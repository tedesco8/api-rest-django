<template>
    <div class="row">
      <div class="col-12">
        <card :title="table1.title" :subTitle="table1.subTitle">
          <div slot="raw-content" class="table-responsive">
            <paper-table :data="table1.data" :columns="table1.columns">

            </paper-table>
          </div>
        </card>
      </div>

      <div class="col-12">
        <card class="card-plain">
          <div class="table-full-width table-responsive">
            <paper-table type="hover" :title="table2.title" :sub-title="table2.subTitle" :data="table2.data"
                         :columns="table2.columns">

            </paper-table>
          </div>
        </card>
      </div>

    </div>
</template>
<script>
import  axios from "axios";
import { PaperTable } from "@/components";
const tableColumns = ["Id", "Descripcion", "Fecha_creado", "Vendido", "Subcategoria"];
const tableData = [];

export default {
  components: {
    PaperTable
  },
  data() {
    return {
      table1: {
        title: "Stripped Table",
        subTitle: "Here is a subtitle for this table",
        columns: [...tableColumns],
        data: []
      },
      table2: {
        title: "Table on Plain Background",
        subTitle: "Here is a subtitle for this table",
        columns: [...tableColumns],
        data: []
      }
    };
  },
  methods: {
      getArticulos() {
          const path = 'http://localhost:8000/api/v1/productos'
          axios.get(path)
          .then( response => {
              this.table1.data = response.data
          })
          .catch(error => console.log(error))
      }
  },
  created(){
      this.getArticulos();
  }
};
</script>
<style>
</style>
