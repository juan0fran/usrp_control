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

class doppler_runner(threading.Thread):
    def __init__(self, callback_tx, callback_rx, host, port):
        threading.Thread.__init__(self)

        self.callback_rx = callback_rx;
        self.callback_tx = callback_tx;
        self.host = host;
        self.port = port;

    def run(self):
        bind_to = (self.host, self.port)
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(bind_to)

        cur_freq_tx = -1
        cur_freq_rx = -1
        while True:
            data, addr = server.recvfrom(1024)
            if not data:
                break

            if data.startswith('F'):
                rx,tx = data.split(";")
                freq_rx = int(rx[1:].strip())
                if freq_rx != cur_freq_rx:
                    print "[Doppler_Correction]:New frequency RX: %d" % freq_rx
                    self.callback_rx(freq_rx)
                    cur_freq_rx = freq_rx

                freq_tx = int(tx.strip())
                if freq_tx != cur_freq_tx:
                    print "[Doppler_Correction]:New frequency TX: %d" % freq_tx
                    self.callback_tx(freq_tx)
                    cur_freq_tx = freq_tx

        sock.close()

class doppler_correction(gr.sync_block):
    """
    docstring for block doppler_correction
    """
    def __init__(self, callback_tx, callback_rx, host, port):
        gr.sync_block.__init__(self,
            name="doppler_correction",
            in_sig= None,
            out_sig= None)
        doppler_runner(callback_tx, callback_rx, host, port).start()
