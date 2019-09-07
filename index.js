const libwdiAddon = require('./build/Release/libwdiAddon.node');
console.log('addon', libwdiAddon);

const devices = libwdiAddon.getDeviceList();

console.log(JSON.stringify(devices, null, 2));

module.exports = libwdiAddon;
