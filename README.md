VTPlanner
=========

VT Planner module for OCF. VTPlanner is a virtual topology embedding tool meant 
to be used in conjunction with VeRTIGO the OFELIA network slicing layer. VeRTIGO 
allows the user to request slices with an arbitrary network topology. 

## Description

VTPlanner is a command line utility for GNU/Linux OSes developed in Python.

## Installation 

Pre-requisites (information for packagers):

* Python 2.6+ (not tested with Python 3+)
* build-essential (for installation via Pypi and setup.py)
* python-dev (for installation via Pypi)
* python-setuptools (for the installation via setup.py)
* scipy 
* numpy 
* lxml
* Java SE 1.7.0+
* libstdc++

### Matlab Compiler Runtime

Download the MCR from the following address:

http://www.mathworks.it/products/compiler/mcr/

Unzip the MCR:

  unzip MCRInstaller.zip -d MCR
  cd MCR

Run installer:

  ./install -mode silent -agreeToLicense yes

Make sure that locale is set (usually this is variable is not set on headless setups):

  export LC_ALL="en_US.utf8"

### From source

Get the latest version (form GitHub):

    $ rm -rf /tmp/vtplanner-*
    $ wget -O /tmp/vtplanner-last.tgz https://github.com/fp7-ofelia/vtplanner/tarball/master

VTPlanner use a standard GNU style installer (for a Debian like system):

    $ sudo apt-get update
    $ sudo apt-get install python-setuptools build-essential python-dev
    $ cd /tmp
    $ tar zxvf vtplanner-last.tgz
    $ cd vtplanner-*
    $ sudo python setup.py install

## Configuration

No configuration is needed to use VTPlanner.

## Command line options

For help on the command line options run

  ./vtplanner.py --help
  
Options:

  -d, --dryrun
  -a ALGORITHM, --algorithm=ALGORITHM [vtplanner]
  -r REQUEST, --request=REQUEST [request.xml]
  -p PORT, --port=PORT [8080]
  -u USER, --user=USER [fvadmin]
  -n HOST, --name=HOST [localhost]
  -m MCR, --mcr=MCR [/usr/local/MATLAB/MATLAB_Compiler_Runtime/v717]

Note: running with the -d flag just prints the vertigo commands without executing them

## Extending the VTPlanner


This file describes how to add support for a new embedding algorithm to the 
vtplanner. All embedding algorithms are defined as Python modules in the 
"embeddings" package.

The new module must define the "compute_embedding" method with the following 
signature:

compute_embedding(sub_devices, sub_links, virt_devices, virt_links, params):

where:

 - sub_devices is a Python dictionary describing the physical nodes in the 
   substrate network

 - sub_links is a Python dictionary describing the physical links in the 
   substrate network

 - virt_devices is a Python dictionary describing the (virtual) nodes in the 
   virtual network request originated from the user

 - virt_links is a Python dictionary describing the (virtual) links in the 
   virtual network request originated from the user

 - params is a Python dictionary contanining a set of parameters for the 
   embedding algorithm specified by the users. An empty dictionary is a valid 
   value, i.e. defualt values must be handled within the module.

The sub_devieces has the following format:

{
    '1': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '4',
            '11',
            '12',
            '26'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 03'
    },
    '0': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '21',
            '22',
            '24'
        ],
        'DPID': '0f: a0: 00: 24: a8: da: 80: 00'
    },
    '3': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '2',
            '4',
            '1'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 07'
    },
    '2': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '4',
            '11',
            '12',
            '25'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 02'
    },
    '5': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '21',
            '22',
            '23',
            '24'
        ],
        'DPID': '0f: a0: 00: 23: 47: 50: 5b: 80'
    },
    '4': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '2',
            '4',
            '1'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 08'
    },
    '7': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '4',
            '11',
            '12',
            '25',
            '26'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 01'
    },
    '6': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '2',
            '4',
            '1'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 09'
    },
    '8': {
        'type': 'switch',
        'tablesize': 'medium'
        'ports': [
            '3',
            '2',
            '4',
            '1'
        ],
        'DPID': '02: 08: 02: 08: 00: 00: 00: 06'
    }
}

The sub_links has the following format:

{
    '11': {
        'src': '2',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 02',
        'capacity': 10000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'dst': '7',
        'srcPort': '25',
        'dstPort': '25'
    },
    '10': {
        'src': '8',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 06',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'dst': '7',
        'srcPort': '3',
        'dstPort': '3'
    },
    '1': {
        'src': '6',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 09',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 02',
        'dst': '2',
        'srcPort': '1',
        'dstPort': '4'
    },
    '0': {
        'src': '7',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 06',
        'dst': '8',
        'srcPort': '3',
        'dstPort': '3'
    },
    '3': {
        'src': '7',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 07',
        'dst': '3',
        'srcPort': '4',
        'dstPort': '1'
    },
    '2': {
        'src': '1',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 03',
        'capacity': 10000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'dst': '7',
        'srcPort': '26',
        'dstPort': '26'
    },
    '5': {
        'src': '5',
        'srcDPID': '0f: a0: 00: 23: 47: 50: 5b: 80',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 03',
        'dst': '1',
        'srcPort': '21',
        'dstPort': '3'
    },
    '4': {
        'src': '2',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 02',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 09',
        'dst': '6',
        'srcPort': '4',
        'dstPort': '1'
    },
    '7': {
        'src': '0',
        'srcDPID': '0f: a0: 00: 24: a8: da: 80: 00',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 03',
        'dst': '1',
        'srcPort': '21',
        'dstPort': '4'
    },
    '6': {
        'src': '3',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 07',
        'capacity': 1000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'dst': '7',
        'srcPort': '1',
        'dstPort': '4'
    },
    '9': {
        'src': '7',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'capacity': 10000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 02',
        'dst': '2',
        'srcPort': '25',
        'dstPort': '25'
    },
    '8': {
        'src': '7',
        'srcDPID': '02: 08: 02: 08: 00: 00: 00: 01',
        'capacity': 10000,
        'dstDPID': '02: 08: 02: 08: 00: 00: 00: 03',
        'dst': '1',
        'srcPort': '26',
        'dstPort': '26'
    }
}

The virt_nodes has the following format. Notice that for the moment vtplanner
che instantiate only virtual links, i.e. the mebedding of the virtual machines
is not implemented yet. As a result the only valid value for 'type' is 'switch'.
The embedding alrothim shall also consider a set of tags which specify some 
constraints in the selection of nodes. Supported tags:

- switchtype: [hw, sw]
- tablesize: [small, medium, large]
- ofversion: [1.0, 1.1, 1.2]

A node that sprecifies one of the above tags can be mapped only on substrate 
nodes that specify a tag with the same value. Tags are optional in both the
substrate network definition and in the vnrequest network definition.

{
    0: {
        'type': 'switch',
        'switchtype': 'hw',
        'tablesize': 'medium'
    },
    1: {
        'type': 'switch',
        'switchtype': 'hw',
    },
    2: {
        'type': 'switch',
        'switchtype': 'hw',
        'tablesize': 'medium'
    },
    3: {
        'type': 'switch',
        'switchtype': 'hw',
        'tablesize': 'medium'
    }
}

The virt_links has the following format. Notice that capacity is expressed in 
Mb. Capacity is an optional argument, i.e. the user can request a best effort 
link. In this case the algorithm must assume a capacity 0 (zero).

{
    0: {
        'src': 0,
        'dst': 1,
        'capacity': 100
    },
    1: {
        'src': 0,
        'dst': 2,
        'capacity': 100
    },
    2: {
        'src': 0,
        'dst': 3,
        'capacity': 100
    }
}

The dictionary params has the following format. Notice that this structure can
also be empty or could contain general purpose parameters.

{
    'alpha' : 0.5
}



