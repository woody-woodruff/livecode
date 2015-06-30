{
	'includes':
	[
		'../common.gypi',
	],
	
	'targets':
	[
		{
			'target_name': 'libcef',
			'type': 'none',
			
			'dependencies':
			[
				'fetch.gyp:fetch',
			],
			
			'direct_dependent_settings':
			{
				'defines':
				[
					'USING_CEF_SHARED=1',
				],
			},
			
			'conditions':
			[
				[
					'OS == "mac"',
					{
						'link_settings':
						{
							'libraries':
							[
								'lib/libcef/mac/Chromium Embedded Framework.framework',
							],
							
							'xcode_settings':
							{
								'FRAMEWORK_SEARCH_PATHS': '$(SOLUTION_DIR)/prebuilt/lib/mac',
							},
						},
					},
				],
				[
					'OS == "win"',
					{
						'all_dependent_settings':
						{
							'variables':
							{
								# Gyp will only use a recursive xcopy if the path ends with '/'
								'dist_aux_files': [ 'lib/win32/x86/CEF/', ],
							},
						},
					},
				],
				[
					'OS == "linux"',
					{
						'all_dependent_settings':
						{
							'variables':
							{
								'dist_aux_files': [ 'lib/linux/<(target_arch)/CEF/', ],
							},
						},
					},
				],
			],
		},
	],
}
