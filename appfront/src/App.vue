<template>
  <div id="app">
    <Header/>
    <router-view/>
  </div>
</template>

<script>
import Header from './components/Header'

export default {
  name: 'app',
  components: {Header},
}
</script>

<style lang="scss">
#app {
  text-align: center;
  height: 100vh
}
p {
  color: white;
  font-size: 2.3vh;
}
</style>
