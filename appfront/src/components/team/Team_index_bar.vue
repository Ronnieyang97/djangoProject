<template>
  <a-row type="flex" justify="center" style="height: 5vh">
    <a-col :span="5" class="team_index_bar_item" v-for="(item, index) in routers" :key="index">
      <router-link :to="item.url">
        <div class="bar_item" :tabindex="index">{{ item.title }}</div>
      </router-link>
    </a-col>
  </a-row>


</template>

<script>
import {reactive} from 'vue'

export default {
  name: 'Team_index_bar',
  setup() {
    const routers = reactive([
      {url: '/team/partner', title: '投资合伙人'},
      {url: '/team/global', title: '全球团队'},
      {url: '/team/manager_adviser', title: '投资经理及顾问'},
      {url: '/team/post_investment_operation', title: '投后及运营团队'}
    ])

    return {routers}

  }
}
</script>

<style>
.team_index_bar_item {
  width: 20.8vw;
  background: grey;
  margin: 0 0.1vh;
  line-height: 5vh;
}

.bar_item {
  color: white;
}

.bar_item:focus {
  background-color: #2f54eb;
}

</style>