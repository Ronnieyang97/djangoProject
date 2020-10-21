<template>
  <Enterprise_index></Enterprise_index>
  <Enterprise_page></Enterprise_page>
  <Footer></Footer>
</template>

<script>
import Enterprise_index from "@/components/enterprise/Enterprise_index";
import Enterprise_page from "@/components/enterprise/Enterprise_page";
import Footer from "@/components/Footer";
export default {
  name: 'Enterprise',
  components: {Enterprise_page, Enterprise_index,Footer},
}

</script>