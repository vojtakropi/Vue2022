<template>
<div class="context">
<h2>Přihlášení</h2>

<form>

  <div class="container">
    <label for="uname"><b>Username</b></label>
    <input type="text" placeholder="Zadej username" name="uname" required>

    <label for="psw"><b>Heslo</b></label>
    <input type="password" placeholder="Zadej heslo" name="psw" required>
        
    <button @click="send">Přihlásit</button>
  </div>

  <div class="container" style="background-color:#f1f1f1">
    <router-link class="register" :to="{name: 'signup'}">Zaregistruj se</router-link>
  </div>
</form>
</div>
</template>
<script>
    export default {
        data() {
            return {};
        },
        methods:{
            send(){
              this.$store.commit("increment");
              console.log(this.$store.state.logedin);
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
    color: #04AA6D;
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