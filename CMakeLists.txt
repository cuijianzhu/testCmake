#项目信息
project(main)

#cmake最低版本要求
cmake_minimum_required(VERSION 2.8.7)

#头文件包含的目录
include_directories(./include)

#添加子目录，在子目录下执行CMakeLists.txt
add_subdirectory(./lib)

#搜索当前目录下的所有源文件.cpp文件，将名称加入变量DIR_SRCS中
aux_source_directory(. DIR_SRCS)
message(${DIR_SRCS})#打印出DIR_SRCS变量的值

#添加可执行文件
add_executable(main ${DIR_SRCS})

#指定链接lib hello
target_link_libraries(main hello)

#设置debug 和 release模式下的编译选项
SET(CMAKE_CXX_FLAGS_DEBUG"$ENV{CXXFLAGS} -O0 -Wall -g -ggdb -std=c++11")
SET(CMAKE_CXX_FLAGS_RELEASE"$ENV{CXXFLAGS} -O3 -Wall -std=c++11")

#设置编译成release模式
SET(CMAKE_BUILD_TYPE "release")

#指定可执行文件的生成路径
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_SOURCE_DIR}/bin)

