
quadruped={
	'controllers': {
        'my_dxl_controller': {
            'sync_read': False,
            'attached_motors': ['left_front', 'left_back', 'right_back', 'right_front'],
            'port': 'auto'
        }
    },
    'motorgroups': {
        'left_front' : ['m1',  'm2',  'm3'],
        'left_back'  : ['m4',  'm5',  'm6'],
        'right_back' : ['m7',  'm8',  'm9'],
        'right_front': ['m10', 'm11', 'm12']
    },

    motors : {
    	'm1' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 1,
            'angle_limit': [-45.0, 45.0],
            'offset': 0.0
    	},

    	'm2' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 2,
            'angle_limit': [-8.0, 190.0],
            'offset': -90.0
    	},

    	'm3' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 3,
            'angle_limit': [-150.0, 30.0],
            'offset': 60.0
    	},

    	'm4' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 4,
            'angle_limit': [-45.0, 45.0],
            'offset': 0.0
    	},

    	'm5' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 5,
            'angle_limit': [-8.0, 190.0],
            'offset': -90.0
    	},

    	'm6' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 6,
            'angle_limit': [-150.0, 30.0],
            'offset': 60.0
    	},

    	'm7' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 7,
            'angle_limit': [-45.0, 45.0],
            'offset': 0.0
    	},

    	'm8' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 8,
            'angle_limit': [-8.0, 190.0],
            'offset': -90.0
    	},

    	'm9' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 9,
            'angle_limit': [-150.0, 30.0],
            'offset': 60.0
    	},

    	'm10' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 10,
            'angle_limit': [-45.0, 45.0],
            'offset': 0.0
    	},

    	'm11' : {
    		'orientation': 'indirect',
            'type': 'AX-12',
            'id': 11,
            'angle_limit': [-8.0, 190.0],
            'offset': -90.0
    	},

    	'm12' : {
    		'orientation': 'direct',
            'type': 'AX-12',
            'id': 12,
            'angle_limit': [-150.0, 30.0],
            'offset': 60.0
    	},
    }
}