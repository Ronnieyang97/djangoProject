<template>
  <div class="backgroud_index_concept">
    <div class="index_concept_text">
      <p class="index_concept_title">投资理念</p>
      <p style="padding-bottom: 1vh">——————</p>
      <p> 我们无法预测哪里有价值洼地，但出现洼地的地方，我们会出现，这是勤奋，也是风格。</p>
      <p>是我们选择了快速生成的洼地，也是新崛起的力量选择了我们。</p>
      <a-row class="index_concept_card">
        <a-col :span="8">
          <img src="../../assets/image/index_concept_card_1.png" class="card_img">
          <p style="padding-top: 1vh">———</p>
          <p class="card_title">早 | 直觉</p>
          <p class="card_text">浩茫广宇，于无声处听惊雷</p>
        </a-col>
        <a-col :span="8">
          <img src="../../assets/image/index_concept_card_2.png" class="card_img">
          <p style="padding-top: 1vh">———</p>
          <p class="card_title">快 | 决断</p>
          <p class="card_text">厚积薄发，当断之机则立断</p>
        </a-col>
        <a-col :span="8">
          <img src="../../assets/image/index_concept_card_3.png" class="card_img">
          <p style="padding-top: 1vh">———</p>
          <p class="card_title">远 | 眼界</p>
          <p class="card_text">除却浮云，风物长宜放眼量</p>
        </a-col>
      </a-row>
      <div class="index_down_button">
        <a-button type="ghost" shape="circle-outline" size="large" @click="next_page">
          <template v-slot:icon>
              <DownOutlined/>
          </template>
        </a-button>
      </div>
    </div>
  </div>
</template>
<script>
import {DownOutlined} from "@ant-design/icons-vue/"

export default {
  name: 'Index_concept',
  setup() {
    const next_page = () => {
      document.documentElement.scrollBy({
        top: window.innerHeight,
        behavior: "smooth",
      })
    }
    return {next_page}
  },
  components: {
    DownOutlined,
  }
}
</script>
<style>
.backgroud_index_concept {
  background-image: url("../../assets/background/index_concept.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}

.index_concept_text {
  padding-top: 18vh;
}

.index_concept_title {
  font-size: 5vh;
  margin-bottom: 0.5vh;
}

p {
  color: white;
  font-size: 2.3vh;
}

.index_concept_card {
  padding-top: 4vh;
  color: white;
}

.card_img {
  height: 10vh;
}

.card_title {
  font-size: 3vh;
}

.card_text {
  font-size: 2vh;
  color: rgba(255, 255, 255, 0.5);
}
</style>