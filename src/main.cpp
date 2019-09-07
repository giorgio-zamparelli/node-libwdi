#include "main.h"

Array getDeviceList(const CallbackInfo& info) {

	Env env = info.Env();

	Array array = Array::New(env, 0);

	return array;
}

Object init(Env env, Object exports) {

	exports.Set("getDeviceList", Function::New(env, getDeviceList));

	return exports;
}

NODE_API_MODULE(libwdiAddon, init)
