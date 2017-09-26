#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Freq Test
# Generated: Tue Sep 26 18:25:19 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys
import usrp_control


class freq_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Freq Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Freq Test")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "freq_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.tx_control = tx_control = 0
        self.freq_tx = freq_tx = int(434e6)
        self.freq_rx = freq_rx = int(433e6)
        self.variable_qtgui_label_1_0 = variable_qtgui_label_1_0 = tx_control
        self.variable_qtgui_label_1 = variable_qtgui_label_1 = freq_tx
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = freq_rx
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        self._variable_qtgui_label_1_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_1_0_formatter = None
        else:
          self._variable_qtgui_label_1_0_formatter = lambda x: x
        
        self._variable_qtgui_label_1_0_tool_bar.addWidget(Qt.QLabel("TX Control"+": "))
        self._variable_qtgui_label_1_0_label = Qt.QLabel(str(self._variable_qtgui_label_1_0_formatter(self.variable_qtgui_label_1_0)))
        self._variable_qtgui_label_1_0_tool_bar.addWidget(self._variable_qtgui_label_1_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_1_0_tool_bar)
          
        self._variable_qtgui_label_1_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_1_formatter = None
        else:
          self._variable_qtgui_label_1_formatter = lambda x: x
        
        self._variable_qtgui_label_1_tool_bar.addWidget(Qt.QLabel("Frequency TX"+": "))
        self._variable_qtgui_label_1_label = Qt.QLabel(str(self._variable_qtgui_label_1_formatter(self.variable_qtgui_label_1)))
        self._variable_qtgui_label_1_tool_bar.addWidget(self._variable_qtgui_label_1_label)
        self.top_layout.addWidget(self._variable_qtgui_label_1_tool_bar)
          
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)
        
        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x
        
        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel("Frequency RX"+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)
          
        self.USRP_TX_Control_0 = usrp_control.tx_control(self.set_tx_control, "localhost", 53002)
        self.USRP_Doppler_Correction_0 = usrp_control.doppler_correction(self.set_freq_tx, self.set_freq_rx, "localhost", 53001)

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "freq_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_tx_control(self):
        return self.tx_control

    def set_tx_control(self, tx_control):
        self.tx_control = tx_control
        self.set_variable_qtgui_label_1_0(self._variable_qtgui_label_1_0_formatter(self.tx_control))

    def get_freq_tx(self):
        return self.freq_tx

    def set_freq_tx(self, freq_tx):
        self.freq_tx = freq_tx
        self.set_variable_qtgui_label_1(self._variable_qtgui_label_1_formatter(self.freq_tx))

    def get_freq_rx(self):
        return self.freq_rx

    def set_freq_rx(self, freq_rx):
        self.freq_rx = freq_rx
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter(self.freq_rx))

    def get_variable_qtgui_label_1_0(self):
        return self.variable_qtgui_label_1_0

    def set_variable_qtgui_label_1_0(self, variable_qtgui_label_1_0):
        self.variable_qtgui_label_1_0 = variable_qtgui_label_1_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_0_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_1_0)))

    def get_variable_qtgui_label_1(self):
        return self.variable_qtgui_label_1

    def set_variable_qtgui_label_1(self, variable_qtgui_label_1):
        self.variable_qtgui_label_1 = variable_qtgui_label_1
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_1_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_1)))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_0)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate


def main(top_block_cls=freq_test, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
