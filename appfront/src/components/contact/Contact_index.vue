<template>
  <div class="contact_index">
    <div class="contact_index_text">
      <p style="font-size: 4vh;margin-bottom: 2vh">关于我们</p>
      <p style="font-size: 6vh;margin-bottom: 2vh">为资本寻路 为新生力量赋能</p>
      <p>SIG是总部设于美国的全球领先的量化交易金融公司，拥有独有的创新、严谨的交易理念和技术，</p>
      <p>是高性能、低延迟交易的全球领导者和创新者。</p>
    </div>
    <div class="index_down">
        <a-button v-on:click="next_page" type="ghost" shape="circle-outline" size="large">
          <template v-slot:icon>
            <DownOutlined>
            </DownOutlined>
          </template>
        </a-button>
      </div>
  </div>
</template>
<script>
import {DownOutlined} from '@ant-design/icons-vue'
export default {
  name: 'Contact_index',
  components: {DownOutlined,},
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
.contact_index {
  background-image: url("../../assets/background/contact_index.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
    text-align: left;
}

.contact_index_text {
  padding-top: 34vh;
  margin-left: 6vw;
}
.index_down{
  padding-left: 6vw;
}
</style>