<template>
  <div class="backgroud_index_index">
    <div class="index_text">
      <p style="font-size: 4vh;">14年+｜项目260+｜$20亿+｜退出60+</p>
      <p style="padding-bottom: 1vh">————————</p>
      <p>SIG是总部设于美国的全球领先的量化交易金融公司，拥有独有的创新、严谨的交易理念和技术，是高性能、低延迟交易的全球领导者和创新者。</p>
      <p>30年来，SIG在全球市场展开投资，尤其在金融衍生品的定价和交易方面享有国际声誉。公司全球员工超过1800人。</p>
      <p>SIG 2005年进入中国，以自有资金投资中国的创新公司。</p>
      <p>10余年来，聚焦中国互联网、消费等相关领域，已经投资了包括：</p>
      <p>乂学、最右、宝宝树、博纳影业、乡村基、康辉医疗、大麦网、Adsage、今日头条、喜马拉雅、出门问问、51信用卡、返利网、声网、</p>
      <p>闪银、一条、Musical.ly、闪送、伴鱼、威马汽车、云丁科技、善诊等在内的超过260家公司.</p>
      <p>总投资金额超过20亿美金，其中60多家公司已经通过上市或者并购实现退出。</p>
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
import router from "@/router";
import {onMounted, reactive} from 'vue'

export default {
  name: 'Index_index',
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
.backgroud_index_index {
  background-image: url("../../assets/background/index_index.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
}

p {
  color: white;
  font-size: 2.2vh;
}

.index_text {
  padding-top: 24.4vh;
  height: 92vh;
}

.index_down_button {
  height: 5vh;
  padding-top: 5vh;
}

</style>