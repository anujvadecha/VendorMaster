<!--<template>-->
<!--  <q-layout view="lHh Lpr lFf">-->
<!--      <q-header class="bg-white text-dark" style="" elevated bordered  >-->
<!--      <q-toolbar style="" class="shadow-2">-->
<!--        <q-btn-->
<!--          class="mobile-only"-->
<!--          flat-->
<!--          dense-->
<!--          round-->
<!--          icon="menu"-->
<!--          aria-label="Menu"-->
<!--          @click="leftDrawerOpen = !leftDrawerOpen"-->
<!--        />-->
<!--        <q-toolbar-title class="font-bold">-->
<!--          <span v-if="currentRouteName==='Home'||''||'/'">-->
<!--            <q-img-->
<!--            :src="imageSrc"-->
<!--            transition="scale-transition"-->
<!--            width="40px"-->
<!--            />-->
<!--            <span class="font-bold text-h6">Zlato</span>-->
<!--          </span>-->
<!--          <span v-else>-->
<!--            {{currentRouteName}}-->
<!--          </span>-->
<!--        </q-toolbar-title>-->
<!--        <div>-->
<!--        <span class="color:grey mobile-hide">-->
<!--        <q-btn flat >-->
<!--          <router-link class="text-primary" to="Home" style="text-decoration: None;">-->
<!--          <q-icon class="lt-md" size="md" name="mdi-home" ></q-icon>-->
<!--         </router-link>-->
<!--        </q-btn>-->
<!--        <q-btn flat>-->
<!--          <router-link class="text-primary" to="Orders" style="text-decoration: None;">-->
<!--          <q-icon class="lt-md" size="md" name="mdi-bag-checked" ></q-icon>-->
<!--           </router-link>-->
<!--        </q-btn>-->
<!--        <q-btn flat>-->
<!--          <router-link class="text-primary" to="Favourites" style="text-decoration: None;">-->
<!--          <q-icon class="lt-md" size="md" name="mdi-heart"></q-icon>-->
<!--            </router-link></q-btn>-->
<!--        <q-btn flat>-->
<!--          <router-link class="text-primary" to="Account" style="text-decoration: None;">-->
<!--          <q-icon class="lt-md"  size="md" name="mdi-account"></q-icon>-->
<!--        </router-link></q-btn>-->
<!--        <q-btn-dropdown-->
<!--          flat-->
<!--          class="lt-md text-primary"-->
<!--          label="Account">-->
<!--          <div class="q-pa-md">-->
<!--            <div class="justify-center full-height full-width text-center">-->
<!--              <q-avatar size="72px">-->
<!--                <img src="https://cdn.quasar.dev/img/boy-avatar.png">-->
<!--              </q-avatar>-->
<!--              <div class="text-subtitle1 q-mt-md q-mb-xs">John Doe</div>-->
<!--              <q-btn-->
<!--                @click="logout()"-->
<!--                color="primary"-->
<!--                label="Logout"-->
<!--                size="sm"-->
<!--                v-close-popup-->
<!--              />-->
<!--            </div>-->
<!--          </div>-->
<!--        </q-btn-dropdown>-->
<!--          </span>-->
<!--        </div>-->
<!--      </q-toolbar>-->
<!--      <q-toolbar class="text-dark bg-white" inset style="font-weight: bold">-->
<!--      <q-space></q-space>-->
<!--&lt;!&ndash;        <q-icon name="mdi-gold"></q-icon>&ndash;&gt;-->
<!--        <span class="" style="">Gold : 1270</span>-->
<!--        <q-space></q-space>-->
<!--&lt;!&ndash;        <q-icon name="mdi-silverware-clean"></q-icon>&ndash;&gt;-->
<!--        <span>Silver: 128392</span>-->
<!--        <q-space></q-space>-->
<!--&lt;!&ndash;        <q-icon name="mdi-gold"></q-icon>&ndash;&gt;-->
<!--        <span>Dollar: 78.9</span>-->
<!--        <q-space></q-space>-->
<!--      </q-toolbar>-->
<!--    </q-header>-->
<!--&lt;!&ndash;    <span class="mobile-only ">&ndash;&gt;-->
<!--    <q-drawer-->
<!--      v-model="leftDrawerOpen"-->
<!--      show-if-above-->
<!--      bordered-->
<!--      content-class="bg-grey-1"-->
<!--    >-->
<!--      <q-img class="absolute-top" src="https://images.livemint.com/img/2020/05/02/600x338/73342ce6-87d6-11ea-9881-602785b14c14_1587970192680_1588398410207.jpg" style="height: 150px;">-->
<!--          <div class="absolute-bottom bg-transparent">-->
<!--            <q-avatar size="56px" class="q-mb-sm">-->
<!--              <img src="https://cdn.quasar.dev/img/boy-avatar.png">-->
<!--            </q-avatar>-->
<!--            <div class="text-weight-bold">Deltacap devs</div>-->
<!--            <div>@deltacap devs</div>-->
<!--          </div>-->
<!--        </q-img>-->
<!--      <q-scroll-area style="height: calc(100% - 150px); margin-top: 150px; border-right: 1px solid #ddd">-->
<!--      <q-list>-->
<!--&lt;!&ndash;        <q-item-label&ndash;&gt;-->
<!--&lt;!&ndash;          header&ndash;&gt;-->
<!--&lt;!&ndash;          class="text-grey-8"&ndash;&gt;-->
<!--&lt;!&ndash;        >&ndash;&gt;-->
<!--&lt;!&ndash;          Links&ndash;&gt;-->
<!--&lt;!&ndash;        </q-item-label>&ndash;&gt;-->
<!--        <EssentialLink-->
<!--          v-for="link in essentialLinks"-->
<!--          :key="link.title"-->
<!--          v-bind="link"-->
<!--        />-->
<!--      </q-list>-->
<!--      </q-scroll-area>-->
<!--    </q-drawer>-->
<!--    <q-page-container>-->
<!--      <router-view />-->
<!--    </q-page-container>-->
<!--  </q-layout>-->
<!--</template>-->

<!--<script>-->
<!--import EssentialLink from 'components/EssentialLink.vue'-->
<!--const linksData = [-->
<!--  {-->
<!--    title: 'Home',-->
<!--    caption: 'HomePage',-->
<!--    icon: 'mdi-home',-->
<!--    link: 'https://quasar.dev'-->
<!--  },-->
<!--  {-->
<!--    title: 'Orders',-->
<!--    caption: 'See your orders',-->
<!--    icon: 'mdi-bag-checked',-->
<!--    link: 'https://github.com/quasarframework'-->
<!--  },-->
<!--  {-->
<!--    title: 'Favourites',-->
<!--    caption: 'See your favourites and compare',-->
<!--    icon: 'mdi-heart',-->
<!--    link: 'https://chat.quasar.dev'-->
<!--  },-->
<!--  {-->
<!--    title: 'Account',-->
<!--    caption: 'Settings for your account',-->
<!--    icon: 'mdi-account',-->
<!--    link: 'https://forum.quasar.dev'-->
<!--  }-->
<!--]-->

<!--export default {-->
<!--  name: 'MainLayout',-->
<!--  components: { EssentialLink },-->
<!--  data () {-->
<!--    return {-->
<!--      imageSrc: '/logo.png',-->
<!--      leftDrawerOpen: false,-->
<!--      essentialLinks: linksData-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    logout () {-->
<!--      console.log('logout called')-->
<!--      this.$q.localStorage.set('token', '')-->
<!--      this.$router.push({-->
<!--        name: 'Login'-->
<!--      })-->
<!--    }-->
<!--  },-->
<!--  created () {-->
<!--    this.$q.notify({ message: 'hello' })-->
<!--  },-->
<!--  computed: {-->
<!--    currentRouteName () {-->
<!--      return this.$route.name-->
<!--    },-->
<!--    logged_in: function () {-->
<!--      console.log('logged in is' + this.$q.localStorage.getItem('token'))-->
<!--      const token = this.$q.localStorage.getItem('token')-->
<!--      console.log(token)-->
<!--      if (token === '' || token === null || token === 'null') {-->
<!--        console.log('returning false')-->
<!--        return false-->
<!--      } else {-->
<!--        console.log('returning true')-->
<!--        return true-->
<!--      }-->
<!--    }-->
<!--  }-->
<!--}-->
<!--</script>-->
