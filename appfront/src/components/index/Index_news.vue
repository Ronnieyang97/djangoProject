<template>
  <div class="backgroud_index_news">
    <div style="padding-top: 24.4vh">
      <p class="index_news_title">我们的优势</p>
      <p style="padding-top: 1vh">———</p>
      <p style="font-size: 3.4vh">感念际遇 不生苦毒 尊重对手 战胜自己</p>
      <p style="font-size: 2.6vh">十余年来，海纳亚洲主要聚焦投资科技、传媒、消费品、现代服务、医疗、环保等领域。</p>
    </div>
    <div style="margin-top: 8vh" >
    <a-button type="ghost">
      <router-link :to="'/news'">查看更多公司新闻</router-link>
    </a-button>
      </div>
    <div class="index_news_down">
      <a-button v-on:click="next_page" type="ghost" shape="circle-outline" size="large">
        <template v-slot:icon>
          <DownOutlined/>
        </template>
      </a-button>
    </div>
  </div>
</template>

<script>
import {DownOutlined} from "@ant-design/icons-vue/";

export default {
  name: 'Index_news',
  components: {
    DownOutlined,
  },
  setup() {
    const next_page = () => {
      document.documentElement.scrollBy({
        top: window.innerHeight,
        behavior: "smooth",
      })
    }
    return {next_page}
  }
}

</script>
<style>
.backgroud_index_news {
  background-image: url("../../assets/background/index_news.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}

.index_news_title {
  font-size: 5vh;
  margin-bottom: 0.5vh;
}
.index_news_down {
  height: 8vh;
  padding-top: 16vh;
}


</style>