<template>
  <table class="styled-table">
    <thead>
        <tr>
            <th>Jméno</th>
            <th>čas</th>
            <th>Obtížnost</th>
        </tr>
    </thead>
    <tbody>
      <score
      v-for="people in dataset"
      :key="people"
      :time = people
      />
    </tbody>
</table>
</template>

<script>
import Score from "../components/Score.vue"
import axios from 'axios'
export default {
    components:{
      Score
    },
    data(){
      return{
          dataset : ''
      }
    },
    methods:{
     
    }, mounted(){
        axios
        .get('http://localhost:8000/users/get')
        .then((response) => {
          console.log(response.data)
          this.dataset = response.data
        })
        .catch((error) => {
          console.log(error)
        })
      }
}
</script>

<style>
.styled-table {
    border-collapse: collapse;
    margin: 25px 0;
    font-size: 0.9em;
    font-family: sans-serif;
    min-width: 400px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);
    margin-left: auto;
    margin-right: auto;;
}

.styled-table thead tr {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
}
.styled-table th,
.styled-table td {
    padding: 12px 15px;
}
.styled-table tbody tr {
    border-bottom: 1px solid #dddddd;
}

.styled-table tbody tr:nth-of-type(even) {
    background-color: #f3f3f3;
}

.styled-table tbody tr:last-of-type {
    border-bottom: 2px solid #009879;
}
.styled-table tbody tr.active-row {
    font-weight: bold;
    color: #009879;
}
</style>