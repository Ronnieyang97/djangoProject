<template>
  <div class="background_team">
    <div class="team_index_text">
      <p style="font-size: 3.5vh;margin-bottom: 1vh">我们投资的企业</p>
      <p style="font-size: 4.6vh; margin-bottom: 5vh;">有勇气试错 有勇气面对失败</p>
      <p>十余年来，海纳亚洲已经凝聚了超过260家被投企业，并且陪伴被投企业共同经历了完整的经济和投资周期，</p>
      <p>这使得我们在行业的广度、洞见的深度上积累了经验。</p>
      <p>创业，失败必然，成功偶然。因此，我们寻找的人，有勇气试错，有勇气面对失败。</p>
      <p>我们寻找的人，见解独立，与众不同。 我们寻找的人，感念际遇，不生苦毒，尊重对手，战胜自己。</p>
      <p>我们首先成为这样的人，我们就将找到这样的人。</p>
      <p>我们尊重成功者，也尊重失败者；在我们的版图上，只有强者。无论是洼地的雏凤，还是登顶的雄鹰，</p>
      <p>我们相信，不忘初心，终得始终。一路之上，我们是同行者，分享暗淡与荣光; </p>
      <p>浮华之后，我们见证周期，更信仰人的可能性。</p>
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
  name: "Enterprise_index",
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
  padding-top: 22vh;
  text-align: left;
  margin-left: 13vh;
}

.background_team {
  background-image: url("../../assets/background/enterprise_index.jpg");
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