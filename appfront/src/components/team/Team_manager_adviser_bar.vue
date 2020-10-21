<template>
  <a-row type="flex" justify="center" style="height: 5vh">
    <a-col :span="10" class="team_index_bar_item">
      <router-link to="/team/manager_adviser/manager">
        <div class="bar_item" tabindex="1">投资经理</div>
      </router-link>
    </a-col>
    <a-col :span="10" class="team_index_bar_item">
      <router-link to="/team/manager_adviser/adviser">
        <div class="bar_item" tabindex="2">投资顾问</div>
      </router-link>
    </a-col>
  </a-row>
</template>
<script>
export default {
  name: 'Team_manager_adviser_bar'
}
</script>
<style>

</style>