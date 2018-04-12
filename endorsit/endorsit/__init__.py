import pkgutil

import pkg_resources

try:
    pkg_resources.declare_namespace(__name__)
except ImportError:
    __path__ = pkgutil.extend_path(__path__, __name__)
