schema = {
    'ifsc':{
        'type':'string',
        'unique':True
    },
    'bank_name':{
        'type':'string'
    },
    'branch':{
        'type':'string'
    },
    'address':{
        'type':'string'
    },
    'city':{
        'type':'string'
    },
    'district':{
        'type':'string'
    },
    'state':{
        'type':'string'
    },
}
bank_details ={
    'url':'bank_branches/<regex("[\w]+"):city>/<regex("[\w]+"):bank_name>/branch',
    'schema':schema
}
DOMAIN = {'bank_branches': {
    'additional_lookup': {
        'url': 'regex("((?:[a-zA-Z]+[0-9]|[0-9]+[a-zA-Z])[a-zA-Z0-9]*)")',
        'field': 'ifsc',
    },
    'schema':schema,
    'resource_methods': ['GET'],
    },
    'branches': bank_details
}

MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'bank_det'
RESOURCE_METHODS = ['GET']