<template>
  <div @wheel.prevent="slide">
    <Index_index></Index_index>
    <Index_concept></Index_concept>
    <Index_team></Index_team>
    <Index_enterprise></Index_enterprise>
    <Index_news></Index_news>
    <Index_contact></Index_contact>
    <Index_affix></Index_affix>
    <router-view/>
  </div>
</template>

<script>
import Index_index from "@/components/index/Index_index";
import Index_concept from "@/components/index/Index_concept";
import Index_team from "@/components/index/Index_team";
import Index_enterprise from "@/components/index/Index_enterprise";
import Index_news from "@/components/index/Index_news";
import Index_contact from "@/components/index/Index_contact";
import router from "@/router";
import {reactive, onMounted} from 'vue'
import Index_affix from "@/components/index/Index_affix";
export default {
  name: 'Index',
  components: {
    Index_contact,
    Index_enterprise,
    Index_team,
    Index_concept,
    Index_index,
    Index_news,
    Index_affix,
  },

  setup() {
    let time = reactive({
      prev: Date.now(),
      now: Date.now(),
      delay: 1000,
    })
    const slide = () => {
      time.now = Date.now()
      if (time.now - time.prev > time.delay) {
        if (window.event.deltaY > 0) {
          document.documentElement.scrollBy({
            top: window.innerHeight,
            behavior: "smooth",
          })
        } else {
          document.documentElement.scrollBy({
            top: -window.innerHeight,
            behavior: "smooth",
          })
        }
        time.prev = Date.now()
      }
    }
    onMounted(() => {
    })
    return {slide}
  }
}
</script>
<style>
::-webkit-scrollbar {
  display: none
}
</style>

