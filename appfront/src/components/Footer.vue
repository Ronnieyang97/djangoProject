<template>
    <a-row class="foot">
      <a-col :span="5" style="height: 20vh;line-height: 20vh"><img src="../assets/footlogo.png"></a-col>
      <a-col :span="14"></a-col>
      <a-col :span="5"></a-col>
    </a-row>
</template>
<script>
export default {
  name: 'Footer'
}
</script>

<style>
.foot{
  background: black;
}
</style>