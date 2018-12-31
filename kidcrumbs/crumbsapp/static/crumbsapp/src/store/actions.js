import {SET_DEVICE} from './mutation_types';


export const screenSize = ({commit}) => {
    let deviceWidth = document.documentElement.clientWidth,
        deviceHeight = document.documentElement.clientHeight,
        maxDeviceDimension = deviceWidth > deviceHeight ? deviceWidth : deviceHeight,
        device = {width:deviceWidth, height: deviceHeight},
        screens = {xs : 576, sm : 768, md: 992, lg: 1200}
    if(deviceWidth <= screens.xs){
        // it's extra small
        device['screen'] = 'xs';
    }
    else if(deviceWidth <= screens.sm){
        // it's small
        device['screen'] = 'sm';
    }
    else if(deviceWidth <= screens.md){
        // it's medium
        device['screen'] = 'md';
    }
    else if(deviceWidth <= screens.lg){
        // it's large
        device['screen'] = 'lg';
    }
    else{
        // it's an extra large screen
        device['screen'] = 'xl';
    }
    commit(SET_DEVICE,device);
    return device;
}
