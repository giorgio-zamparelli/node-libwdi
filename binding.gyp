{
	'variables': {
		'use_udev%': 1,
	},
	"targets": [
		{
	      "target_name": "libwdi_configuration",
	      "type": "none",
	      "conditions": [
	        [ "OS=='win'", {
	          "actions": [
	            {
	              "action_name": "detect_arch",
	              "message": "Detecting build architecture",
	              "inputs": [],
	              "outputs": [ "<(module_root_dir)/deps/libwdi/build64.h" ],
	              "action": [ "call", "deps/detect-arch.bat", "<(target_arch)" ]
	            },
	            {
	              "action_name": "configure",
	              "message": "Configuring libwdi",
	              "inputs": [],
	              "outputs": [ "<(module_root_dir)/deps/libwdi/msvc/config.h" ],
	              "action": [ "call", "deps/config.bat" ]
	            }
	          ]
	        }]
	      ]
	    },
		{
			"target_name": "libwdiAddon",
			"cflags!": [ "-fno-exceptions" ],
			"cflags_cc!": [ "-fno-exceptions" ],
			"sources": [
				"src/main.cpp"
			],
			'include_dirs': [
				"<!@(node -p \"require('node-addon-api').include\")"
			],
			'libraries': [],
			'dependencies': [
				"<!(node -p \"require('node-addon-api').gyp\")",
				"libwdi.gypi:libwdi"
			],
			'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
		}
	]
}
