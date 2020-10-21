<template>
<Concept_index></Concept_index>
  <Concept_page></Concept_page>
  <a-row style="height: 5vh"/>
  <Footer></Footer>
</template>

<script>
import Concept_index from '../components/concept/Concept_index';
import Concept_page from "../components/concept/Concept_page";
import Footer from "../components/Footer";
export default {
  name: 'Concept',
  components: {Concept_page, Concept_index, Footer},
}

</script>