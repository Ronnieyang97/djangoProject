<template>
  <a-input-search
      v-model:value="value.item"
      :placeholder="'input search text'"
      enter-button
      @search="search"
      size="large"
      style="padding-top: 15vh; width: 80vw;line-height: 5vh"
  />

</template>
<script>
import axios from 'axios'
import {reactive,} from 'vue'

export default {
  name: 'Search',
  setup() {
    const value = reactive({
      item: '',
    })
    const result = reactive({
      enterprise: [],
      news: [],
    })
    const test = () => {
      console.log('test')
    }
    const search = () => {
      let params = new URLSearchParams()
      params.append("value", value.item)
      axios.post('http://127.0.0.1:8000/api/search/', params)
      .then((res) => {
        result.enterprise = res.data[0]
        result.news = res.data[1]
      })
    }

    return {test, value, search, result}
  }
}
</script>
<style>

</style>