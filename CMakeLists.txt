cmake_minimum_required(VERSION 3.16)
project(ci_cd_example CXX)
set(CMAKE_CXX_STANDARD 17)

file(GLOB_RECURSE APP_SRC "src/c++/*.cpp")
add_executable(app ${APP_SRC})