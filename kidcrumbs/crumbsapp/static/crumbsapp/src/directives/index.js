import Vue from 'vue';


export const focus = Vue.directive('focus', {
  // When the bound element is inserted into the DOM...
  inserted: function (el) {
    // Focus the element
    el.focus()
  }
})


export const dashHover = Vue.directive('dash-hover',(el,binding) => {
        $(el).addClass('dash-hover');
        el.addEventListener('mouseover', (ev) => {
            ev.currentTarget.style.transform = 'scale(1.1,1.1)';
        });

        el.addEventListener('mouseout', (ev) => {
            ev.currentTarget.style.transform = 'scale(1,1)';
        })
})
