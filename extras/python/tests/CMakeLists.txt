set(SRC
  "test_version.py"
)

foreach(_test ${SRC})
  add_test(python.${_test}
    COMMAND ${Python3_EXECUTABLE} -m pytest ${CMAKE_CURRENT_LIST_DIR}/pyproj/${_test}
  )
endforeach()
