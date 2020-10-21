<template>
  <a-row type="flex">
    <a-col :span="2"></a-col>
    <a-col :span="5" class="contact_page_title">联系我们</a-col>
    <a-col :span="17"></a-col>
  </a-row>
  <Contact_page_map/>
  <div class="contact_page_text">
    <br/>
    <p style="color: black; font-size: 4vh; margin-bottom: 1vh;font-weight: bold">联系我们</p>
    <p>我们寻找的人，感念际遇，不生苦毒，尊重对手，战胜自己。</p>
    <p>我们首先成为这样的人，我们就将找到这样的人。</p>
    <p>如您想成为同行者，请联系我们：<a>ChinaPIM@sig.com</a></p>
    <p style="margin: 3vh 0;font-size: 2.5vh">上海地址</p>
    <p>上海市黄浦区湖滨路222号企业天地1705-09室</p>
    <p>邮编200021，电话 （+86）21-61222888</p>
    <p>传真（+86）21-61130320</p>
    <p style="margin: 3vh 0;font-size: 2.5vh">北京地址</p>
    <p>北京市朝阳区建国门外大街乙12号双子座大厦东塔1908室</p>
    <p>邮编100022，电话（+86）10-65665096</p>
    <p>传真 (+86）10-65666881</p>
    <br/>
  </div>
  <Footer></Footer>


</template>
<script>
import Contact_page_map from "./Contact_page_map";
import Footer from "@/components/Footer";

export default {
  name: 'Contact_page',
  components: {
    Footer,
    Contact_page_map,
  },
}
</script>
<style>
.contact_page_title {
  background: #2f54eb;
  color: white;
  font-size: 2.6vh;
  height: 5.4vh;
  text-align: left;
  line-height: 5.4vh;
  padding-left: 2vh;
  text-indent: 2em;
}

.contact_page_text p{
  color: grey;
  margin-bottom: 1vh;
}

.contact_page_text {
  margin-left: 8.33vw;
  text-align: left;
}
</style>