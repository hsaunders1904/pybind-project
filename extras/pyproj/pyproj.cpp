#include "proj/proj.h"

#include <pybind11/pybind11.h>

PYBIND11_MODULE(pyproj, m) { m.def("hello", &proj::hello); }
