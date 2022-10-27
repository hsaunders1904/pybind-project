cmake_minimum_required(VERSION 3.18)

project(
  proj
  VERSION 0.1.0
  LANGUAGES CXX
)

set(proj_INCLUDE_DIR ${CMAKE_CURRENT_LIST_DIR}/src)

add_subdirectory(src)
add_subdirectory(extras)
