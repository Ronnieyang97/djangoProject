<template>
  <div class="background_team">
    <div class="team_index_text">
      <p style="font-size: 3.5vh">我们的团队</p>
      <p style="font-size: 4.6vh; margin-bottom: 0;">我们是同行者</p>
      <p style="font-size: 4.6vh">分享暗淡与荣光</p>
      <p style="margin-bottom: 0">SIG企业文化的核心，是激发员工的创造力，鼓励员工挑战自身极限。</p>
      <p>在投资对象中，我们同样看中有创造力、理解快速发展的中国经济、兼备战略眼光和执行力的创业团队。</p>
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
  name: "Team_index",
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

<style>
.team_index_text {
  padding-top: 30vh;
  text-align: left;
  margin-left: 13vh;
}

.background_team {
  background-image: url("../../assets/background/index_team.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}


</style>