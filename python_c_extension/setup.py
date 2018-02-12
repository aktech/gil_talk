from distutils.core import setup, Extension

module1 = Extension('extension_module',
                    sources = ['python_c_extension/extension_module.c'])

setup (name = 'Extension Module',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
