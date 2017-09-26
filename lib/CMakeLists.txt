# Copyright 2011,2012 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

########################################################################
# Setup library
########################################################################
include(GrPlatform) #define LIB_SUFFIX

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

list(APPEND usrp_control_sources
)

set(usrp_control_sources "${usrp_control_sources}" PARENT_SCOPE)
if(NOT usrp_control_sources)
	MESSAGE(STATUS "No C++ sources... skipping lib/")
	return()
endif(NOT usrp_control_sources)

add_library(gnuradio-usrp_control SHARED ${usrp_control_sources})
target_link_libraries(gnuradio-usrp_control ${Boost_LIBRARIES} ${GNURADIO_ALL_LIBRARIES})
set_target_properties(gnuradio-usrp_control PROPERTIES DEFINE_SYMBOL "gnuradio_usrp_control_EXPORTS")

if(APPLE)
    set_target_properties(gnuradio-usrp_control PROPERTIES
        INSTALL_NAME_DIR "${CMAKE_INSTALL_PREFIX}/lib"
    )
endif(APPLE)

########################################################################
# Install built library files
########################################################################
install(TARGETS gnuradio-usrp_control
    LIBRARY DESTINATION lib${LIB_SUFFIX} # .so/.dylib file
    ARCHIVE DESTINATION lib${LIB_SUFFIX} # .lib file
    RUNTIME DESTINATION bin              # .dll file
)

########################################################################
# Build and register unit test
########################################################################
include(GrTest)

include_directories(${CPPUNIT_INCLUDE_DIRS})

list(APPEND test_usrp_control_sources
    ${CMAKE_CURRENT_SOURCE_DIR}/test_usrp_control.cc
    ${CMAKE_CURRENT_SOURCE_DIR}/qa_usrp_control.cc
)

add_executable(test-usrp_control ${test_usrp_control_sources})

target_link_libraries(
  test-usrp_control
  ${GNURADIO_RUNTIME_LIBRARIES}
  ${Boost_LIBRARIES}
  ${CPPUNIT_LIBRARIES}
  gnuradio-usrp_control
)

GR_ADD_TEST(test_usrp_control test-usrp_control)
