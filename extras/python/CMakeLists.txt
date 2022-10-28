find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
include(${PROJECT_SOURCE_DIR}/tools/cmake/set_up_pybind11.cmake)

set(SRC
  "pyproj.cpp"
)

pybind11_add_module(cpplib ${SRC})
target_link_libraries(cpplib PUBLIC proj::proj)
