cmake_minimum_required(VERSION 3.6)

project(run)

SET(CMAKE_CXX_COMPILER "g++")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -march=native -mavx -O3")

set(exName1 "run")

add_subdirectory(biClique)
add_subdirectory(biGraph)
# add_subdirectory(runner)
add_subdirectory(tools)


add_executable(${exName1} runner/run.cpp)

target_link_libraries(${exName1} getArgs)
target_link_libraries(${exName1} biGraph)

target_link_libraries(${exName1} BCListPlusPlus)
target_link_libraries(${exName1} BK)
target_link_libraries(${exName1} rawEdgePivot)
target_link_libraries(${exName1} fastEdgePivot)
target_link_libraries(${exName1} edgePivotSpecificPQ)
target_link_libraries(${exName1} colorPath)
target_link_libraries(${exName1} pivotAndPath)
target_link_libraries(${exName1} turan)
target_link_libraries(${exName1} bcAndPath)


