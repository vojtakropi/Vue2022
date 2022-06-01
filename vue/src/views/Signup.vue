<template>
<div class="context">
<h2>Registrace</h2>

<form>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input v-model="uname" placeholder="Zadej username" id="uname" required>

    <label for="psw"><b>Heslo</b></label>
    <input v-model="psw" placeholder="Zadej heslo" id="psw" required>
        
    <button @click="send">Registrovat</button>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <router-link class="register" :to="{name: 'login'}">Přihlaš se</router-link>
  </div>
</form>
</div>
</template>
<script>
import axios from 'axios'
    export default {
        data() {
            return {
              psw  : '',
              uname : '',
              dataset : ''
            };
        },
        methods:{
            send(){
                axios
              .put('http://localhost:8000/users/put?username='+this.uname+'&passwd=' + this.psw)
              .then((response) => {
                this.dataset = response.data
              })
                this.$store.commit("increment");
                this.$router.push("home"); 
            }
        }
    };
</script>

<style>

body {font-family: Arial, Helvetica, sans-serif;}
form {border: 3px solid #f1f1f1;}

.context{
    justify-content: center;
}

input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

h2{
    color: #aa0404;
    text-align: center;

}

button {
  background-color: #04AA6D;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
}

button:hover {
  opacity: 0.8;
}

.register {
  width: auto;
  padding: 10px 18px;
  background-color: #f44336;
}

.container {
  padding: 16px;
}

span.psw {
  float: right;
  padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
     display: block;
     float: none;
  }
  .register {
     width: 100%;
  }
}
</style>