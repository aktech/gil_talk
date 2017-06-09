from distutils.core import setup, Extension


module1 = Extension('my_module',
	include_dirs = ['/usr/local/include'],
	libraries=['pthread'],
	sources=['my_module.c']
	)

setup(name="exmod",
	  version='1.0',
	  description="My package.",
	  author='Amit Kumar',
	  url="http://iamit.in",
	  ext_modules=[module1]
	  )