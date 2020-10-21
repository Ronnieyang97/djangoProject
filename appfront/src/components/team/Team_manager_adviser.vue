<template>
  <div style="margin: 4vh 10vw; width: 80vw; ">
    <h1 style="font-weight: bolder">管理团队</h1>
    <pre class="detail_page">我们特别重视企业的管理团队。SIG自身的企业文化即以激发员工的创造力，鼓励员工挑战自身极限，将员工成长融入企业成长而著称。因此在投资对象中，我们同样期望有创造力，理解快速发展的中国经济，兼备战略眼光和执行力的创业团队。</pre>
  </div>
  <Team_manager_adviser_bar></Team_manager_adviser_bar>
  <router-view></router-view>

</template>

<script>
import Team_manager_adviser_bar from "@/components/team/Team_manager_adviser_bar";
export default {
  name: 'Team_manager_adviser',
  components: {Team_manager_adviser_bar,}
}

</script>

<style>
.detail_page {
  color: black;
  white-space: pre-wrap;
  margin: 5vh 10vh;
  font-size: 2vh;

}
</style>