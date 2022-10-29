set(CODE_COV_REVISION 1b68d17)
file(
  DOWNLOAD
  https://raw.githubusercontent.com/bilke/cmake-modules/${CODE_COV_REVISION}/CodeCoverage.cmake
  ${CMAKE_CURRENT_BINARY_DIR}/CodeCoverage.cmake
)
include(${CMAKE_CURRENT_BINARY_DIR}/CodeCoverage.cmake)

append_coverage_compiler_flags()
setup_target_for_coverage_gcovr_html(
  NAME coverage-html
  EXECUTABLE ctest -E python\..*
  BASE_DIRECTORY ${PROJECT_SOURCE_DIR}/src
)
setup_target_for_coverage_gcovr_xml(
  NAME coverage-xml
  EXECUTABLE ctest -E python\..*
  BASE_DIRECTORY ${PROJECT_SOURCE_DIR}/src
)
