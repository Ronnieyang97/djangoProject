<template>
  <div class="hello">
    <h1 v-show=state.show1>{{ msg }}</h1>
    <button v-on:click="clickHand">{{ state.msg1 }}</button>


  </div>
</template>

<script>
import {reactive} from "vue";


export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
  setup(){
    const state = reactive({
      msg1: 1,
      show1: true
    })
    const clickHand = () => {
      state.show1 = !state.show1
    }
    return {state, clickHand}
  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
