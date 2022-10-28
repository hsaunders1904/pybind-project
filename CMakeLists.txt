cmake_minimum_required(VERSION 3.18)

project(proj
  VERSION 0.1.0
  LANGUAGES CXX
)

option(proj_BUILD_PYTHON "Build python bindings" ON)
option(proj_BUILD_TESTS "Build tests" ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(proj_INCLUDE_DIR ${CMAKE_CURRENT_LIST_DIR}/src)

add_subdirectory(src)
if(proj_BUILD_TESTS)
  enable_testing()
  add_subdirectory(tests)
endif()
add_subdirectory(extras)
