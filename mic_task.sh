#!/bin/sh
#Designed to run on a MIC card

ulimit -s unlimited
export LD_LIBRARY_PATH=`cat $HOME/MIC_LD_LIBRARY_PATH`
export PYTHONHOME=$HOME/mic/python/_install
export PYTHONPATH=$PYTHONHOME/lib/python2.7:$PYTHONHOME/lib/python2.7/site-packages
export PATH=$PYTHONHOME/bin:$PATH
echo "Number of cores:" `grep -c ^processor /proc/cpuinfo`
# which python
# python -V
# python -m test.test_math
# python -m test.test_ctypes
# echo $PYTHONPATH
# python -c "import sys; print 'sys.maxunicode', sys.maxunicode"
# python -c "import numpy; print 'NumPy version:', numpy.__version__;"
python mic_task.py
# export NPHOME=$PYTHONHOME/lib/python2.7/site-packages/numpy
# python $NPHOME/core/tests/test_arrayprint.py
