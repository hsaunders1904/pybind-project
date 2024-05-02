set(PYBIND11_NEWPYTHON ON)
find_package(pybind11 CONFIG)
if(NOT pybind11_FOUND)
  include(set_up_pybind11)
endif()

set(SRC
  "pyproj.cpp"
)

pybind11_add_module(proj_pyproj ${SRC})
target_link_libraries(proj_pyproj PUBLIC proj::proj)
set_target_properties(proj_pyproj PROPERTIES OUTPUT_NAME _pyproj)
add_library(proj::pyproj ALIAS proj_pyproj)

if(proj_BUILD_TESTS)
  add_subdirectory(tests)
endif()

install(TARGETS proj_pyproj LIBRARY DESTINATION pyproj)
