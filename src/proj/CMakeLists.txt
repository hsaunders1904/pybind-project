configure_file("version.h.in" "${CMAKE_CURRENT_LIST_DIR}/version.h")

set(SRC
  "version.cpp"
)
set(HDR
  "version.h"
)

add_library(proj_proj STATIC ${SRC} ${HDR})
target_include_directories(proj_proj PRIVATE ${proj_INCLUDE_DIR})
target_include_directories(proj_proj INTERFACE
  $<BUILD_INTERFACE:${proj_INCLUDE_DIR}>
)
add_library(proj::proj ALIAS proj_proj)
