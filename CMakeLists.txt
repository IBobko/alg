cmake_minimum_required(VERSION 3.24)
project(untitled)

set(CMAKE_CXX_STANDARD 17)

add_executable(untitled main.cpp ShuntingYardAlgorithm.cpp ShuntingYardAlgorithm.h StateOfState.cpp StateOfState.h Solution224.cpp Solution224.h cpp/hello.cpp cpp/main.c)
