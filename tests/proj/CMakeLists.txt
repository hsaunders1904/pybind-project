set(SRC
  "version.test.cpp"
)

add_executable(test_proj ${SRC})
target_link_libraries(test_proj
  PRIVATE proj::proj
  PRIVATE GTest::gtest_main
)

gtest_discover_tests(test_proj)
