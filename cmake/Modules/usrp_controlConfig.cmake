INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_USRP_CONTROL usrp_control)

FIND_PATH(
    USRP_CONTROL_INCLUDE_DIRS
    NAMES usrp_control/api.h
    HINTS $ENV{USRP_CONTROL_DIR}/include
        ${PC_USRP_CONTROL_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    USRP_CONTROL_LIBRARIES
    NAMES gnuradio-usrp_control
    HINTS $ENV{USRP_CONTROL_DIR}/lib
        ${PC_USRP_CONTROL_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(USRP_CONTROL DEFAULT_MSG USRP_CONTROL_LIBRARIES USRP_CONTROL_INCLUDE_DIRS)
MARK_AS_ADVANCED(USRP_CONTROL_LIBRARIES USRP_CONTROL_INCLUDE_DIRS)

