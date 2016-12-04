from __future__ import absolute_import as _
from __future__ import unicode_literals as _

from pkg_resources import get_distribution as _get_distribution
from pkg_resources import DistributionNotFound as _DistributionNotFound

try:
    __version__ = _get_distribution('pandas_plink').version
except _DistributionNotFound:
    __version__ = 'unknown'

from .read import read_plink

def test():
    import os
    p = __import__('pandas_plink').__path__[0]
    src_path = os.path.abspath(p)
    old_path = os.getcwd()
    os.chdir(src_path)

    try:
        return_code = __import__('pytest').main(['-q'])
    finally:
        os.chdir(old_path)

    if return_code == 0:
        print("Congratulations. All tests have passed!")

    return return_code