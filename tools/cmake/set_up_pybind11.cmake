include(FetchContent)

set(proj_PYBIND11_TAG v2.10.0 CACHE STRING "Branch or tag of pybind11 to use")
FetchContent_Declare(
  pybind11
  GIT_REPOSITORY https://github.com/pybind/pybind11.git
  GIT_TAG        ${proj_PYBIND11_TAG}
)
FetchContent_MakeAvailable(pybind11)
