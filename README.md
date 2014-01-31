# PyPhi
## Python for Scientific Computing on Intel's Xeon Phi MIC Platform

*Compiled by Brenton Partridge, Harvard University*

*All utilities released under Creative Commons CC-BY.*

This repository contains tools for cross-compiling a Python interpreter
and the Numpy and Scipy libraries for an Intel Xeon Phi coprocessor,
allowing you to run Python code using those libraries as a native
executable on the coprocessor.

Based on [Emilio Castillo Villar's work](http://software.intel.com/en-us/forums/topic/392736) to cross-compile Python.

Numpy was never designed to be cross-compiled for anything, much less
a system without a compiler of its own, so much effort was placed into
re-engineering it to use the "MIC" architecture and the relevant Intel MKL
libraries. Internal testing code for Numpy and Scipy also works.

After downloading the Makefile into a folder and running `make`,
that folder will then contain `python/_install` which will be the
`$PYTHONHOME` whose `bin/python` can be executed on the Phi.
See `mic_task.sh` for a usage example.

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

