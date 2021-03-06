#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# VTPlanner OFELIA OCF module
#
# Copyright (C) 2013 Roberto Riggio <roberto.riggio@create-net.org>
#
# VTPlanner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# COPYING file for more details.

__appname__ = 'vtplanner'
__version__ = "1.0.0"
__author__ = "Roberto Riggio <roberto.riggio@create-net.org>"
__licence__ = "LGPL"

# Libraries
#==========

import optparse

from backends.vectl import import_vnrequest
from backends.vectl import import_substrate
from backends.vectl import create_slice

def main():

    p = optparse.OptionParser()
    p.add_option("-a", "--algorithm", dest="algorithm", default="vtplanner")
    p.add_option('-d', '--dryrun', action="store_true", dest="dryrun", default=False)    
    p.add_option('-r', '--request', dest="request", default='request.xml')
    p.add_option("-p", "--port", dest="port", type="int", default="8080")
    p.add_option("-f", "--passwd-file", dest="passwd_file", default="passwd")
    p.add_option("-u", "--user", dest="user", default="fvadmin")
    p.add_option("-n", "--name", dest="host", default="localhost")
    p.add_option("-m", "--mcr", dest="mcr", default="/usr/local/MATLAB/MATLAB_Compiler_Runtime/v717")
    options, _ = p.parse_args()

    embedding = __import__("vtplanner.embedding.%s" % options.algorithm, fromlist=["embedding"])

    # load vn request
    ( virt_devices, virt_links ) = import_vnrequest(options)

    # load substrate
    ( sub_devices, sub_links ) = import_substrate(options)
        
    # compute embedding
    params = { 'mcr' : options.mcr, 'alpha' : 0.5 }
    success = embedding.compute_embedding(sub_devices, sub_links, virt_devices, virt_links, params)
    
    # create_slice
    if success and not options.dryrun:
        create_slice(virt_devices, virt_links, options)

if __name__ == "__main__":
    main()

