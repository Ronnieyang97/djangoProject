<template>
  <a-row type="flex" justify="center" v-if="employee.investment_manager[0]">
    <a-col class="team_employee" v-for="(item, index) in employee.investment_manager"
           v-on:mouseover="employee.investment_manager[index].active = true"
           v-on:mouseleave="employee.investment_manager[index].active = false"
           :key="index">
      <img :src="item.picture" class="image">
      <div class="team_employee_name" v-if="employee.investment_manager[index].active">
        <h1>{{ employee.investment_manager[index].name }}</h1>
      </div>

    </a-col>
  </a-row>
</template>
<script>

import axios from "axios";
import {reactive, onMounted} from 'vue'

export default {
  name: 'Team_manager',
  setup() {
    let employee = reactive({
      investment_manager: [],
    })

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/employee/manager')
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
                employee.investment_manager.push(res.data[i])
              }
              employee.investment_manager.sort((a, b) => {
                return a['id'] - b['id']
              })
              for (let i = 0; i < employee.investment_manager.length; i++) {
                employee.investment_manager[i]['picture'] = 'http://localhost:8000' + employee.investment_manager[i]['picture']
                employee.investment_manager[i].active = false
              }
            }
          )
    })

    return {employee}
  }
}
</script>
<style scoped>
.team_employee {
  width: auto;
  height: auto;
  align-items: center;
  justify-content: center;
  max-width: 20.8vw;
}

.image {
  width: 20.8vw;
  height: auto;
  max-width: 20.8vw;
}

.team_employee_name {
  z-index: 2;
  position: absolute;
  bottom: 3vh;
  left: 2vw;
}

.image:hover {
  opacity: 0.5;
}

</style>