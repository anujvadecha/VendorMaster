import Orders from 'pages/Orders'
import Favourites from 'pages/Favourites'
import Home from 'pages/Home'
import Account from 'pages/Account'
import VendorDetails from 'pages/VendorDetails'
import Login from 'pages/Login'
import Register from 'pages/Register'
import Marketing from 'pages/Marketing'
import Main from 'pages/Main'
import UserMargins from 'pages/UserMargins'
import RegistrationForm from 'components/RegistrationForm'

const routes = [
  {
    path: '/main',
    name: 'Marketing',
    component: Marketing
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    props: true
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/',
    component: Main,
    name: 'Main',
    children: [
      {
        path: 'home',
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
      },
      {
        path: 'margins',
        name: 'Margins',
        component: UserMargins
      },
      {
        path: 'registration',
        name: 'Registration',
        component: RegistrationForm
      }
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
