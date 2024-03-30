import colorama
import inspect
print(type(colorama))
print(inspect.ismodule(colorama))
print(inspect.isfunction(colorama))
print(dir(colorama))
print(hasattr(colorama, "penup"))
print(hasattr(colorama, "colorama"))
print(hasattr(colorama, "__file__"))
print(hasattr(colorama, "__doc__"))
print(hasattr(colorama, "colored"))
print(callable(colorama))