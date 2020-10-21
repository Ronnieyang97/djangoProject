<template>
  <a-row type="flex">
    <a-col :span="2"></a-col>
    <a-col :span="5" class="enterprise_page_title">被投企业</a-col>
    <a-col :span="17"></a-col>
  </a-row>
  <a-row type="flex" justify="center">
    <a-col v-for="(item, index) in enterprise.items" :key="index" class="enterprise_item" @click="showmodal(index)">
      <img :src="item.trademark">
      <p style="color: grey; margin-top: 3vh">{{ item.name }}</p>
    </a-col>
  </a-row>
  <a-modal v-model:visible="modal.visible" @click="close"
           :centered="true" :footer="null" :closable="false" :width="'80vw'"
           :bodyStyle="{padding: 0,}" :destroyOnClose="true">
    <div v-if="modal.picture_owner" class="enterpirse_item_detail">
      <a-row>
        <a-col :span="12" style="display: flex">
          <img :src="modal.picture_owner">
          <div style="z-index: 2;position: absolute; padding:28vh 3vh">
            <p style="margin: 0; font-size: 4vh">{{ modal.name }}</p>
            <p>——</p>
            <p style="font-size: 4vh">{{ modal.owner }}</p>
            <a style="color: white;font-size: 2.5vh">{{ modal.site }}</a>
          </div>
        </a-col>
        <a-col :span="12">
          <img :src="modal.trademark"
               style="width:100%; height:100%;max-width: 30vw;padding-top: 4vh;margin-left: 5vw;filter: brightness(100%)">
          <p style="font-size: 5vh;font-weight: bolder;color: black;text-align: center;margin-bottom: 2vh">
            {{ modal.name }}</p>
          <img src="../../assets/image/line.png"
               style="width: 10vw;margin-left: 15vw;padding-bottom: 2vh;padding-top: 0">
          <p style="color: black; margin: 1vh 3vw">公司官网 <a>{{ modal.site }}</a></p>
          <p style="color: black; margin: 1vh 3vw;max-height: 30vh;overflow-y: scroll;">{{ modal.introduction }}</p>
        </a-col>
      </a-row>
    </div>
    <div v-else>
      <img :src="modal.trademark" style="width: 30vw;margin-left: 25vw;">
      <p style="color: black;text-align: center;font-size:6vh;font-weight: bolder;margin-bottom: 2vh">{{modal.name}}</p>
      <img src="../../assets/image/line.png" style="width: 10vw;margin-left: 35vw">
      <p style="color: black;overflow-x: hidden;padding: 5vw">{{modal.introduction}}</p>
    </div>
  </a-modal>
</template>

<script>
import axios from 'axios'
import {reactive, onMounted} from 'vue'

export default {
  name: 'Enterprise_page',
  components: {},
  setup() {
    const enterprise = reactive({
      items: []
    })
    let modal = reactive({
      name: '',
      site: '',
      owner: '',
      introduction: '',
      picture_owner: '',
      trademark: '',
      visible: false,
    })
    const showmodal = (index) => {
      modal.name = enterprise.items[index]['name']
      modal.site = enterprise.items[index]['site']
      modal.owner = enterprise.items[index]['owner']
      modal.introduction = enterprise.items[index]['introduction']
      modal.picture_owner = enterprise.items[index]['picture_owner']
      modal.trademark = enterprise.items[index]['trademark']
      modal.visible = true
    }
    const close = (e) => {
      console.log(e)
      modal.visible = false
    }
    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/enterprise')
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
              if (res.data[i].available){
              enterprise.items.push(res.data[i])}
            }
            enterprise.items.sort((a, b) => {
                return a['id'] - b['id']
              })
            for (let i = 0; i < enterprise.items.length; i++) {
              enterprise.items[i]["trademark"] = 'http://localhost:8000' + enterprise.items[i]["trademark"]
              if (enterprise.items[i]["picture_owner"]) {
                enterprise.items[i]["picture_owner"] = 'http://localhost:8000' + enterprise.items[i]["picture_owner"]
              }
            }
          })
    })
    return {enterprise, modal, showmodal, close}
  },
}
</script>

<style>
.enterprise_item {
  border-style: solid;
  border-width: 1px;
  border-color: #f8f8f8;
  width: 20.8vw;
  height: 25vh;
}

.enterprise_item img {
  padding-top: 4vh;
  width: auto;
  height: auto;
  max-width: 16vw;
  -webkit-filter: grayscale(100%);
  -moz-filter: grayscale(100%);
  -ms-filter: grayscale(100%);
  -o-filter: grayscale(100%);
  filter: grayscale(100%);
  filter: gray;
}

.enterprise_item img:hover {
  -webkit-filter: inherit;
  -moz-filter: inherit;
  -ms-filter: inherit;
  -o-filter: inherit;
  filter: inherit;
  filter: inherit;
}

.enterprise_page_title{
    background: #2f54eb;
  color: white;
  font-size: 2.6vh;
  height: 5.4vh;
  text-align: left;
  line-height: 5.4vh;
  padding-left: 2vh;
  text-indent: 2em;
}
.enterpirse_item_detail {

}

.enterpirse_item_detail img {
  width: 100%;
  height: 100%;
  max-width: 40vw;
  filter: brightness(80%)
}
</style>