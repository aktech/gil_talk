from setuptools import Extension, setup

setup(
    name='Extension Module',
    version="0.2",
    description='Python C Extension module',
    ext_modules=[
        Extension(
            name="extension_module",
            sources=["python_c_extension/extension_module.c"],
        ),
    ]
)
