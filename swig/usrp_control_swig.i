/* -*- c++ -*- */

#define USRP_CONTROL_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "usrp_control_swig_doc.i"

%{
#include "usrp_control/pdu_to_pmt.h"
%}


%include "usrp_control/pdu_to_pmt.h"
GR_SWIG_BLOCK_MAGIC2(usrp_control, pdu_to_pmt);
