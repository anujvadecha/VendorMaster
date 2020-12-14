<template>
  <q-layout view="lHh Lpr lFf">
    <q-header style="background-color: white; color: black;" bordered  >
      <q-toolbar>
        <q-btn
          class="mobile-only"
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />
        <q-toolbar-title class="font-bold">
          <span v-if="currentRouteName==='Home'">
            Zlato
          </span>
          <span v-else>
            {{currentRouteName}}
          </span>
        </q-toolbar-title>
        <div>
        <span class="color:grey mobile-hide">
        <q-btn flat >
          <router-link to="Home" style="text-decoration: None;color: dimgrey">
          <q-icon class="lt-md" size="md" name="mdi-home" ></q-icon>
         </router-link>
        </q-btn>
        <q-btn flat>
          <router-link to="Orders" style="text-decoration: None;color: dimgrey">
          <q-icon class="lt-md" size="md" name="mdi-bag-checked" ></q-icon>
           </router-link>
        </q-btn>
        <q-btn flat>
          <router-link to="Favourites" style="text-decoration: None;color: dimgrey">
          <q-icon class="lt-md" size="md" name="mdi-heart"></q-icon>
            </router-link></q-btn>
        <q-btn flat>
          <router-link to="Account" style="text-decoration: None;color: dimgrey">
          <q-icon class="lt-md"  size="md" name="mdi-account"></q-icon>
            </router-link></q-btn>
          </span>
        </div>
      </q-toolbar>
      <q-toolbar inset>
      <q-space></q-space>
        <q-icon name="mdi-gold"></q-icon>
        <span>1270</span>
        <q-space></q-space>
        <q-icon name="mdi-silverware-clean"></q-icon>
        <span>128392</span>
        <q-space></q-space>
        <q-icon name="mdi-gold"></q-icon>
        <span>78.9</span>
        <q-space></q-space>
      </q-toolbar>
    </q-header>
<!--    <span class="mobile-only ">-->
    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
    >
      <q-list>
<!--        <q-item-label-->
<!--          header-->
<!--          class="text-grey-8"-->
<!--        >-->
<!--          Essential Links-->
<!--        </q-item-label>-->
        <EssentialLink
          v-for="link in essentialLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>
<!--      </span>-->
    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from 'components/EssentialLink.vue'

const linksData = [
  {
    title: 'Home',
    caption: 'HomePage',
    icon: 'mdi-home',
    link: 'https://quasar.dev'
  },
  {
    title: 'Orders',
    caption: 'See your orders',
    icon: 'mdi-bag-checked',
    link: 'https://github.com/quasarframework'
  },
  {
    title: 'Favourites',
    caption: 'See your favourites and compare',
    icon: 'mdi-heart',
    link: 'https://chat.quasar.dev'
  },
  {
    title: 'Account',
    caption: 'Settings for your account',
    icon: 'mdi-account',
    link: 'https://forum.quasar.dev'
  }
]

export default {
  name: 'MainLayout',
  components: { EssentialLink },
  data () {
    return {
      leftDrawerOpen: false,
      essentialLinks: linksData
    }
  },
  computed: {
    currentRouteName () {
      return this.$route.name
    }
  }
}
</script>
