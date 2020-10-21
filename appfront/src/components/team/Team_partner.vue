<template>
  <a-row type="flex" justify="center" v-if="employee.investment_partner[0]">
    <a-col :span="5" style="height:auto;margin: 0.5vh 0.1vh;width: 20.8vw">
      <a-row class="team_employee">
        <img :src="employee.investment_partner[0].picture" @click="showmodal(0)">
      </a-row>
      <a-row class="team_employee">
        <img :src="employee.investment_partner[2].picture" @click="showmodal(2)">
      </a-row>
    </a-col>
    <a-col :span="10" style="background-color: #3047d3;margin: 0.5vh 0.1vh;width: 41.7vw;
    position: relative">
      <div style="margin: 0 6vw; text-align: left;position: absolute;top: 50%;
      -webkit-transform:translateY(-50%);transform:translateY(-50%);">
        <p style="font-size: 3vh">
          管理团队
        </p>
        <p>
          我们特别重视企业的管理团队。SIG自身的企业文化即以激发员工的创造力，鼓励员工挑战自身极限，将员工成长融入企业成长而著称。因此在投资对象中，我们同样期望有创造力，理解快速发展的中国经济，兼备战略眼光和执行力的创业团队。
        </p>
      </div>
    </a-col>
    <a-col :span="5" style="margin: 0.5vh 0.1vh;width: 20.8vw">
      <a-row class="team_employee">
        <img :src="employee.investment_partner[1].picture" @click="showmodal(1)">
      </a-row>
      <a-row class="team_employee">
        <img :src="employee.investment_partner[3].picture" @click="showmodal(3)">
      </a-row>
    </a-col>
  </a-row>
  <a-row type="flex" justify="center">
    <a-col v-for="(item, index) in employee.investment_partner.slice(4,)"
           class="team_employee" :key="index">
      <img :src="item.picture" @click="showmodal(index+4)">
    </a-col>
  </a-row>

  <a-modal v-model:visible="modal.visible" @click="close" width="80vw"
           :centered="true" :footer="null" :closable="false">
    <div style="text-align: center">
      <p class="deta；lil_title">{{ modal.name }}</p>
      <img src="../../assets/image/line.png" style="vertical-align: center">
      <pre class="detail_page">{{ modal.introduction }}</pre>
    </div>
  </a-modal>

</template>

<script>
import {onMounted, reactive} from 'vue'
import axios from "axios";

export default {
  name: 'Team_partner',
  setup() {
    let employee = reactive({
      investment_partner: [],
    })
    let modal = reactive({
          visible: false,
          name: '',
          introduction: '',
        }
    )
    const showmodal = (index) => {
      modal.visible = true;
      modal.name = employee.investment_partner[index].name
      modal.introduction = employee.investment_partner[index].introduction
    }
    const close = (e) => {
      console.log(e)
      modal.visible = false
    }

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/employee/partner')
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
              if (res.data[i].available){
                employee.investment_partner.push(res.data[i])}
            }
            employee.investment_partner.sort((a, b) => {
              return a['id'] - b['id']
            })
            for (let i = 0; i < employee.investment_partner.length; i++) {
              employee.investment_partner[i]['picture'] = 'http://localhost:8000' + employee.investment_partner[i]['picture']
            }
          })
    })

    return {employee, modal, showmodal, close}
  }
}
</script>

<style scoped>
.team_employee {
  width: 20.8vw;
  height: auto;
  align-items: center;
  justify-content: center;
}

img {
  width: auto;
  height: auto;
  max-width: 20.8vw;

}

.detail_page {
  color: black;
  white-space: pre-wrap;
  margin: 5vh 10vh;
  font-size: 2.5vh;
  text-align: left;
}

.detail_title {
  margin-top: 2vh;
  color: black;
  font-size: 5vh;
  text-align: center;
}
</style>