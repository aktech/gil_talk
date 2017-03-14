from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "My hello app",
    ext_modules = cythonize('gil.pyx'),  # accepts a glob pattern
)
