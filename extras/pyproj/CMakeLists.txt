include(${PROJECT_SOURCE_DIR}/tools/cmake/set_up_pybind11.cmake)

set(SRC
  "pyproj.cpp"
)

pybind11_add_module(pyproj ${SRC})
target_link_libraries(pyproj PRIVATE proj::proj)
