(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[8],{"0b35":function(e,t,r){"use strict";r.r(t);var s=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("q-pull-to-refresh",{on:{refresh:e.refresher}},[e.orders_to_rate.length>0?r("div",e._l(e.orders_to_rate,(function(e){return r("div",{key:e.order_id},[r("Rating",{attrs:{data:[e.instrument_id.vendor_id,e.instrument_id.vendor,!0]}})],1)})),0):e._e(),r("div",{},[r("div",{staticClass:"q-gutter-y-md"},[r("q-card",{attrs:{flat:""}},[r("q-tabs",{staticClass:"text-grey",attrs:{"active-color":"primary","indicator-color":"primary",align:"justify","narrow-indicator":"",stretch:""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[r("q-tab",{attrs:{name:"executed",label:"Executed"}}),r("q-tab",{attrs:{name:"pending",label:"Pending"}}),r("q-tab",{attrs:{name:"closed",label:"Closed"}})],1),r("q-separator"),r("q-tab-panels",{attrs:{swipeable:"",animated:""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[r("q-tab-panel",{attrs:{name:"executed"}},[r("ExecutedOrders",{attrs:{waiting:e.executed_orders_waiting,confirmed:e.executed_orders_confirmed}})],1),r("q-tab-panel",{attrs:{name:"pending"}},[r("PendingOrders",{attrs:{pending:e.active_orders,refresh:this.get_orders}})],1),r("q-tab-panel",{attrs:{name:"closed"}},[r("ClosedOrders",{attrs:{closed:e.closed_orders}})],1)],1)],1)],1)])])],1)},a=[],i=(r("4e82"),function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[e.waiting.length>0||e.confirmed.length>0?r("div",[r("div",{},[r("OrderItemTable",{attrs:{orders:e.confirmed,title:"Confirmed"}}),r("OrderItemTable",{attrs:{orders:e.waiting,title:"Waiting"}})],1)]):r("div",[r("div",{staticClass:"row align-middle"},[r("div",{staticClass:"center"},[r("q-img",{staticClass:"q-ml-lg",attrs:{width:"200px",src:"Human.png"}})],1),r("q-card",{staticClass:"q-ma-md"},[r("div",{staticClass:"text-h6 font-bold q-ma-lg"},[e._v("No Executed orders")]),r("div",{staticClass:" q-ma-lg"},[e._v("To place an order. Please go to  "),r("q-btn",{on:{click:function(t){return e.$router.push("Home")}}},[e._v("Home")])],1)])],1)])])}),o=[],n=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[e.orders.length>0?r("div",[r("q-table",{attrs:{grid:"","card-class":"bg-primary text-white",title:e.title,data:e.orders,"row-key":"name",filter:e.filter,"hide-header":"","hide-no-data":"",pagination:e.pagination},scopedSlots:e._u([{key:"top-right",fn:function(){return[r("q-input",{attrs:{borderless:"",dense:"",debounce:"300",placeholder:"Search"},scopedSlots:e._u([{key:"append",fn:function(){return[r("q-icon",{attrs:{name:"search"}})]},proxy:!0}],null,!1,4009527860),model:{value:e.filter,callback:function(t){e.filter=t},expression:"filter"}})]},proxy:!0},{key:"item",fn:function(e){return[r("div",{staticClass:"q-pa-xs col-xs-12 col-sm-12 col-md-6"},[r("OrderItem",{attrs:{order:e.row}})],1)]}}],null,!1,402120872)})],1):r("div",[e.show_illustration?r("div",[r("div",{staticClass:"row align-middle"},[r("div",{staticClass:"center"},[r("q-img",{staticClass:"q-ml-lg",attrs:{width:"200px",src:"Human.png"}})],1),r("q-card",{staticClass:"q-ma-md"},[r("div",{staticClass:"text-h6 font-bold q-ma-lg"},[e._v("No "+e._s(e.title)+" orders")]),r("div",{staticClass:" q-ma-lg"},[e._v("To place an order. Please go to\n          "),r("q-btn",{on:{click:function(t){return e.$router.push("Home")}}},[e._v("Home")])],1)])],1)]):e._e()]),void 0!==e.best_limit_orders?r("div",[e.best_limit_orders.length>0?r("div",[r("q-table",{attrs:{grid:"","card-class":"bg-primary text-white",title:e.title,data:e.best_limit_orders,"row-key":"name",filter:e.filter,"hide-header":"","hide-no-data":"",pagination:e.pagination},scopedSlots:e._u([{key:"top-right",fn:function(){return[r("q-input",{attrs:{borderless:"",dense:"",debounce:"300",placeholder:"Search"},scopedSlots:e._u([{key:"append",fn:function(){return[r("q-icon",{attrs:{name:"search"}})]},proxy:!0}],null,!1,4009527860),model:{value:e.filter,callback:function(t){e.filter=t},expression:"filter"}})]},proxy:!0},{key:"item",fn:function(e){return[r("div",{staticClass:"q-pa-xs col-xs-12 col-sm-12 col-md-6"},[r("BestLimitOrderItem",{attrs:{order:e.row}})],1)]}}],null,!1,1504375389)})],1):e._e()]):e._e()])},d=[],l=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{},[r("q-card",{staticClass:"my-card",attrs:{square:"",flat:"",bordered:""}},[r("q-card-actions",{attrs:{align:"right"}},[r("div",{staticClass:"justify-start"},[r("q-chip",{attrs:{outline:"",color:"black",dense:""}},[e._v("ID : "+e._s(e.order.transaction_id))])],1),"EXECUTED"===e.order.status?r("div",["BEST_LIMIT"===e.order.type?r("q-chip",{attrs:{outline:"",color:"orange",dense:""}},[e._v("BEST_LIMIT")]):e._e(),r("q-chip",{attrs:{outline:"",size:"md",color:"green",dense:""}},[e._v("Payment confirmed")]),r("q-chip",{attrs:{outline:"",color:"blue",dense:""}},[e._v("OTP:"+e._s(e.order.otp))])],1):e._e(),"OPEN"===e.order.status?r("div",["BEST_LIMIT"===e.order.type?r("q-chip",{attrs:{outline:"",color:"orange",dense:""}},[e._v("BEST_LIMIT")]):e._e(),r("q-chip",{attrs:{outline:"",color:"blue",dense:""}},[e._v("Waiting for payment")])],1):e._e(),"WAITING_FOR_LIMIT"===e.order.status?r("div",["BEST_LIMIT"===e.order.type?r("q-chip",{attrs:{outline:"",color:"orange",dense:""}},[e._v("BEST_LIMIT")]):e._e(),r("q-chip",{attrs:{outline:"",color:"blue",dense:""}},[e._v("Limit Order waiting")]),e.is_cancelled?r("q-chip",{attrs:{outline:"",color:"red",dense:""}},[e._v("Cancelled")]):r("q-btn",{attrs:{outline:"",color:"black",dense:""},on:{click:function(t){return e.cancel_limit_order()}}},[e._v("CANCEL")])],1):e._e(),"CLOSED"===e.order.status?r("div",[r("q-chip",{attrs:{outline:"",color:"green",dense:""}},[e._v("Closed")])],1):e._e()]),r("q-separator"),r("div",{on:{click:function(t){return e.set_order_details()}}},[r("div",{staticClass:"row q-ma-sm"},[r("div",{staticClass:"col"},[r("strong",[e._v(e._s(e.order.instrument.vendor))]),r("span",{staticClass:"font-bold q-ml-xs-sm "},[e._v(" "+e._s(e.order.instrument.name))])]),r("div",{staticClass:"col"},[r("div",{staticClass:"text-right align-right"},[r("div",{staticClass:"col text-right"},[e._v("Price:"+e._s(e.order.price))])])])]),r("div",{staticClass:"row q-ma-sm"},[r("div",{staticClass:"col"},[r("q-chip",{attrs:{dense:"",outline:"",color:"orange"}},[e._v(e._s(e.order.side)+" ")]),e._v(" "+e._s(e.order.quantity)+"\n        "),r("span",{staticClass:"q-ml-sm",staticStyle:{color:"grey"}},[r("q-icon",{attrs:{name:"mdi-clock"}}),e._v(e._s(e.get_formated_time))],1)],1),r("span",{staticClass:"text-sm q-ml-sm",staticStyle:{color:"grey"}},[e._v("ltp: "+e._s(e.order.instrument.ask))])])])],1)],1)},c=[],_=r("c993"),u={name:"OrderItem",props:["order"],computed:{get_formated_time(){const e=new Date(this.order.created_at);return e.toLocaleString("en-GB")},logged_in:function(){const e=this.$q.localStorage.getItem("token");return""!==e&&null!==e&&"null"!==e},is_cancelled:function(){return this.cancelled}},methods:{set_order_details(){this.$store.dispatch("set_order_details",this.order),console.log(this.$store.state.order_details_selected),this.$store.state.order_details_bottom_sheet=!0},cancel_limit_order(){console.log("limit order cancellation request for"+this.order),Object(_["e"])({order_id:this.order.order_id}).then((e=>{this.cancelled=!0}))}},data:function(){return{cancelled:!1}}},m=u,p=r("2877"),h=r("f09f"),g=r("4b7e"),v=r("b047"),f=r("9c40"),b=r("eb85"),q=r("0016"),C=r("eebe"),x=r.n(C),w=Object(p["a"])(m,l,c,!1,null,"2efe8cec",null),I=w.exports;x()(w,"components",{QCard:h["a"],QCardActions:g["a"],QChip:v["a"],QBtn:f["a"],QSeparator:b["a"],QIcon:q["a"]});var y=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{},[r("q-card",{staticClass:"my-card",attrs:{square:"",flat:"",bordered:""}},[r("q-card-actions",{attrs:{align:"right"}},[r("div",{staticClass:"justify-start"},[r("q-chip",{attrs:{outline:"",color:"black",dense:""}},[e._v("ID : "+e._s(e.order.best_limit_id))])],1),r("q-chip",{attrs:{outline:"",color:"orange",dense:""}},[e._v("BEST_LIMIT")]),e.is_cancelled?r("q-chip",{attrs:{outline:"",color:"red",dense:""}},[e._v("Cancelled")]):r("q-btn",{attrs:{outline:"",color:"black",dense:""},on:{click:function(t){return e.cancel_limit_order()}}},[e._v("CANCEL")])],1),r("q-expansion-item",{staticClass:"font-bold",attrs:{label:e.order.orders[0].instrument.vendor+" :"+e.order.orders[0].instrument.name+"  +"+(e.order.orders.length-1)+" more"}},e._l(e.order.orders,(function(t){return r("div",{key:t.order_id},[r("q-separator"),r("div",{staticClass:"row q-ma-sm"},[r("div",{staticClass:"col"},[r("strong",[e._v(e._s(t.instrument.vendor))]),r("span",{staticClass:"font-bold q-ml-xs-sm "},[e._v(" "+e._s(t.instrument.name))])]),r("span",{staticClass:"text-right text-sm q-ml-sm",staticStyle:{color:"grey"}},[e._v("ltp: "+e._s(t.instrument.ask))])])],1)})),0),r("q-separator"),r("div",{staticClass:"row q-ma-sm"},[r("div",{staticClass:"col"},[r("q-chip",{attrs:{dense:"",outline:"",color:"orange"}},[e._v(e._s(e.order.orders[0].side)+" ")]),e._v(" "+e._s(e.order.orders[0].quantity)+"\n          "),r("span",{staticClass:"q-ml-sm",staticStyle:{color:"grey"}},[r("q-icon",{attrs:{name:"mdi-clock"}}),e._v(e._s(e.get_formated_time))],1)],1),r("div",{staticClass:"col"},[r("div",{staticClass:"text-right align-right"},[r("div",{staticClass:"col text-right"},[e._v("Price:"+e._s(e.order.orders[0].price))])])])])],1)],1)},O=[],T={name:"BestLimitOrderItem",props:["order"],computed:{get_formated_time(){const e=new Date(this.order.orders[0].created_at);return e.toLocaleString("en-GB")},logged_in:function(){const e=this.$q.localStorage.getItem("token");return""!==e&&null!==e&&"null"!==e},is_cancelled:function(){return this.cancelled}},methods:{cancel_limit_order(){console.log(this.order.orders),this.order.orders.map((e=>{Object(_["e"])({order_id:e.order_id}).then((e=>{this.cancelled=!0}))}))}},data:function(){return{cancelled:!1}},created(){}},Q=T,k=r("3b73"),E=Object(p["a"])(Q,y,O,!1,null,"eeae11ec",null),S=E.exports;x()(E,"components",{QCard:h["a"],QCardActions:g["a"],QChip:v["a"],QBtn:f["a"],QExpansionItem:k["a"],QSeparator:b["a"],QIcon:q["a"]});var P={name:"OrderItemTable",components:{BestLimitOrderItem:S,OrderItem:I},props:["orders","best_limit_orders","title","show_illustration"],data:function(){return{filter:"",pagination:{rowsPerPage:0}}},created(){}},L=P,B=r("eaac"),j=r("27f9"),$=r("068f"),D=Object(p["a"])(L,n,d,!1,null,"56ece881",null),M=D.exports;x()(D,"components",{QTable:B["a"],QInput:j["a"],QIcon:q["a"],QImg:$["a"],QCard:h["a"],QBtn:f["a"]});var N={name:"ExecutedOrders",props:["confirmed","waiting"],components:{OrderItemTable:M},created(){console.log(this.waiting.length),console.log(this.confirmed.length)}},A=N,R=Object(p["a"])(A,i,o,!1,null,"0582aaf8",null),H=R.exports;x()(R,"components",{QImg:$["a"],QCard:h["a"],QBtn:f["a"]});var G=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("OrderItemTable",{attrs:{orders:e.pending_orders,best_limit_orders:e.best_limit,show_illustration:!0,title:"Pending limit"}})],1)},W=[],V={name:"PendingOrders",components:{OrderItemTable:M},props:["pending"],data:function(){return{pending_orders:[],best_limit:[]}},created(){var e={};for(var t in this.pending.map((t=>{"BEST_LIMIT"===t.type?(t.best_limit_id in e||(e[t.best_limit_id]=[]),e[t.best_limit_id].push(t)):this.pending_orders.push(t)})),e){var r={best_limit_id:t,orders:e[t]};this.best_limit.push(r)}}},z=V,F=Object(p["a"])(z,G,W,!1,null,null,null),J=F.exports,U=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("OrderItemTable",{attrs:{show_illustration:!0,orders:e.closed}})},X=[],Y={name:"ClosedOrders",components:{OrderItemTable:M},props:["closed"]},K=Y,Z=Object(p["a"])(K,U,X,!1,null,"05a4a288",null),ee=Z.exports,te=function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",[r("q-dialog",{model:{value:e.card,callback:function(t){e.card=t},expression:"card"}},[r("q-card",[r("q-card-section",{staticClass:"bg-primary text-h6",staticStyle:{color:"white"}},[e._v("\n            "+e._s(e.order.instrument_id.vendor)+"\n          ")]),r("q-card-section",[r("q-rating",{attrs:{"aria-placeholder":"Please provide a rating for the Vendor!",max:5,size:"32px"},model:{value:e.stars,callback:function(t){e.stars=t},expression:"stars"}})],1),r("q-card-section",[r("div",[r("q-input",{attrs:{label:"Please leave a review here ...",filled:"",type:"textarea",cols:"33",rows:"10",autogrow:""},model:{value:e.rating_text,callback:function(t){e.rating_text=t},expression:"rating_text"}})],1)]),r("q-separator"),r("q-card-actions",{attrs:{align:"right"}},[r("q-btn",{attrs:{flat:"",color:"primary",label:"Submit"},on:{click:e.rateVendor}})],1)],1)],1)],1)},re=[],se=r("2a19"),ae={name:"Rating",props:["data"],methods:{rateVendor(){if(!this.stars)return void se["a"].create({message:"Please provide a rating for the given vendor",position:"top-right"});if(this.stars>2)this.card=!1;else if(this.stars<3&&0===this.rating_text.length)return void se["a"].create({message:"Please provide a review for rating below 3",position:"top-right"});this.card=!1;const e={vendor_id:this.order.instrument_id.vendor_id,rating:this.stars,rating_text:this.rating_text,is_rated:!0,order_id:this.order.order_id};Object(_["j"])(e).then((e=>{console.log(e),se["a"].create({message:"Your review has been successfully delivered!",position:"top-right"}),this.order.is_rated=!0})).catch((e=>{console.log(e),se["a"].create({message:"Your rating could not be submitted!",position:"top-right"})}))}},data(){return{order:[],card:!1,rating_text:"",stars:""}},created(){this.order=this.data[0],this.card=this.data[1],console.log("Created of rating!"),console.log(this.data)}},ie=ae,oe=r("24e8"),ne=r("a370"),de=r("daf4"),le=Object(p["a"])(ie,te,re,!1,null,"0fd9c923",null),ce=le.exports;x()(le,"components",{QDialog:oe["a"],QCard:h["a"],QCardSection:ne["a"],QRating:de["a"],QInput:j["a"],QSeparator:b["a"],QCardActions:g["a"],QBtn:f["a"]});var _e={name:"Orders",components:{ClosedOrders:ee,PendingOrders:J,ExecutedOrders:H,Rating:ce},data(){return{tab:"executed",orders:[],active_orders:[],executed_orders_confirmed:[],executed_orders_waiting:[],closed_orders:[],orders_to_rate:[]}},methods:{refresher(e){this.get_orders().then(e())},get_orders(){return Object(_["f"])().then((e=>{this.orders=e})).then((()=>{this.orders=this.orders.map((e=>(e.instrument=this.$store.getters.get_instrument(e.instrument_id),e)))})).then((()=>{this.orders.sort(((e,t)=>new Date(t.created_at)-new Date(e.created_at)))})).then((()=>{})).then((()=>{this.active_orders=this.orders.filter((e=>"WAITING_FOR_LIMIT"===e.status)),this.executed_orders_waiting=this.orders.filter((e=>"OPEN"===e.status)),this.executed_orders_waiting.sort(((e,t)=>new Date(t.created_at)-new Date(e.created_at))),this.executed_orders_confirmed=this.orders.filter((e=>"EXECUTED"===e.status)),this.closed_orders=this.orders.filter((e=>"CLOSED"===e.status)),this.orders_to_rate=this.orders.filter((e=>"CLOSED"===e.status&&!1===e.is_rated))}))}},created(){this.get_orders()}},ue=_e,me=r("59d7"),pe=r("429b"),he=r("7460"),ge=r("adad"),ve=r("823b"),fe=Object(p["a"])(ue,s,a,!1,null,"38fc3db4",null);t["default"]=fe.exports;x()(fe,"components",{QPullToRefresh:me["a"],QCard:h["a"],QTabs:pe["a"],QTab:he["a"],QSeparator:b["a"],QTabPanels:ge["a"],QTabPanel:ve["a"]})}}]);