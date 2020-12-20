import Orders from 'pages/Orders'
import Favourites from 'pages/Favourites'
import Home from 'pages/Home'
import Account from 'pages/Account'
import VendorDetails from 'pages/VendorDetails'
import Login from 'pages/Login'
import Register from 'pages/Register'
import Marketing from 'pages/Marketing'
import Main from 'pages/Main'
// import Login from 'pages/Login'

// const routes = [

//   {
//     path: '/',
//     component: () => import('pages/Home.vue'),
//     children: [
//       { path: '', component: () => import('pages/Index.vue') }
//     ]
//   },
//   {
//     path: '/orders',
//     name: 'Orders',
//     component: Orders
//   },
//   {
//     path: '/favourites',
//     name: 'Favourites',
//     component: Favourites
//   },
//   {
//     path: '/home',
//     name: 'Home',
//     component: Home
//   },
//   {
//     path: '/account',
//     name: 'Account',
//     component: Account
//   },
//   {
//     path: '/login',
//     name: 'Login',
//     component: Login
//   },
//   {
//     path: '/vendor',
//     name: 'Vendor',
//     component: VendorDetails,
//     props: true
//   },
//   {
//     path: '*',
//     component: () => import('pages/Error404.vue')
//   }
// ]

const routes = [
  {
    path: '/main',
    component: Marketing
  },
  {
    path: '/login',
    component: Login
  },
  {
    path: '/register',
    component: Register
  },
  {
    path: '/',
    component: Main,
    name: 'Main',
    children: [
      {
        path: '',
        component: Home,
        name: 'Home'
      },
      {
        path: 'orders',
        component: Orders,
        name: 'Orders'
      },
      {
        path: 'favourites',
        component: Favourites,
        name: 'Favourites'
      },
      {
        path: 'account',
        component: Account,
        name: 'Account'
      },
      {
        path: 'vendor',
        name: 'Vendor',
        component: VendorDetails,
        props: true
      }
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
