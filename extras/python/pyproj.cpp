#include "proj/version.h"

#include <pybind11/pybind11.h>

PYBIND11_MODULE(cpplib, m) { m.attr("__version__") = proj::VERSION; }
