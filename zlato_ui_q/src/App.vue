<template>
  <div id="q-app">
    <router-view></router-view>
  </div>
</template>

<script>
document.addEventListener('deviceready', () => {
  // cordova.plugins.FCMPlugin.getToken(function (token) {
  //   console.log(token)
  // cordova.plugins.FCMPlugin.onNotification(function (data) {
  //   console.log(data)
  //   cordova.plugins.notification.local.schedule({
  //     title: 'My first notification',
  //     text: data.toString()
  //   })
  // })
  // })
  console.log('deviceready')
  cordova.plugins.notification.local.schedule({
    title: 'My first notification',
    text: 'Thats pretty easy...'
  })
}, false)

export default {
  name: 'App',
  created () {

  }
}
</script>
