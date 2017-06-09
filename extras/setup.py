from distutils.core import setup, Extension


module1 = Extension('exmod',
	include_dirs = ['/usr/local/include'],
	libraries=['pthread'],
	sources=['exmodmodule.c']
	)

setup(name="exmod",
	  version='1.0',
	  description="My package.",
	  author='Amit Kumar',
	  url="http://iamit.in",
	  ext_modules=[module1]
	  )