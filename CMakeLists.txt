cmake_minimum_required(VERSION 3.23)
project(myLogger)

set(CMAKE_CXX_STANDARD 11)

add_library(myLogger Logger.cpp)