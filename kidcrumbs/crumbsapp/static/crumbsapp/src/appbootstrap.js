import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import Vue2Filters from 'vue2-filters'
import VeeValidate from 'vee-validate';
import {Validator} from 'vee-validate';
import * as directives from './directives';
import VCalendar from 'v-calendar';
import 'v-calendar/lib/v-calendar.min.css';
import VModal from 'vue-js-modal'
import VueCtkDateTimePicker from 'vue-ctk-date-time-picker';
import 'vue-ctk-date-time-picker/dist/vue-ctk-date-time-picker.min.css';
import Toasted from 'vue-toasted';
import Notifications from 'vue-notification';
import { MdCheckbox,MdSwitch,MdDivider, MdAvatar, MdField,MdTabs, MdRadio, MdDatepicker, MdButton, MdDialog, MdMenu, MdListItem, MdList } from 'vue-material/dist/components';
import 'vue-material/dist/vue-material.min.css';
import 'vue-material/dist/theme/default.css';
import 'vue-material/dist/theme/default-dark.css';
import './styles/material_styles.scss';
import VueGoodTablePlugin from 'vue-good-table';
import http from './http';

// import the styles 
import 'vue-good-table/dist/vue-good-table.css'
Vue.use(VeeValidate);


Vue.use(Vue2Filters);
Vue.use(VModal)
Vue.use(Toasted, {
    duration : 3000, 
    position : 'top-center',
    fullWidth : true
})
Vue.use(Notifications)
Vue.use(MdCheckbox)
Vue.use(MdSwitch)
Vue.use(MdRadio)
Vue.use(MdField)
Vue.use(MdTabs)
Vue.use(MdDialog)
Vue.use(MdDivider)
Vue.use(MdDatepicker)
Vue.use(MdButton)
Vue.use(MdMenu)
Vue.use(MdList)
Vue.use(MdAvatar)
Vue.use(VueGoodTablePlugin);


Vue.component('dtpicker', VueCtkDateTimePicker);
// Access v-calendar, v-date-packer and v-popover components
Vue.use(VCalendar, {
   formats: {
    title: 'MMMM YYYY',
    weekdays: 'W',
    navMonths: 'MMM',
    input: ['DD/MM/YYYY', 'DD/MM/YYYY','DD-MM-YYYY','YYYY-MM-DD'],
    dayPopover: 'DD/MM/YYYY',
    data: [ 'DD/MM/YYYY','DD-MM-YYYY','YYYY-MM-DD']
  }
});


Vue.use(VueRouter);
Vue.use(Vuex);


import routes from './routes';
import AppStore from "./store";

const store = new Vuex.Store(AppStore);
const router = new VueRouter({
    mode: 'history',
    routes
});

export {Vue, store, router}
