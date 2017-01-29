# -*- coding: utf-8 -*-
# 3DES vault

from __future__ import absolute_import
from ansible import errors

from ansible.compat.six import iteritems
from ansible.module_utils._text import to_native, to_text

from subprocess import Popen, PIPE

import os,hashlib
from Crypto.Cipher import DES3
import base64, string, random

BS    = 8
pad   = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS) 
unpad = lambda s: s[0:-ord(s[-1])]

# Return a random string using a given seed
def random_key(seed, length = 24, string_class = string.ascii_lowercase + string.ascii_uppercase + string.digits):
    random.seed(seed)
    password = ''.join([random.choice(string_class) for i in range(length)])
    return password

def des3_vault(a, key):
    des = DES3.new(key, DES3.MODE_ECB)
    return base64.b64encode(des.encrypt(pad(to_native(a))))

def des3_unvault(a, key):
    des = DES3.new(key, DES3.MODE_ECB)
    return to_text(unpad(des.decrypt(base64.b64decode(a))))

class FilterModule(object):
    '''Return 3DES filters'''

    def filters(self):
        return {
            'des3_vault'       : des3_vault,
            'des3_unvault'     : des3_unvault,
            'random_key'       : random_key,
        }
