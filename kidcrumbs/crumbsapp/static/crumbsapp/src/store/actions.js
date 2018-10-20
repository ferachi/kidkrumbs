import {SET_DEVICE} from './mutation_types';

export const getDevice = ({commit}) => {
    let deviceWidth = document.documentElement.clientWidth,
        deviceHeight = document.documentElement.clientHeight,
        maxDeviceDimension = deviceWidth > deviceHeight ? deviceWidth : deviceHeight,
        deviceDimensions = {mobile:767, tab: 1024},
        device = '';
    if(deviceWidth <= deviceDimensions.mobile){
        // it's a mobile
        device = 'mobile';
    }
    else if (maxDeviceDimension > deviceDimensions.mobile && maxDeviceDimension <= deviceDimensions.tab){
        // it's a tab
        device = 'tab';
    }
    else{
        // it a bigger screen
        device = 'other';
    }
    commit(SET_DEVICE,device);
    return device;
}
