# Current OIDs are tentative and and will change after we finalizes/register a proper parent OID subtree
ROLE_STRUCT = {
    'topics':{
        'subscriber':{
            'mask':'s', # subscribe
            'OID':'1.2.3.4.5.6.7.8.9.1', 
            'allow':{'OID':'1.2.3.4.5.6.7.8.9.1.1'},
            'deny' :{'OID':'1.2.3.4.5.6.7.8.9.1.2'},
        },
        'publisher':{
            'mask':'p', # publish
            'OID':'1.2.3.4.5.6.7.8.9.2', 
            'allow':{'OID':'1.2.3.4.5.6.7.8.9.2.1'},
            'deny' :{'OID':'1.2.3.4.5.6.7.8.9.2.2'},
        },
    },
    'services':{
        'client':{
            'mask':'c', # call
            'OID':'1.2.3.4.5.6.7.8.9.3', 
            'allow':{'OID':'1.2.3.4.5.6.7.8.9.3.1'},
            'deny' :{'OID':'1.2.3.4.5.6.7.8.9.3.2'},
        },
        'server':{
            'mask':'x', # execute
            'OID':'1.2.3.4.5.6.7.8.9.4', 
            'allow':{'OID':'1.2.3.4.5.6.7.8.9.4.1'},
            'deny' :{'OID':'1.2.3.4.5.6.7.8.9.4.2'},
        },
    },
    'parameters':{
        'reader':{
            'mask':'r', # read
            'OID':'1.2.3.4.5.6.7.8.9.5', 
            'allow':{'OID':'1.2.3.4.5.6.7.8.9.5.1'},
            'deny' :{'OID':'1.2.3.4.5.6.7.8.9.5.2'},
        },
        'writer':{
            'mask':'w', # write
            'OID':'1.2.3.4.5.6.7.8.9.6', 
            'allow':{'OID':'1.2.3.4.5.6.7.8.9.6.1'},
            'deny' :{'OID':'1.2.3.4.5.6.7.8.9.6.2'},
        },
    },
}

EXTENSION_MAPPING = {
    'key': '.pem',
    'cert': '.cert',
}


class GraphModes:
    audit = 'audit'
    complain = 'complain'
    enforce = 'enforce'
    train = 'train'

    class __metaclass__(type):
        def __contains__(self, item):
            return hasattr(self, item)

class SecuityModes:
    TLSv1_2 = "TLSv1_2"

    class __metaclass__(type):
        def __contains__(self, item):
            return hasattr(self, item)

class PolicyModes:
    NAMESPACE = "NAMESPACE"
    NONE = "NONE"

    class __metaclass__(type):
        def __contains__(self, item):
            return hasattr(self, item)

class VerifyModes:
    CERT_NONE = "CERT_NONE"
    CERT_OPTIONAL = "CERT_OPTIONAL"
    CERT_REQUIRED = "CERT_REQUIRED"

    class __metaclass__(type):
        def __contains__(self, item):
            return hasattr(self, item)
