<template>
  <div id="container" style="height: 60vh;width: 83.33vw; margin-left: 8.33vw"></div>
</template>
<script>
import MapLoader from "../../utils/Amap";//引入刚刚新建的amap.js

export default {
  name: "Contact_page_map",
  data() {
    return {
      map: null
    }
  },
  mounted() {
    MapLoader().then(AMap => {
      console.log('地图加载成功')
      this.map = new AMap.Map('container', {
        center: [(116.39 + 121.482171 + 114.17077)/3 ,(39.9 + 31.224 + 22.270715)/3],
        zoom: 4,
        zoomEnable: false,
        dragEnable: false,
      })
      let beijing = new AMap.Marker({
            position: new AMap.LngLat(116.39, 39.9),
            title: '北京',
          })
      let shanghai = new AMap.Marker({
        position: new AMap.LngLat(121.482171,31.224),
        title: '上海',
      })
      let hongkong = new AMap.Marker({
        position: new AMap.LngLat(114.17077,22.270715),
        title: '香港',
      })
      let tokyo = new AMap.Marker({
        position: new AMap.LngLat(139.46, 35.42),
        title: '东京'
      })
      this.map.add([beijing, shanghai, hongkong,tokyo])
    }, e => {
      console.log('地图加载失败', e)
    })
  }
}
</script>
<style>

</style>