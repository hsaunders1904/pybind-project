#include "proj/version.h"

#include <pybind11/pybind11.h>

PYBIND11_MODULE(_pyproj, m) { m.attr("__version__") = proj::VERSION; }
