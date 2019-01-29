try:
    # For Run
    from Libraries.DefaultConfig.Config import *
    pass
except ImportError:
    # Fro RED Parse
    import sys
    import os as _os
    _path = _os.path.dirname(__file__)
    _path_root = _os.path.join(_path, '../../')
    sys.path.append(_path_root)
    from Libraries.DefaultConfig.Config import *
    pass

PROJECT = 'UC_MIT'
PROJECT_DOC = 'CONFIG PROJECT FOR {}: {}'.format(PROJECT, VERSION)

