<template>
  <a-row type="flex" justify="center" style="height: 5vh">
    <a-col :span="7" class="team_index_bar_item">
      <router-link to="/team/post_investment_operation/post_investment">
        <div class="bar_item" tabindex="1">投后团队</div>
      </router-link>
    </a-col>
    <a-col :span="7" class="team_index_bar_item">
      <router-link to="/team/post_investment_operation/legal">
        <div class="bar_item" tabindex="2">法务团队</div>
      </router-link>
    </a-col>
    <a-col :span="6" class="team_index_bar_item">
      <router-link to="/team/post_investment_operation/operation">
        <div class="bar_item" tabindex="3">运营团队</div>
      </router-link>
    </a-col>
  </a-row>
</template>

<script>
export default {
  name: 'Team_post_investment_operation_bar',
}
</script>

<style>

</style>