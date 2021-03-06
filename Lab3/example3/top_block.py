#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Bipolar NRZ over AWGN channel
# Author: Alexandros-Apostolos A. Boulogeorgos
# Generated: Mon Aug 19 18:58:58 2019
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
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import fec
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from optparse import OptionParser
import sip
import sys


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Bipolar NRZ over AWGN channel")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Bipolar NRZ over AWGN channel")
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

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.seed = seed = 1
        self.scale = scale = 0.5
        self.samp_rate = samp_rate = 32000
        self.noise_amplitude = noise_amplitude = 0.000001
        self.noiseSourceSeed = noiseSourceSeed = 0
        self.mask = mask = 0
        self.degree = degree = 20
        self.constant = constant = -1
        self.K = K = 8

        ##################################################
        # Blocks
        ##################################################
        self._noise_amplitude_range = Range(0.000001, 100, 0.000001, 0.000001, 200)
        self._noise_amplitude_win = RangeWidget(self._noise_amplitude_range, self.set_noise_amplitude, 'Noise amplitude (Vrms)', "counter_slider", float)
        self.top_layout.addWidget(self._noise_amplitude_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	2 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0.disable_legend()
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")
        
        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, -1)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])
        
        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.fec_ber_bf_0 = fec.ber_bf(False, 100, -7.0)
        self.digital_glfsr_source_x_0 = digital.glfsr_source_b(degree, True, mask, seed)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_pack_k_bits_bb_0_0 = blocks.pack_k_bits_bb(K)
        self.blocks_pack_k_bits_bb_0 = blocks.pack_k_bits_bb(K)
        self.blocks_char_to_float_0_0 = blocks.char_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, scale)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((constant, ))
        self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amplitude, noiseSourceSeed)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.blocks_add_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_char_to_float_0_0, 0), (self.qtgui_time_sink_x_0, 1))    
        self.connect((self.blocks_pack_k_bits_bb_0, 0), (self.fec_ber_bf_0, 0))    
        self.connect((self.blocks_pack_k_bits_bb_0_0, 0), (self.fec_ber_bf_0, 1))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_char_to_float_0_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_pack_k_bits_bb_0_0, 0))    
        self.connect((self.digital_glfsr_source_x_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.digital_glfsr_source_x_0, 0), (self.blocks_pack_k_bits_bb_0, 0))    
        self.connect((self.fec_ber_bf_0, 0), (self.qtgui_number_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_seed(self):
        return self.seed

    def set_seed(self, seed):
        self.seed = seed

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        self.blocks_char_to_float_0.set_scale(self.scale)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_noise_amplitude(self):
        return self.noise_amplitude

    def set_noise_amplitude(self, noise_amplitude):
        self.noise_amplitude = noise_amplitude
        self.analog_noise_source_x_0.set_amplitude(self.noise_amplitude)

    def get_noiseSourceSeed(self):
        return self.noiseSourceSeed

    def set_noiseSourceSeed(self, noiseSourceSeed):
        self.noiseSourceSeed = noiseSourceSeed

    def get_mask(self):
        return self.mask

    def set_mask(self, mask):
        self.mask = mask

    def get_degree(self):
        return self.degree

    def set_degree(self, degree):
        self.degree = degree

    def get_constant(self):
        return self.constant

    def set_constant(self, constant):
        self.constant = constant
        self.blocks_add_const_vxx_0.set_k((self.constant, ))

    def get_K(self):
        return self.K

    def set_K(self, K):
        self.K = K


def main(top_block_cls=top_block, options=None):

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
