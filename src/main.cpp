#include "main.h"

Array getDeviceList(const CallbackInfo& info) {

	Env env = info.Env();

	Array array = Array::New(env, 0);

	struct wdi_device_info *device, *list;

	if (wdi_create_list(&list, NULL) == WDI_SUCCESS) {

		for (device = list; device != NULL; device = device->next) {
			printf(
				"Installing driver for USB device: \"%s\" (%04X:%04X)\n",
				device->desc,
				device->vid,
				device->pid
			);
		}

		wdi_destroy_list(list);

	}

	return array;

}

Object init(Env env, Object exports) {

	exports.Set("getDeviceList", Function::New(env, getDeviceList));

	return exports;
}

NODE_API_MODULE(libwdiAddon, init)
