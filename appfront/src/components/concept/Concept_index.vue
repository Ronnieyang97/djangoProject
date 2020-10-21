<template>
  <div class="background_concept">
    <div class="concept_index_text">
      <p style="font-size: 3.5vh">我们的理念</p>
      <p style="font-size: 5vh;">寻找价值洼地 赋能新生力量</p>
      <p>我们无法预测哪里有价值洼地，但出现洼地的地方，我们会出现，这是勤奋，也是风格。</p>
      <p>是我们选择了快速生成的洼地，也是新崛起的力量选择了我们。</p>
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
  name: 'Concept_index',
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
.background_concept {
  background-image: url("../../assets/background/concept_index.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}

.concept_index_text {
  padding-top: 28.4vh;
  text-align: left;
  margin-left: 15vh;
}


</style>