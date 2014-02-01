import os, sys

xcprefix = os.environ.get('PYTHONXCPREFIX', None)
if not xcprefix:
  raise Exception("Must specify PYTHONXCPREFIX as an argument to make this work")

xcdirflags = "-I{0}/include -L{0}/lib -L{0}/lib/python2.7 " + \
  "-L{0}/lib/python2.7/site-packages/numpy/core/lib"
xcdirflags = xcdirflags.format(xcprefix)

import setup
print setup.__file__

from numpy.distutils import fcompiler, ccompiler
from numpy.distutils.intelccompiler import IntelCCompiler
from numpy.distutils.fcompiler.intel import IntelFCompiler

class IntelMICCompiler(IntelCCompiler):
  """ A modified Intel compiler compatible with an gcc built Python."""
  compiler_type = 'intelmic'
  cc_exe = 'icc'

  def __init__ (self, verbose=0, dry_run=0, force=0):
    IntelCCompiler.__init__ (self, verbose, dry_run, force)
    compiler = "icc -mmic -mkl -fPIC -fp-model strict -g " + xcdirflags
    self.set_executables(compiler=compiler + ' -shared',
                         compiler_so=compiler,
                         compiler_cxx=compiler,
                         linker_exe=compiler,
                         linker_so=compiler + ' -shared')

# Export it into a module that is __import__ed by np.distutils.ccompiler
import sys, imp
imc = imp.new_module('numpy.distutils.intelmiccompiler')
sys.modules['numpy.distutils.intelmiccompiler'] = imc
imc.IntelMICCompiler = IntelMICCompiler

# print ccompiler.compiler_class # {name: (module_name, module_member_name, desc), ...}
ccompiler.compiler_class['intelmic'] = ('intelmiccompiler', 'IntelMICCompiler', 'Intel Compiler for Xeon Phi')

class IntelMICFCompiler(IntelFCompiler):
  compiler_type = 'intelmic'
  compiler_aliases = ()
  description = "Intel Fortran Cross-Compiler for 64-bit MIC"

  executables = {
    'version_cmd'  : None,          # set by update_executables
    'compiler_f77' : [None, "-72"],
    'compiler_f90' : [None],
    'compiler_fix' : [None, "-FI"],
    'linker_so'    : ["<F90>", "-shared"],
    'archiver'     : ["ar", "-cr"],
    'ranlib'       : ["ranlib"]
    }

  def get_flags(self):
    # for Intel Fortran, -fp-model source is the same as precise without a compiler warning
    return ["-fPIC -shared -mmic -mkl -fp-model strict -g " + xcdirflags]

  def get_flags_linker_so(self):
    return self.get_flags()

  def get_flags_opt(self):
    return ['']

  def get_version(self):
    return "TODO"

fcompiler.load_all_fcompiler_classes()
# print fcompiler.fcompiler_class # {name: (name, klass, desc), ...}
fcompiler.fcompiler_class['intelmic'] = ('intelmic', IntelMICFCompiler, IntelMICFCompiler.description)

setup.setup_package()
