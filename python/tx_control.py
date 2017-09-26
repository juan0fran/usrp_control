#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
#
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

from gnuradio import gr
import numpy
import threading
import time
import socket

class control_runner(threading.Thread):
    def __init__(self, callback, host, port):
        threading.Thread.__init__(self)

        self.callback = callback;
        self.host = host;
        self.port = port;

    def run(self):
        bind_to = (self.host, self.port)
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(bind_to)
        server.listen(0)

        cur_ctrl = 0
        while True:
            print "[TX Control]: Waiting for connection on: %s:%d" % bind_to
            sock, addr = server.accept()
            print "[TX Control]: Connected from: %s:%d" % (addr[0], addr[1])
            while True:
                data = sock.recv(1024)
                if not data:
                    break

                if data.startswith('T'):
                    ctrl = int(data[1:].strip())
                    if ((ctrl != 0) and (ctrl != 1)) :
                        ctrl = 1;
                    if ctrl != cur_ctrl:
                        print "[TX Control]: New CTRL: %d" % ctrl
                        self.callback(ctrl)
                        cur_ctrl = ctrl

            sock.close()
            print "[TX Control]: Disconnected from: %s:%d" % (addr[0], addr[1])

class tx_control(gr.sync_block):
    """
    docstring for block tx_control
    """
    def __init__(self, callback, host, port):
        gr.sync_block.__init__(self,
            name="tx_control",
            in_sig= None,
            out_sig= None)
        control_runner(callback, host, port).start()
