cmake_minimum_required(VERSION 3.20)
project(Project C)

set(CMAKE_C_STANDARD 11)


add_executable(Project serial_test.c)
target_link_libraries(Project gmp)
