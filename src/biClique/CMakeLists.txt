include_directories(../biGraph ../tools)

add_library(BCListPlusPlus BCListPlusPlus.h BCListPlusPlus.cpp)
target_link_libraries(BCListPlusPlus biGraph linearSet)

add_library(BK BK.h BK.cpp)
target_link_libraries(BK biGraph linearSet)

add_library(rawEdgePivot rawEdgePivot.h rawEdgePivot.cpp)
target_link_libraries(rawEdgePivot biGraph linearSet)

add_library(fastEdgePivot fastEdgePivot.h fastEdgePivot.cpp)
target_link_libraries(fastEdgePivot biGraph linearSet)

add_library(edgePivotSpecificPQ edgePivotSpecificPQ.h edgePivotSpecificPQ.cpp)
target_link_libraries(edgePivotSpecificPQ biGraph linearSet)

add_library(colorPath colorPath.h colorPath.cpp colorPathAV5.cpp)
target_link_libraries(colorPath biGraph linearSet)

add_library(pivotAndPath pivotAndPath.h pivotAndPath.cpp pivotAndPathSamplev5.cpp)
target_link_libraries(pivotAndPath biGraph linearSet)

add_library(turan turan.h turan.cpp)
target_link_libraries(turan biGraph)

add_library(bcAndPath bcAndPath.h bcAndPath.cpp bcAndPathV5.cpp)
target_link_libraries(bcAndPath biGraph linearSet)