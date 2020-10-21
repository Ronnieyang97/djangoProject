<template>
  <a-row type="flex" justify="center" v-if="employee.operation[0]">
    <a-col class="team_employee" v-for="(item, index) in employee.operation"
           v-on:mouseover="employee.operation[index].active = true"
           v-on:mouseleave="employee.operation[index].active = false"
           :key="index">
      <img :src="item.picture" class="image">
      <div class="team_employee_name" v-if="employee.operation[index].active">
        <h1>{{ employee.operation[index].name }}</h1>
      </div>

    </a-col>
  </a-row>
</template>

<script>
import axios from "axios";
import {reactive, onMounted} from 'vue'
export default {
  name: 'Team_operation',
    setup() {
    let employee = reactive({
      operation: [],
    })

    onMounted(() => {
      axios.get('http://127.0.0.1:8000/api/employee/operation')
          .then((res) => {
            for (let i = 0; i < res.data.length; i++) {
              if (res.data[i].available){
                employee.operation.push(res.data[i])}

            }
            employee.operation.sort((a, b) => {
              return a['id'] - b['id']
            })
            for (let i = 0; i < employee.operation.length; i++) {
              employee.operation[i]['picture'] = 'http://localhost:8000' + employee.operation[i]['picture']
              employee.operation[i].active = false
            }
          })
    })

    return {employee}
  }
}
</script>

<style>

</style>