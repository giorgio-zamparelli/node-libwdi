{
	'variables': {
		'use_udev%': 1,
	},
	"targets": [{
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
			"<!(node -p \"require('node-addon-api').gyp\")"
		],
		'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ],
	}]
}
