OS := $(shell uname)

extension_module.so: extension_module.c
	@echo "Building extension_module on $(OS)"

ifeq ($(OS),Darwin)
	gcc extension_module.c -I/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7 /Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/config/libpython2.7.a -o extension_module.so -shared
else ifeq ($(OS),Linux)
	gcc extension_module.c
else
	@echo "No rule specified for $(OS)"
endif

clean:
	rm *.so
