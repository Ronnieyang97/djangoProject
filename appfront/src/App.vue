<template>
  <div id="app">
    <Header/>
    <!--<router-view v-if="judge.routeralive"></router-view>-->

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

</style>
