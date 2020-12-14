import Orders from 'pages/Orders'
import Favourites from 'pages/Favourites'
import Home from 'pages/Home'
import Account from 'pages/Account'
import VendorDetails from 'pages/VendorDetails'

const routes = [
  {
    path: '/',
    component: () => import('pages/Home.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') }
    ]
  },
  {
    path: '/orders',
    name: 'Orders',
    component: Orders
  },
  {
    path: '/favourites',
    name: 'Favourites',
    component: Favourites
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/account',
    name: 'Account',
    component: Account
  },
  {
    path: '/vendor/:vendor',
    name: 'Vendor',
    component: VendorDetails,
    props: true
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
