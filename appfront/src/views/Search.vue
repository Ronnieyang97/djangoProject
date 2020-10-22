<template>
  <a-input-search
      v-model:value="value.item"
      :placeholder="'input search text'"
      enter-button
      @search="search"
      size="large"
      style="padding-top: 15vh; width: 80vw;line-height: 5vh"
      pressEnter = "search"
  />
  <div v-if="value.visible" class="result_page">
    <p style="font-size: 1vh">找到{{ result.enterprise.length + result.news.length }}个有关"{{ value.item }}"的结果</p>
    <p style="margin-bottom: 0.5vh;background: #7c7cff;color: white;text-align: center">被投企业</p>
    <div v-if="result.enterprise.length > 0">
      <div style="border-bottom-style: solid; border-color: #cacaca; border-width: 1px"
           v-for="(item, index) in result.enterprise" :key="index" @click="showmodal(index, 'enterprise')">
        <p style="text-indent: 1em;font-size: 2.5vh;margin-bottom: 0.5vh">{{ item.name }}</p>
        <p style="font-size: 1.8vh;overflow: hidden;width: 84vw; white-space: nowrap; text-overflow: ellipsis;">
          {{ item.introduction }}</p>
      </div>
    </div>
    <div v-else>
      <p>无"{{ value.item }}"的相关被投企业结果</p>
    </div>
    <p style="margin-bottom: 0.5vh;background: #7c7cff;color: white;text-align: center">公司新闻</p>
    <div v-if="result.news.length > 0">
      <div style="border-bottom-style: solid; border-color: #cacaca; border-width: 1px"
           v-for="(item, index) in result.news" :key="index" @click="showmodal(index, 'news')">
        <p style="text-indent: 1em;font-size: 2.5vh;margin-bottom: 0.5vh">{{ item.title }}</p>
        <p style="font-size: 1.8vh;overflow: hidden;width: 84vw; white-space: nowrap; text-overflow: ellipsis;">
          {{ item.summary }}</p>
      </div>
    </div>
    <div v-else>
      <p>无"{{ value.item }}"的相关公司新闻结果</p>
    </div>
  </div>
  <a-modal v-model:visible="modal_entrprise.visible" @click="close"
           :centered="true" :footer="null" :closable="false" :width="'80vw'"
           :bodyStyle="{padding: 0,}" :destroyOnClose="true">
    <div v-if="modal_entrprise.picture_owner" class="enterpirse_item_detail">
      <a-row>
        <a-col :span="12" style="display: flex">
          <img :src="modal_entrprise.picture_owner">
          <div style="z-index: 2;position: absolute; padding:28vh 3vh">
            <p style="margin: 0; font-size: 4vh">{{ modal_entrprise.name }}</p>
            <p>——</p>
            <p style="font-size: 4vh">{{ modal_entrprise.owner }}</p>
            <a style="color: white;font-size: 2.5vh">{{ modal_entrprise.site }}</a>
          </div>
        </a-col>
        <a-col :span="12">
          <img :src="modal_entrprise.trademark"
               style="width:100%; height:100%;max-width: 30vw;padding-top: 4vh;margin-left: 5vw;filter: brightness(100%)">
          <p style="font-size: 5vh;font-weight: bolder;color: black;text-align: center;margin-bottom: 2vh">
            {{ modal_entrprise.name }}</p>
          <img src="../assets/image/line.png"
               style="width: 10vw;margin-left: 15vw;padding-bottom: 2vh;padding-top: 0">
          <p style="color: black; margin: 1vh 3vw">公司官网 <a>{{ modal_entrprise.site }}</a></p>
          <p style="color: black; margin: 1vh 3vw;max-height: 30vh;overflow-y: scroll;">{{
              modal_entrprise.introduction
            }}</p>
        </a-col>
      </a-row>
    </div>
    <div v-else>
      <img :src="modal_entrprise.trademark" style="width: 30vw;margin-left: 25vw;">
      <p style="color: black;text-align: center;font-size:6vh;font-weight: bolder;margin-bottom: 2vh">
        {{ modal_entrprise.name }}</p>
      <img src="../assets/image/line.png" style="width: 10vw;margin-left: 35vw">
      <p style="color: black;overflow-x: hidden;padding: 5vw">{{ modal_entrprise.introduction }}</p>
    </div>
  </a-modal>

  <a-modal v-model:visible="modal_news.visible"
           :centered="true" :footer="null" :width="'100%'"
           :bodyStyle="{'padding-bottom': 0} " :destroyOnClose="true">
    <div class="news_detail">
      <p style="color: blue; font-size: 4vh;margin-bottom: 2vh">{{ modal_news.title }}</p>
      <p style="color: blue;margin-bottom: 1vh">{{ modal_news.date }}</p>
      <p style="color: blue">——</p>
      <p style="height: 50vh;max-height: 50vh;margin-bottom:0;overflow-x: hidden;white-space: pre-line">
        {{ modal_news.introduction }}</p>
    </div>
  </a-modal>


</template>
<script>
import axios from 'axios'
import {reactive,} from 'vue'

export default {
  name: 'Search',
  setup() {
    const value = reactive({
      item: '',
      visible: false,
    })
    const result = reactive({
      enterprise: [],
      news: [],
    })
    const modal_entrprise = reactive({
      visible: false,
      name: '',
      site: '',
      owner: '',
      introduction: '',
      picture_owner: '',
      trademark: '',
    })
    const modal_news = reactive({
      visible: false,
      title: '',
      date: '',
      summary: '',
      introduction: '',
    })
    const close = (e) => {
      console.log(e)
      modal_news.visible = false
      modal_entrprise.visible = false
    }
    const showmodal = (index, category) => {
      if (category === 'enterprise') {
        modal_entrprise.visible = true
        modal_entrprise.name = result.enterprise[index]['name']
        modal_entrprise.site = result.enterprise[index]['site']
        modal_entrprise.owner = result.enterprise[index]['owner']
        modal_entrprise.introduction = result.enterprise[index]['introduction']
        modal_entrprise.picture_owner = result.enterprise[index]['picture_owner']
        modal_entrprise.trademark = result.enterprise[index]['trademark']
      } else if (category === 'news') {
        modal_news.visible = true
        modal_news.title = result.news[index].title
        modal_news.date = result.news[index].date
        modal_news.summary = result.news[index].summary
        modal_news.introduction = result.news[index].introduction
      }
    }
    const search = () => {
      if (value.item.length > 0) {
        value.visible = true
        let params = new URLSearchParams()
        params.append("value", value.item)
        axios.post('http://127.0.0.1:8000/api/search/', params)
            .then((res) => {
              result.enterprise = res.data[0]
              result.news = res.data[1]
              result.enterprise.sort((a, b) => {
                return a['id'] - b['id']
              })
              result.news.sort((a, b) => {
                return a['id'] - b['id']
              })
              for (let i = 0; i < result.enterprise.length; i++) {
                result.enterprise[i]["trademark"] = 'http://localhost:8000' + result.enterprise[i]["trademark"]
                if (result.enterprise[i]["picture_owner"]) {
                  result.enterprise[i]["picture_owner"] = 'http://localhost:8000' + result.enterprise[i]["picture_owner"]
                }
              }
            })
      }
    }

    return {value, search, result, modal_entrprise, modal_news, showmodal, close}
  }
}
</script>
<style>
.result_page {
  padding-top: 2vh;
  margin: 0 8vw;

}

.result_page p {
  color: #7a7a7a;
  text-align: left;
}
</style>