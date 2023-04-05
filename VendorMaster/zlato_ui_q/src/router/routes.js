// import Orders from 'pages/Orders'
// import Favourites from 'pages/Favourites'
import Home from 'pages/Home'
// import Account from 'pages/Account'
// import VendorDetails from 'pages/VendorDetails'
// import Login from 'pages/Login'
// import Register from 'pages/Register'
// import Marketing from 'pages/Marketing'
import Main from 'pages/Main'
import UserMargins from 'pages/UserMargins'
import Register from 'pages/Register'
// import UserMargins from 'pages/UserMargins'
// import RegistrationForm from 'components/RegistrationForm'
// import Vendors from 'pages/Vendors'

const routes = [
  {
    path: '/main',
    name: 'Marketing',
    component: import('pages/Marketing')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('pages/Login'),
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
        component: () => import('pages/Orders'),
        name: 'Orders'
      },
      {
        path: 'favourites',
        component: () => import('pages/Favourites'),
        name: 'Favourites'
      },
      {
        path: 'account',
        name: 'Account',
        component: () => import('pages/Account')
      },
      {
        path: 'vendor',
        name: 'Vendor',
        component: () => import('pages/VendorDetails'),
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
        component: () => import('components/RegistrationForm')
      },
      {
        path: 'vendors',
        name: 'Vendors',
        component: () => import('pages/Vendors')
      }
    ]
  },
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
