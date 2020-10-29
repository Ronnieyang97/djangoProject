<template>
  <a-menu mode="horizontal" class="header-bar">
    <a-menu-item style="line-height:8vh;width: 12vw;padding: 0">
      <router-link :to="'/index_index'">
        <img src="../assets/logo.png">
      </router-link>
    </a-menu-item>
    <a-menu-item v-for="(item, index) in routers" :key="index" class="item">
      <router-link :to="item.url" @click.passive="backtotop">{{ item.title }}</router-link>
    </a-menu-item>
    <a-menu-item style="line-height:8vh;width: 6vw;padding: 0">
      <router-link :to="'/search'">
        <SearchOutlined :style="{fontSize: '3vh'}"/>
      </router-link>
    </a-menu-item>
  </a-menu>
  <router-view></router-view>
</template>


<script>
import {reactive} from 'vue'
import {SearchOutlined} from '@ant-design/icons-vue'
export default {
  name: 'Header',
  components: {
    SearchOutlined,
  },
  setup() {
    const routers = reactive([
      {url: '/index_index', title: '首页'},
      {url: '/concept', title: '投资理念'},
      {url: '/team', title: '投资团队'},
      {url: '/enterprise', title: '被投企业'},
      {url: '/news', title: '公司新闻'},
      {url: '/contact', title: '联系我们'},
    ])
    const backtotop = () => {
      document.documentElement.scrollTo(0, 0)
    }
    return {routers, backtotop}
  }
}
</script>

<style>
.item {
  width: 12vw;
  line-height: 8vh;
}

.header-bar {
  font-weight: bold;
  height: 8vh;
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 999;
}

.header-bar img {
  width: 12vw;
}

.ant-menu-inline > .ant-menu-item img {
  width: 12vw !important;
}
</style>
