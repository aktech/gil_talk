from setuptools import Extension, setup

setup(
    ext_modules=[
        Extension(
            name="python_c_extension.extension_module",
            sources=["src/python_c_extension/extension_module.c"],
        ),
    ]
)
