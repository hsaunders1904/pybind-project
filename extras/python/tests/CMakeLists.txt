set(SRC
  "test_version.py"
)

foreach(_test ${SRC})
  add_test(
    NAME python.${_test}
    COMMAND ${Python3_EXECUTABLE} -m pytest ${CMAKE_CURRENT_LIST_DIR}/pyproj/${_test}
  )
  set_tests_properties(python.${_test} PROPERTIES
    ENVIRONMENT_MODIFICATION PYTHONPATH=path_list_prepend:${proj_PYPROJ_LIBRARY_DIR}/..
  )
endforeach()
