<template>
  <News_index></News_index>
  <News_page></News_page>
</template>

<script>
import News_index from "@/components/news/News_index";
import News_page from "@/components/news/News_page";
export default {
  name: 'News',
  components: {News_index, News_page},
}

</script>