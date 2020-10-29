<template>
  <div class="backgroud_index_contact">
    <div class="index_contact_text">
      <p style="font-size: 3vh;font-weight: bolder">联系我们</p>
      <p>上海地址</p>
      <p>上海市黄浦区湖滨路222号企业天地1705-09室</p>
      <p>邮编200021，电话 （+86）21-61222888</p>
      <p>传真（+86）21-61130320</p>
      <p>邮箱：ChinaPIM@sig.com</p>
    </div>
    <div style="height: 23vh;">
      <a-carousel autoplay :slides-to-show="6" :dots="false"
                  style="padding-top: 2vh;">
        <div v-for="(item, index) in logo.items" :key="index">
          <img :src="item">
        </div>
      </a-carousel>
    </div>
  </div>
  <Footer></Footer>
</template>

<script>
import Footer from '../Footer'
import {reactive, onMounted} from 'vue'

export default {
  name: 'Index_contact',
  components: {
    Footer
  },
  setup() {
    const logo = reactive({
      items: [],
      test: ["../../assets/logo/logo1.png", "../../assets/logo/logo4.png",
        "../../assets/logo/logo2.png", "../../assets/logo/logo5.png",
        "../../assets/logo/logo3.png", "../../assets/logo/logo6.png",],
    })
    onMounted(() => {
      const files = require.context('../../assets/logo').keys()
      for (let item of files) {
        logo.items.push(require('../../assets/logo' + item.substring(1)))
      }
    })
    return {logo,}
  }
}

</script>
<style scoped>
/*有跑马灯组件需要使用scoped-*/
.backgroud_index_contact {
  background-image: url("../../assets/background/index_contact.jpg");
  height: 80vh;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 0;
  padding: 0 5vw;
}

.index_contact_text {
  text-align: left;
  padding-top: 20vh;
  padding-left: 5vw;
}

.ant-carousel ::v-deep(.slick-slide) {
  text-align: center;
  height: 20vh;
  line-height: 20vh;
  overflow: hidden;
}

.ant-carousel ::v-deep(.slick-slide img) {
  width: auto;
  height: auto;
  max-width: 15vw;
}
</style>