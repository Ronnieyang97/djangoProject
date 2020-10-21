<template>
  <Team_index></Team_index>
  <Team_index_bar></Team_index_bar>
  <router-view/>
<Footer></Footer>
</template>

<script>

import Team_index from "../components/team/Team_index";
import Team_index_bar from "../components/team/Team_index_bar"
import Footer from "../components/Footer";

export default {
  name: 'Team',
  components: {Footer, Team_index_bar, Team_index},

}

</script>