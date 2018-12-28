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


export const iconButton = Vue.directive('icon-button',(el,binding) => {
    $(el).addClass('icon-button');
    if(_.includes(_.keys(binding.modifiers), 'border'))
            $(el).addClass('border border-width-2 border_4');
})
