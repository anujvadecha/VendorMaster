(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([[10],{ed35:function(e,t,a){"use strict";a.r(t);var s=function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",[a("q-card",{staticClass:"q-ma-md",staticStyle:{height:"100%"}},[a("q-img",{staticStyle:{"max-height":"250px"},attrs:{alt:"https://source.unsplash.com/featured?nature,water",src:e.get_vendor_background_image(e.vendor_object.vendor.theme.background_image)}},[a("div",{staticClass:"absolute-bottom"},[a("div",{staticClass:"row"},[a("q-img",{staticStyle:{width:"15%","max-width":"80px"},attrs:{alt:"https://source.unsplash.com/featured?nature,water",src:e.get_vendor_background_image(e.vendor_object.vendor.theme.logo)}}),a("div",{staticClass:"col-9 q-ml-md"},[a("div",{staticClass:"text-h6"},[e._v(e._s(e.vendor_object.vendor.name))]),a("div",{staticClass:"text-subtitle2"},[e._v(e._s(e.vendor_object.vendor.vendor_details.collection_address))]),a("div",{staticClass:"text-subtitle2"},[e._v("Call: "+e._s(e.vendor_object.vendor.vendor_details.mobile_number_1)+" /"+e._s(e.vendor_object.vendor.vendor_details.mobile_number_2))])])],1)])]),a("TickerPriceTable",{attrs:{title:"Our symbols",instruments_to_render:e.vendor_object.instruments}}),a("q-card",{attrs:{flat:"",bordered:""}},[a("div",{staticClass:"q-ma-md text-h6"},[e._v("Messages from "+e._s(e.vendor_object.vendor.name))]),a("div",{staticClass:"q-ma-md"},[a("span",{domProps:{innerHTML:e._s(e.vendor_object.vendor.vendor_details.messages)}})])]),a("q-card",[a("div",{staticClass:"q-ma-md text-h6"},[e._v("Company info from "+e._s(e.vendor_object.vendor.name))]),a("q-tabs",{staticClass:"text-grey",attrs:{"active-color":"primary","indicator-color":"primary",align:"justify","narrow-indicator":""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[a("q-tab",{attrs:{name:"About-us",label:"About us"}}),a("q-tab",{attrs:{name:"Contact-info",label:"Contact info"}}),a("q-tab",{attrs:{name:"Delivery-charges",label:"Delivery charges"}})],1),a("q-separator"),a("q-tab-panels",{attrs:{swipeable:"",animated:""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[a("q-tab-panel",{attrs:{name:"About-us"}},[a("span",{domProps:{innerHTML:e._s(e.vendor_object.vendor.vendor_details.about_us)}})]),a("q-tab-panel",{attrs:{name:"Contact-info"}},[a("span",{domProps:{innerHTML:e._s(e.vendor_object.vendor.vendor_details.contact_details)}})]),a("q-tab-panel",{attrs:{name:"Delivery-charges"}},[a("span",{domProps:{innerHTML:e._s(e.vendor_object.vendor.vendor_details.delivery_charges)}})])],1)],1)],1)],1)},r=[],o=a("4bff"),n=a("c993"),d={name:"VendorDetails",props:["vendor_object","vendor"],components:{TickerPriceTable:o["a"]},data(){return{tab:"About-us",headers:[{text:"Symbol",value:"name"},{text:"Bid",value:"bid",filterable:!1},{text:"Ask",value:"ask",filterable:!1},{text:"High",value:"high",filterable:!1},{text:"Low",value:"low",filterable:!1}],selected_item:null}},methods:{get_vendor_background_image(e){return null===e?"https://source.unsplash.com/featured?nature,water":n["c"].concat(e)}}},l=d,i=a("2877"),c=a("f09f"),b=a("068f"),v=a("429b"),m=a("7460"),_=a("eb85"),u=a("adad"),p=a("823b"),f=a("eebe"),h=a.n(f),g=Object(i["a"])(l,s,r,!1,null,"44f2af8c",null);t["default"]=g.exports;h()(g,"components",{QCard:c["a"],QImg:b["a"],QTabs:v["a"],QTab:m["a"],QSeparator:_["a"],QTabPanels:u["a"],QTabPanel:p["a"]})}}]);