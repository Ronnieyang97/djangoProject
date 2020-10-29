<template>
  <div class="backgroud_index_team">
    <div style="padding-top: 26.4vh">
      <p class="index_team_title">我们的团队</p>
      <p>————</p>
      <p style="font-size: 3.5vh;">我们是同行者 分享暗淡与荣光</p>
      <p>SIG企业文化的核心，是激发员工的创造力，鼓励员工挑战自身极限。</p>
      <p>在投资对象中，我们同样看中有创造力、理解快速发展的中国经济、兼备战略眼光和执行力的创业团队。</p>
    </div>
    <div style="margin-top: 8vh">
      <a-button type="ghost">
        <router-link :to="'/team'">查看更多团队成员</router-link>
      </a-button>
    </div>
    <div class="index_down_button">
      <a-button type="ghost" shape="circle-outline" size="large" @click="next_page">
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
  name: 'Index_team',
  components: {
    DownOutlined,
  },
  setup() {
    const next_page = () => {   //跳转下一页
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
.backgroud_index_team {
  background-image: url("../../assets/background/index_team.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}

.index_team_title {
  font-size: 5vh;
  margin-bottom: 0.5vh;
}

.index_team_down {
  height: 8vh;
  padding-top: 12vh;
}
</style>