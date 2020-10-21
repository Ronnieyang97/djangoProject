<template>
  <div class="index_enterprise_down">
    <a-button v-on:click="next_page" type="ghost" shape="circle-outline" size="large">
      <template v-slot:icon>
        <DownOutlined/>
      </template>
    </a-button>
  </div>
  <a-carousel autoplay :autoplaySpeed="2000" arrows style="height: 100vh;" :dots="false" effect="fade">
    <template v-slot:prevArrow>
      <div class="custom-slick-arrow" style="left: 10px;z-index: 1">
        <left-circle-outlined/>
      </div>
    </template>
    <template v-slot:nextArrow>
      <div class="custom-slick-arrow" style="right: 10px">
        <right-circle-outlined/>
      </div>
    </template>
    <div v-for="(item, index) in enterprise.items" :key="index">
      <a-row>
        <a-col :span="12" style="height: 100vh">
          <div class="index_enterprise_introduction">
            <div style="padding-top: 20vh;padding-left: 10vw;padding-right: 5vw">
              <p style="font-size: 5vh;margin-bottom: 1vh">被投企业</p>
              <p>————</p>
              <p style="font-size: 4vh;margin-bottom: 2vh">{{ item.name }}</p>
              <p>{{ item.introduction }}</p>
            </div>
          </div>
        </a-col>
        <a-col :span="12" style="height: 100vh">
          <div class="index_enterprise_owner">
            <img :src="item.picture_owner">
            <div class="index_enterprise_owner_text">
              <p style="font-size: 4vh">{{ item.name }}</p>
              <p style="font-size: 3.5vh">{{ item.owner }}</p>
              <p>——</p>
              <a style="font-size: 2vh;color: white">{{ item.site }}</a>
              <br>
              <a-button type="ghost" style="margin-top: 10vh">
                <router-link :to="'/team'">查看更多团队成员</router-link>
              </a-button>
            </div>
          </div>
        </a-col>
      </a-row>
    </div>

  </a-carousel>
</template>

<script>
import {reactive, onMounted} from 'vue'
import axios from "axios";
import {DownOutlined, LeftCircleOutlined, RightCircleOutlined} from "@ant-design/icons-vue/";


export default {
  name: 'Index_enterprise',
  components: {DownOutlined, LeftCircleOutlined, RightCircleOutlined},
  setup() {
    const enterprise = reactive({
      items: []
    })
    const next_page = () => {
      document.documentElement.scrollBy({
        top: window.innerHeight,
        behavior: "smooth",
      })
    }

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/enterprise/index')
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
              enterprise.items.push(res.data[i])
            }
            for (let i = 0; i < enterprise.items.length; i++) {
              enterprise.items[i]["trademark"] = 'http://localhost:8000' + enterprise.items[i]["trademark"]
              enterprise.items[i]["picture_owner"] = 'http://localhost:8000' + enterprise.items[i]["picture_owner"]
            }
          })
    })
    return {enterprise, next_page,}

  }
}

</script>
<style scoped>
.ant-carousel ::v-deep(.slick-slide) {
  height: 100vh;
}

img {
  width: 100%;
  height: 100%;
  filter: brightness(80%);
}

.ant-carousel ::v-deep(.slick-slide .index_enterprise_introduction) {
  background-image: url("../../assets/background/index_enterprise.jpg");
  height: 100vh;
  background-repeat: no-repeat;
  background-size: 100% 100%;
}

.ant-carousel ::v-deep(.slick-slide .index_enterprise_owner) {
  width: 50vw;
  height: 100vh;
  display: flex;
}

.ant-carousel ::v-deep(.slick-slide .index_enterprise_owner_text) {
  position: absolute;
  z-index: 2;
  text-align: left;
  padding-top: 30vh;
  padding-left: 5vh;
}

.index_enterprise_down {
  height: 8vh;
  padding-top: 88vh;
  position: absolute;
  z-index: 2;
  padding-left: calc(50vw - 27px);
}


.ant-carousel ::v-deep(.slick-arrow.custom-slick-arrow) {
  width: 10vh;
  height: 10vh;
  font-size: 10vh;
  color: #fff;
  background-color: rgba(31, 45, 61, 0.11);
  opacity: 0.3;
  margin: 0 1vw;
}
.ant-carousel ::v-deep(.custom-slick-arrow:before) {
  display: none;
}
.ant-carousel ::v-deep(.custom-slick-arrow:hover) {
  opacity: 0.5;
}
</style>