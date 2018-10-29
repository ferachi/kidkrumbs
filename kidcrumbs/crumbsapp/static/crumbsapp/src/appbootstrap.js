import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import Vue2Filters from 'vue2-filters'
import VeeValidate from 'vee-validate';
import * as directives from './directives';
import VCalendar from 'v-calendar';
import 'v-calendar/lib/v-calendar.min.css';

Vue.use(VeeValidate);
Vue.use(Vue2Filters);


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
