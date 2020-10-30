<template>
  <a-affix :offset-bottom="10" style="text-align: right; ">
    <a-button type="primary" style="bottom: 25vh;height: 6vh" @click="affix.visible = true">
      <p style="font-size: 1.5vh;padding: 0.5vh 0">法律<br/>声明</p>
    </a-button>
  </a-affix>
  <a-modal v-model:visible="affix.visible" @click="close" width="40vw"
           :centered="true" :footer="null" :closable="false" :bodyStyle="{background: '#0397d6'}">
    <div class="index_affix_text">
      <p style="font-size: 2.4vh;text-align: center">法律声明</p>
      <p>近期可能网络上出现不法分子假冒我司名义进行欺诈活动。</p>
      <p>SIG均用自有资金投资并通过境外全资子公司管理SIG在亚洲的私募股权投资。</p>
      <p>SIG或者其任何子公司从未对外进行任何理财、荐股、虚拟货币买卖等业务的推荐和咨询，避免上当受骗。</p>
      <p>SIG对于诈骗受害人不承担任何责任；若发现任何诈骗行为，请及时告知我们或者向当地公安部门举报，SIG保留追究诈骗人的法律责任。</p>
      <p style="font-size: 2.4vh;text-align: center">Disclaimer</p>
      <p>There are recent cases of illegal use of our company name for fraudulent activities on the Internet.</p>
      <p>SIG is fully internally funded and manages all the Private Equity investments in Asia through its wholly foreign owned subsidiaries.</p>
      <p>SIG, or any of its subsidiaries or affiliates, has neither provided nor referred any consultation service to the public on financial management, stock recommendation, virtual currency trading, etc.</p>
      <p>SIG bears no responsibility to the victims of such fraud. If you are aware of any fraudulent activities, please report to the local Public Security Department and inform us in time. SIG reserves the right to pursue legal action against the fraudster(s).</p>
    </div>
  </a-modal>
</template>
<script>
import {reactive} from 'vue'

export default {
  name: 'Index_affix',
  setup() {
    let affix = reactive({
      visible: true
    })
    const close = () => {
      affix.visible = false
    }
    return {affix, close}
  }
}
</script>
<style>
#app > div > div:nth-child(9) > div {
  /* antd固钉组件有一个<div class>样式只能强制找绝对css路径改 */
  height: 0;
}
.index_affix_text p{
  margin-bottom: 1vh;
  font-size: 2vh;
}
</style>