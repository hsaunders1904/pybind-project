include(FetchContent)

set(proj_GOOGLETEST_TAG release-1.12.1 CACHE STRING "Branch or tag of googletest to use")
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG ${proj_GOOGLETEST_TAG}
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)
