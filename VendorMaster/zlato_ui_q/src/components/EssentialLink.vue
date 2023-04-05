<template>
<!--  color:rebeccapurple-->
  <router-link style="text-decoration: none; " :to="title">
  <q-item
    clickable
    tag="a"
    target="_blank"
  >
    <q-item-section v-if="icon" avatar>
    <q-icon class="text-primary" :name="icon" />
    </q-item-section>
    <q-item-section class="text-primary" >
      {{ title }}
    </q-item-section>
  </q-item>
  </router-link>
</template>

<script>
export default {
  name: 'EssentialLink',
  props: {
    title: {
      type: String,
      required: true
    },

    caption: {
      type: String,
      default: ''
    },

    link: {
      type: String,
      default: '#'
    },

    icon: {
      type: String,
      default: ''
    }
  }
}
</script>
