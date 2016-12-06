from __future__ import print_function

import logging
import os
# import names
# import time
# import socket
# import ssl


import sros_consts as sros_consts

from validators import \
    NameSpaceEngine, \
    NameSpaceMasterAPI, \
    NameSpaceSlaveAPI, \
    NameSpaceTransport

_logger = logging.getLogger('rosgraph.policy')

#########################################################################

class Policy(object):
    # TODO: add security logging stuff here
    def __init__(self, node_id, node_stem, node_name):
        _logger.info("policy init")

        self.node_id = node_id
        self.node_stem = node_stem
        self.node_name = node_name

        self.engine = None
        self.master_api = None
        self.slave_api = None
        self.transport = None

#########################################################################

class NoPolicy(Policy):
    def __init__(self, node_id, node_stem, node_name):
        super(NoPolicy, self).__init__(node_id, node_stem, node_name)
        _logger.info("  rospy.policy.NoPolicy init")

##########################################################################

class NameSpacePolicy(Policy):

    def __init__(self, node_id, node_stem, node_name):
        super(NameSpacePolicy, self).__init__(node_id, node_stem, node_name)
        _logger.info("rospy.policy.NameSpacePolicy init")

        self.engine = NameSpaceEngine(self.node_name, _logger)
        self.master_api = NameSpaceMasterAPI(self.engine, _logger)
        # self.master_api = None
        self.slave_api = NameSpaceSlaveAPI(self.engine, _logger)
        # self.slave_api = None
        self.transport = NameSpaceTransport(self.engine, _logger)
        # self.transport = None

#########################################################################
_policy = None


def init(node_id, node_stem, node_name):
    # print('security.init(%s)' % node_stem)
    global _policy
    if _policy is None:
        _logger.info("choosing policy model...")
        if 'SROS_POLICY' in os.environ:
            if os.environ['SROS_POLICY'] == sros_consts.PolicyModes.NAMESPACE:
                _policy = NameSpacePolicy(node_id, node_stem, node_name)
            elif os.environ['SROS_POLICY'] == sros_consts.PolicyModes.NONE:
                _policy = NoPolicy(node_id, node_stem, node_name)
            else:
                raise ValueError("illegal SROS_POLICY value: [%s]" % os.environ['SROS_POLICY'])
        else:
            _policy = NoPolicy(node_id, node_stem, node_name)


def get():
    if _policy is None:
        import traceback
        traceback.print_stack()
        raise ValueError("woah there partner. policy.init() wasn't called before policy.get()")
    return _policy
