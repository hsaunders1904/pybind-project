find_program(ClangTidy_EXECUTABLE NAMES clang-tidy REQUIRED)

# The configuration comes from the .clang-tidy file in the project root
# Only analyze files in src/ as tests throw up lots of gtest macro warnings:
# https://github.com/google/googletest/issues/2442
add_custom_target(clang-tidy
  COMMAND ${ClangTidy_EXECUTABLE}
    ${PROJECT_SOURCE_DIR}/src/**/*.cpp ${PROJECT_SOURCE_DIR}/extras/**/*.cpp
    -p ${PROJECT_BINARY_DIR}
    -header-filter=${PROJECT_SOURCE_DIR}/.*\.h
  WORKING_DIRECTORY ${PROJECT_SOURCE_DIR}
  COMMENT "Running clang-tidy"
  USES_TERMINAL
)
