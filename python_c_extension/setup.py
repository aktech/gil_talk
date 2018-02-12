from distutils.core import setup, Extension

ext_module = Extension('extension_module',
                       sources=['python_c_extension/extension_module.c'])

setup(name='Extension Module',
      version='1.0',
      description='Python C Extension module',
      ext_modules=[ext_module])
