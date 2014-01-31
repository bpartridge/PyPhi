import sys
print 'sys.maxunicode:', sys.maxunicode

import numpy as np

np.seterr(all='ignore')
print "errors:", np.geterr()

# print 'NumPy version:', np.__version__
print np.random.test(verbose=3)
# print np.linalg.test()

print np.log(np.arange(5))

import scipy.stats

print scipy.stats.test(verbose=3)
