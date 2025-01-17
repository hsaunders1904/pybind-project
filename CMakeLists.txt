cmake_minimum_required(VERSION 3.18)

project(proj
  VERSION 0.1.0
  LANGUAGES CXX
)

option(proj_BUILD_PYTHON "Build python bindings" ON)
option(proj_BUILD_TESTS "Build tests" ON)
option(proj_ENABLE_CLANGTIDY "Add clang-tidy target" OFF)
option(proj_ENABLE_COVERAGE "Add coverage flags to build" OFF)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/tools/cmake)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(proj_INCLUDE_DIR ${CMAKE_CURRENT_LIST_DIR}/src)

if(proj_ENABLE_COVERAGE)
  include(target_coverage)
endif()
if(proj_ENABLE_CLANGTIDY)
  include(target_clang_tidy)
endif()

add_subdirectory(src)
if(proj_BUILD_TESTS)
  enable_testing()
  add_subdirectory(tests)
endif()
add_subdirectory(extras)
