#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Alex -*-

class ServerInfo(object):

    def __init__(self):
        self.local_os = ''
        self.local_kernel = ''
        self.local_distributive = ''
        self.local_hostname = ''
        self.local_architecture = ''

    def to_string(self):
        all_data = "Operation System: " + str(self.local_os) + "\n" + "Hostname: " + str(self.local_hostname) + "\n" + "Kernel: " + str(self.local_kernel) + "\n" + "Distributive: " + str(self.local_distributive) + "\n" + "Architecture: " + str(self.local_architecture) + "\n"
        return str(all_data)

    def print_data(self):
        print "Operation System: " + str(self.local_os)
        print "Hostname: " + str(self.local_hostname)
        print "Kernel: " + str(self.local_kernel)
        print "Distributive: " + str(self.local_distributive)
        print "Architecture: " + str(self.local_architecture) + "\n"
