<template>
  <div>
    <a-row type="flex">
      <a-col :span="1"></a-col>
      <a-col :span="5" class="concept_page_title">投资理念</a-col>
      <a-col :span="18"></a-col>
    </a-row>
    <a-row type="flex" justify="center">
      <a-col :span="11" class="concept_page_background1"></a-col>
      <a-col :span="11" class="concept_page_text">
        <div style="padding: 4vh 0">
          <p style="font-size: 2.4vh; font-weight: bolder; ">我们的理念</p>
          <p style="font-size: 3vh; font-weight: bolder; ">寻找价值洼地 赋能新生力量</p>
          <p>————</p>
          <p>不信奉风口、跑道和明星</p>
          <p>不追逐风口上的“飞猪” </p>
          <p>以勤奋、低调和宽容</p>
          <p>向下不断探索价值洼地</p>
          <p>以此为念 </p>
          <p>海纳亚洲得以持续前行</p>
          <p>不以物喜 不以己悲</p>
          <p>为资本寻路，为新生力量赋能</p><br>
          <p>我们无法预测哪里有价值洼地 </p>
          <p>但出现洼地的地方</p>
          <p>我们会出现</p>
          <p>这是勤奋，也是风格</p>
          <p>是我们选择了快速生成的洼地</p>
          <p>也是新崛起的力量选择了我们</p>
        </div>
      </a-col>
    </a-row>
    <a-row type="flex" justify="center">
      <a-col :span="11" class="concept_page_text" style="height: 55vh">
        <div style="padding: 6vh">
          <p style="font-size: 3vh; font-weight: bolder;">主要投资领域</p>
          <p>———</p>
          <p style="font-size: 2vh">十余年来，海纳亚洲主要聚焦科技、传媒、消费品、现代服务、医疗、环保等领域。</p>
          <p style="font-size: 2vh">
            我们关注新业态新模式，关注技术创新与裂变，更看重人的禀赋与潜质。我们投资处于各个发展阶段，能够在中国大陆及全球快速推出独到产品及服务，特别关注消费类，服务类，以及数字媒体方面的企业。</p>
        </div>
      </a-col>
      <a-col :span="11" class="concept_page_background2"></a-col>
    </a-row>
    <a-row type="flex" justify="center">
      <a-col :span="11" class="concept_page_background3"></a-col>
      <a-col :span="11" class="concept_page_text">
        <div style="padding: 5vh 0">
          <p style="font-size: 3vh; font-weight: bolder;">独特优势</p>
          <p>————</p>
          <p style="font-size: 2vh">
            十余年来，海纳亚洲已经凝聚了超过260家被投企业，并陪伴被投企业共同经历了完整的经济和投资周期，这使得我们在行业的广度、洞见的深度上积累了相当的经验。被投企业在SIG群体里可以在运营、商业路径、人才、发展战略上分享一线公司的实操经验，并与众多企业达成协同。此外，SIG作为一个全球化的金融集团，在亚洲乃至全球的网络对中国创业公司出海可给予支持，这样的支持正在发生。</p>
          <p style="font-size: 2vh">
            海纳亚洲以自有资金进行投资，可以长久持有。同时，自有资金使得海纳亚洲的投资决策更迅速，可灵活处理各种变数，而无需协同外部投资人或外部投资委员会各方。海纳不跟风，坚持独立的投资理念，辅以快速的决策能力，使得被投企业可以聚焦业务突破与核心竞争力打造，聚焦成长。</p>
          <p style="font-size: 2vh">
            不推崇蜻蜓点水，过去十多年，海纳亚洲以类似联合创始人的方式，孵化了众多初创项目，并在企业后续融资中持续投入、始终持有高股比。专业的投后管理，持久的陪伴方式，使得海纳亚洲与创业公司交融笃深，共赴乾坤。</p>
        </div>
      </a-col>
    </a-row>
    <a-row>
      <a-col :span="1"></a-col>
      <a-col :span="7" class="concept_page_background4">
        <div style="padding-top: 10vh">
          <img src="../../assets/image/concept_page4.png" class="card_img">
          <p style="padding-top: 2vh;font-size:3vh">早 | 直觉</p>
          <p>———</p>
          <p>浩茫广宇，于无声处听惊雷</p>
        </div>
      </a-col>
      <a-col :span="8" class="concept_page_background5">
        <div style="padding-top: 10vh">
          <img src="../../assets/image/concept_page5.png" class="card_img">
          <p style="padding-top: 2vh;font-size:3vh">快 | 决断</p>
          <p>———</p>
          <p>厚积薄发，当断之机则立断</p>
        </div>
      </a-col>
      <a-col :span="7" class="concept_page_background6">
        <div style="padding-top: 10vh">
          <img src="../../assets/image/concept_page6.png" class="card_img">
          <p style="padding-top: 2vh;font-size:3vh">远 | 眼界</p>
          <p>———</p>
          <p>除却浮云，风物长宜放眼量</p>
        </div>
      </a-col>
      <a-col :span="1"></a-col>
    </a-row>

  </div>
</template>

<script>
export default {
  name: 'Concept_page',

}
</script>

<style>
.concept_page_title {
  background: #2f54eb;
  color: white;
  font-size: 2.6vh;
  height: 5.4vh;
  text-align: left;
  line-height: 5.4vh;
  padding-left: 2vh;
  text-indent: 2em;
}

.concept_page_background1 {
  background-image: url("../../assets/image/concept_page1.jpg");
  background-size: 100% 100%;
}

.concept_page_background2 {
  background-image: url("../../assets/image/concept_page2.jpg");
  background-size: 100% 100%;
}

.concept_page_background3 {
  background-image: url("../../assets/image/concept_page3.jpg");
  background-size: 100% 100%;
}

.concept_page_background4 {
  background-image: url("../../assets/background/concept_page4.jpg");
  background-size: 100% 100%;
  height: 30vw;

}

.concept_page_background5 {
  background-image: url("../../assets/background/concept_page5.jpg");
  background-size: 100% 100%;
  height: 30vw;
}

.concept_page_background6 {
  background-image: url("../../assets/background/concept_page6.jpg");
  background-size: 100% 100%;
  height: 30vw;
}

.concept_page_text {
  background: #f3f3f3;
  text-align: left;

}

.concept_page_text p {
  color: black;
  font-size: 1.6vh;
  margin: 0.8vh 3vw;
}
</style>