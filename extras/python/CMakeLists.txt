find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
include(${PROJECT_SOURCE_DIR}/tools/cmake/set_up_pybind11.cmake)

set(SRC
  "pyproj.cpp"
)

set(proj_PYPROJ_LIBRARY_DIR
  ${CMAKE_CURRENT_LIST_DIR}/src/pyproj
  CACHE PATH "Directory to output python library to."
)
pybind11_add_module(_pyproj ${SRC})
target_link_libraries(_pyproj PUBLIC proj::proj)
set_target_properties(_pyproj PROPERTIES
  LIBRARY_OUTPUT_DIRECTORY ${proj_PYPROJ_LIBRARY_DIR}
)

if(proj_BUILD_TESTS)
  add_subdirectory(tests)
endif()
