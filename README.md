# PyPhi
## Python for Scientific Computing on Intel's Xeon Phi MIC Platform

This repository contains tools for cross-compiling a Python interpreter
and the Numpy and Scipy libraries for an Intel Xeon Phi 
Many Integrated Core (MIC) coprocessor,
allowing you to run Python code using those libraries as parallel native
executables on the coprocessor, communicating and processing
with the full power and expressivity of Python.

Based on [Emilio Castillo Villar's work](http://software.intel.com/en-us/forums/topic/392736)
to cross-compile Python.

Numpy was never designed to be cross-compiled for anything, much less
a system without a compiler of its own, so much effort was placed into
re-engineering it to use the "MIC" architecture and the relevant Intel MKL
libraries. Internal testing code for Numpy and Scipy also works.

After downloading the Makefile into a folder and running `make`
like the following:

    mkdir -p mic
    cd mic
    wget https://raw.github.com/bpartridge/PyPhi/master/Makefile -N && make

that folder `mic` will then contain `python/_install`, which will be the
`$PYTHONHOME` whose `bin/python` can be executed on the Phi, and whose
`lib/python2.7[/site-packages]` should be on `$PYTHONPATH`.
See `mic_task.sh` for a usage example.

Tested on the Babbage cluster at NERSC as part of the
[MANTISSA project](https://www.nersc.gov/assets/HPC-Requirements-for-Science/ASCR2017/Prabhat-Quincey.pdf).

## REQUIREMENTS

- 64-bit Intel system for compiling.

- Recent Python installed on that system;
  tested with the Anaconda distribution.

- Intel Composer XE 2013 SP1 installed with MKL and MPI support in
  `/opt/intel/composer_xe_2013_sp1/`.

- A Xeon Phi coprocessor for testing (not needed for compilation itself.)

## TODO

- Currently, SSE instructions are disabled for Numpy, since they are
  very different on the Phi. This would require a native porting effort
  for such files as `einsum.c.src`.

- MPI such as mpi4py.

- Pip/setuptools for non-native python packages.

- A generic modified version of Pip for native python packages.

## References

- http://software.intel.com/en-us/forums/topic/392736

- http://randomsplat.com/id5-cross-compiling-python-for-embedded-linux.html

- http://www.nersc.gov/users/computational-systems/testbeds/babbage/#toc-anchor-12

- http://www.scipy.org/scipylib/building/linux.html#any-distribution-with-intel-c-compiler-and-mkl

- http://thread.gmane.org/gmane.comp.python.scientific.user/32036/focus=32037

- http://whatschrisdoing.com/blog/2009/10/16/cross-compiling-python-extensions/

## License (for all utilities)

Copyright (c) 2014 Brenton Partridge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

[![Analytics](https://ga-beacon.appspot.com/UA-47697237-1/pyphi/README.md)](https://github.com/igrigorik/ga-beacon?pixel)
