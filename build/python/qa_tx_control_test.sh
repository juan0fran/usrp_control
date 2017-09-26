#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/cubecat/gr-usrp_control/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/cubecat/gr-usrp_control/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/cubecat/gr-usrp_control/build/swig:$PYTHONPATH
/usr/bin/python2 /home/cubecat/gr-usrp_control/python/qa_tx_control.py 
