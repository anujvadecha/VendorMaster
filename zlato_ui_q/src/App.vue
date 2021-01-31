<template>
  <div id="q-app">
    <router-view></router-view>
  </div>
</template>

<script>

import { FCMPlugin } from 'app/src-cordova/plugins/cordova-plugin-fcm-with-dependecy-updated'
// function formatNow () {
//   var now = new Date()
//   return (
//     now.getHours() +
//     ':' +
//     now.getMinutes() +
//     ':' +
//     now.getSeconds() +
//     '.' +
//     now.getMilliseconds()
//   )
// }

// function addToLog(log) {
//   document.getElementById("notification-logs").innerHTML =
//     "<hr>" +
//     "<p>Received at " +
//     formatNow() +
//     "</p>" +
//     log +
//     document.getElementById("notification-logs").innerHTML;
// }

function trySomeTimes (asyncFunc, onSuccess, onFailure, customTries) {
  var tries = typeof customTries === 'undefined' ? 100 : customTries
  var interval = setTimeout(function () {
    if (typeof asyncFunc !== 'function') {
      onSuccess('Unavailable')
      return
    }
    asyncFunc()
      .then(function (result) {
        if ((result !== null && result !== '') || tries < 0) {
          onSuccess(result)
        } else {
          trySomeTimes(asyncFunc, onSuccess, onFailure, tries - 1)
        }
      })
      .catch(function (e) {
        clearInterval(interval)
        onFailure(e)
      })
  }, 100)
}

function setupOnTokenRefresh () {
  FCMPlugin.eventTarget.addEventListener(
    'tokenRefresh',
    function (data) {
      console.log(data)
      // addToLog('<p>FCM Token refreshed to ' + data.detail + '</p>')
    },
    false
  )
}

function setupOnNotification () {
  FCMPlugin.eventTarget.addEventListener(
    'notification',
    function (data) {
      cordova.plugins.notification.local.schedule({
        title: 'My first notification',
        text: data
      })
    },
    false
  )
  FCMPlugin.getInitialPushPayload()
    .then((payload) => {
      cordova.plugins.notification.local.schedule({
        title: 'My first notification',
        text: payload
      })
      // addToLog(
      //   "<p>Initial Payload</p><pre>" +
      //     JSON.stringify(payload, null, 2) +
      //     "</pre>"
      // );
    })
    .catch((error) => {
      cordova.plugins.notification.local.schedule({
        title: 'My first notification',
        text: error
      })
    })
}

function logFCMToken () {
  console.log('Trying for fcm token')
  trySomeTimes(
    FCMPlugin.getToken,
    function (token) {
      console.log('token is ' + token.toString())
      cordova.plugins.notification.local.schedule({
        title: 'My token is',
        text: token
      })
    },
    function (error) {
      cordova.plugins.notification.local.schedule({
        title: 'Error creating token',
        text: error
      })
    }
  )
}

function logAPNSToken () {
  if (cordova.platformId !== 'ios') {
    return
  }
  FCMPlugin.getAPNSToken(
    function (token) {
      console.log(token)
      // addToLog('<p>Started listening APNS as ' + token + '</p>')
    },
    function (error) {
      console.log(error)
      // addToLog('<p>Error on listening for APNS token: ' + error + '</p>')
    }
  )
}

// function setupClearAllNotificationsButton() {
//   document.getElementById("clear-all-notifications").addEventListener(
//     "click",
//     function () {
//       FCM.clearAllNotifications();
//     },
//     false
//   );
// }
//
// function setupClearAllNotificationsButton() {
//   document.getElementById("delete-instance-id").addEventListener(
//     "click",
//     function () {
//       FCM.deleteInstanceId().catch(function (error) {
//         alert(error);
//       });
//     },
//     false
//   );

function waitForPermission (callback) {
  FCMPlugin.requestPushPermission()
    .then(function (didIt) {
      if (didIt) {
        callback()
      } else {
        // addToLog("<p>Push permission was not given to this application</p>");
      }
    })
    .catch(error => {
      console.log(error)
      // addToLog("<p>Error on checking permission: " + error + "</p>");
    })
}

function setupListeners () {
  waitForPermission(function () {
    FCMPlugin.createNotificationChannel({
      id: 'sound_alert6',
      name: 'Sound Alert6',
      // description: "Useless",
      importance: 'high',
      // visibility: "public",
      sound: 'elet_mp3'
      // lights: false,
      // vibration: false,
    })
    logFCMToken()
    logAPNSToken()
    setupOnTokenRefresh()
    setupOnNotification()
    // setupClearAllNotificationsButton();
  })
}
document.addEventListener('deviceready', () => {
  try {
    // FCMPlugin.getToken(function (token) {
    //   console.log(token)
    //   FCMPlugin.onNotification(function (data) {
    //     console.log(data)
    //     cordova.plugins.notification.local.schedule({
    //       title: 'My first notification',
    //       text: data.toString()
    //     })
    //   })
    // })
    setupListeners().then(cordova.plugins.notification.local.schedule({
      title: 'Welcome to zlato',
      text: 'Your experience is high priority , We shall connect you to high speed data. '
    }))
  } catch (err) {
    cordova.plugins.notification.local.schedule({
      title: 'An error has occured',
      text: err.toString()
    })
  }
  cordova.plugins.notification.local.schedule({
    title: 'Welcome to zlato',
    text: 'Your experience is high priority , We shall connect you to high speed data. '
  })
}, false)

export default {
  name: 'App',
  created () {

  }
}
</script>
