#include "proj/proj.h"

#include <pybind11/pybind11.h>

PYBIND11_MODULE(cpplib, m) { m.def("hello", &proj::hello); }
