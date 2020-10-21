<template>
  <div class="background_team">
    <div class="team_index_text">
      <p style="font-size: 3.5vh;margin-bottom: 3vh">我们的优势</p>
      <p style="font-size: 4.6vh;">感念际遇 不生苦毒</p>
      <p style="font-size: 4.6vh; margin-bottom: 5vh;">尊重对手 战胜自己</p>
      <p>十余年来，海纳亚洲主要聚焦投资科技、传媒、消费品、现代服务、医疗、环保等领域。</p>

      <div class="index_down">
        <a-button v-on:click="next_page" type="ghost" shape="circle-outline" size="large">
          <template v-slot:icon>
            <DownOutlined>
            </DownOutlined>
          </template>
        </a-button>
      </div>
    </div>
  </div>
</template>

<script>
import {DownOutlined} from '@ant-design/icons-vue'

export default {
  name: "News_index",
  components: {
    DownOutlined,
  },
  setup() {
    const next_page = () => {
      document.documentElement.scrollBy({
        top: window.innerHeight * 92 / 100,
        behavior: "smooth",
      })
    }
    return {next_page}
  }
}
</script>

<style scoped>
.team_index_text {
  padding-top: 28vh;
  text-align: left;
  margin-left: 13vh;
}

.background_team {
  background-image: url("../../assets/background/index_news.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}
p{
  font-size: 2.2vh;
  margin: 1vh;
}

</style>