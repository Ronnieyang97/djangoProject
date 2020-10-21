<template>
<a-row type="flex" justify="center" v-if="employee.legal[0]">
    <a-col class="team_employee" v-for="(item, index) in employee.legal"
           v-on:mouseover="employee.legal[index].active = true"
           v-on:mouseleave="employee.legal[index].active = false"
           :key="index">
      <img :src="item.picture" class="image">
      <div class="team_employee_name" v-if="employee.legal[index].active">
        <h1>{{ employee.legal[index].name }}</h1>
      </div>
    </a-col>
  </a-row>
</template>

<script>
import axios from "axios";
import {reactive, onMounted} from 'vue'
export default {
  name: 'Team_legal',
      setup() {
    let employee = reactive({
      legal: [],
    })

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/employee/legal')
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
              if (res.data[i].available){
                employee.legal.push(res.data[i])}

            }
            employee.legal.sort((a, b) => {
              return a['id'] - b['id']
            })
            for (let i = 0; i < employee.legal.length; i++) {
              employee.legal[i]['picture'] = 'http://localhost:8000' + employee.legal[i]['picture']
              employee.legal[i].active = false
            }
          })
    })

    return {employee}
  }
}
</script>

<style>
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