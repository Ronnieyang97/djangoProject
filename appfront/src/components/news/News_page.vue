<template>
  <br/>
  <p style="font-size: 4.5vh;color: black;letter-spacing: 0.5vw;font-weight: bold">公司新闻</p>
  <p style="color: black">——</p>
  <div v-for="(item, index) in news.items" :key="index">
    <a-row>
      <a-col :span="2"></a-col>
      <a-col :span="5" style="border-width: thin;border-bottom-style: solid;border-top-style: solid;">
        <div class="news_date_icon">
          <div class="news_date">
            <p>{{ item.date.substring(0, 4) }}</p>
            <p>{{ item.date.substring(5, 7) }} | {{ item.date.substring(8) }}</p>
          </div>
        </div>
      </a-col>
      <a-col :span="15" @click="showmodal(index)">
        <div class="news_brief">
          <p style="color: black;font-weight: bold;font-size: 3vh">{{ item.title }}</p>
          <p style="color: grey;text-align: left">{{ item.summary }}</p>
        </div>
      </a-col>
    </a-row>
  </div>
  <a-modal v-model:visible="modal.visible"
           :centered="true" :footer="null" :width="'100%'"
           :bodyStyle="{'padding-bottom': 0} " :destroyOnClose="true">
    <div class="news_detail">
      <p style="color: blue; font-size: 4vh;margin-bottom: 2vh">{{ modal.title }}</p>
      <p style="color: blue;margin-bottom: 1vh">{{ modal.date }}</p>
      <p style="color: blue">——</p>
      <p style="height: 50vh;max-height: 50vh;margin-bottom:0;overflow-x: hidden;white-space: pre-line">
        {{ modal.introduction }}</p>
    </div>
    <a-row style="padding-bottom: 4vh">
      <a-col :span="9"></a-col>
      <a-col :span="2">
        <LeftCircleTwoTone v-on:click="previous_news(modal.index)" :style="{fontSize: '8vh'} "/>
      </a-col>
      <a-col :span="2">
        <CloseCircleTwoTone v-on:click="close" :style="{fontSize: '8vh'}"/>
      </a-col>
      <a-col :span="2">
        <RightCircleTwoTone v-on:click="next_news(modal.index)" :style="{fontSize: '8vh'}"/>
      </a-col>
    </a-row>
  </a-modal>
</template>

<script>
import axios from 'axios'
import {reactive, onMounted} from 'vue'
import {LeftCircleTwoTone, RightCircleTwoTone, CloseCircleTwoTone} from "@ant-design/icons-vue/"

export default {
  name: 'News_page',
  components: {
    LeftCircleTwoTone, RightCircleTwoTone, CloseCircleTwoTone
  },
  setup() {
    const news = reactive({
      items: [],
    })
    const modal = reactive({
      title: '',
      date: '',
      summary: '',
      introduction: '',
      visible: false,
      index: 0,
    })
    const showmodal = (index) => {
      modal.visible = true
      modal.title = news.items[index].title
      modal.date = news.items[index].date
      modal.summary = news.items[index].summary
      modal.introduction = news.items[index].introduction
      modal.index = index
    }
    const previous_news = (index) => {
      if (index > 0) {
        close
        showmodal(index - 1)
      }
    }
    const next_news = (index) => {
      if (index < news.items.length) {
        close
        showmodal(index + 1)
      }
    }
    const close = () => {
      modal.visible = false
    }
    onMounted(axios.get('http://127.0.0.1:8000/api/news')
        .then((res) => {
          for (let i = 0; i < res.data.length; i++) {
              news.items.push(res.data[i])
          }
          news.items.sort((a, b) => {
            return a['id'] - b['id']
          })
        }))
    return {news, modal, showmodal, close, previous_news, next_news}
  }
}
</script>
<style>
.news_date_icon {
  height: 180px;
  width: 180px;
  background-image: url("../../assets/image/news_icon.png");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 100% 100%;
  margin: 3vh calc((20.83vw - 180px) / 2);
}

.news_date p {
  font-size: 4vh;
  margin-bottom: 1vh;
}

.news_date {
  padding-top: 6vh;
}

.news_brief {
  padding-top: 6vh;
  margin: 0 2vw;
}

.news_detail p {
  color: black;
}

.news_detail {
  margin: 0 5vw;
  padding-top: 6vh;
  height: 100%;
  padding-bottom: 6vh;
}

.news_detail_icon {
  height: 5vh;
  width: 5vh;
}
</style>