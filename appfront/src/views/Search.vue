<template>
  <a-input-search
      v-model:value="value.item"
      :placeholder="'input search text'"
      enter-button
      @search="test"
      size="large"
      style="padding-top: 15vh; width: 80vw;line-height: 5vh"
    />

</template>
<script>
import {reactive} from 'vue'
export default {
  name: 'Search',
  setup(){
    const value = reactive({
      item: '',
      category: 0,
    })
    const test = () => {
      console.log('test')
    }
    return {test, value}
  }

}
</script>
<style>

</style>