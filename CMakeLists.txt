cmake_minimum_required(VERSION 3.0)

project(cpp_lib)

#Using c90 standard
set (CMAKE_CXX_STANDARD 11)

#Include the current directory as search path
set(CMAKE_INCLUDE_CURRENT_DIR ON)

SET_PROPERTY(CACHE CMAKE_BUILD_TYPE PROPERTY STRINGS "Debug" "Release")

message(STATUS "Compiler identification: ${CMAKE_CXX_COMPILER_ID}")

get_filename_component(CXX_COMPILER_PATH ${CMAKE_CXX_COMPILER} DIRECTORY)

set(SOURCES_LIB
    cpp_lib.cpp
    cpp_lib.h
    )

add_library(${PROJECT_NAME} SHARED ${SOURCES_LIB})

set(SOURCES_EXEC
    main.cpp
    )

#Add the executable
add_executable("${PROJECT_NAME}_call" ${SOURCES_EXEC})
target_link_libraries("${PROJECT_NAME}_call" ${PROJECT_NAME})

message(STATUS "Compiler path: ${CXX_COMPILER_PATH}")

file(COPY "${CXX_COMPILER_PATH}/libstdc++-6.dll" DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY "${CXX_COMPILER_PATH}/libgcc_s_seh-1.dll" DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
file(COPY "${CXX_COMPILER_PATH}/libwinpthread-1.dll" DESTINATION ${CMAKE_CURRENT_BINARY_DIR})
