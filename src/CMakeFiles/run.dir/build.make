# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/local/bin/cmake

# The command to remove a file.
RM = /usr/local/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/yexw/biclique/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/yexw/biclique/src

# Include any dependencies generated for this target.
include CMakeFiles/run.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/run.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/run.dir/flags.make

CMakeFiles/run.dir/runner/run.cpp.o: CMakeFiles/run.dir/flags.make
CMakeFiles/run.dir/runner/run.cpp.o: runner/run.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/yexw/biclique/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/run.dir/runner/run.cpp.o"
	g++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/run.dir/runner/run.cpp.o -c /home/yexw/biclique/src/runner/run.cpp

CMakeFiles/run.dir/runner/run.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/run.dir/runner/run.cpp.i"
	g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/yexw/biclique/src/runner/run.cpp > CMakeFiles/run.dir/runner/run.cpp.i

CMakeFiles/run.dir/runner/run.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/run.dir/runner/run.cpp.s"
	g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/yexw/biclique/src/runner/run.cpp -o CMakeFiles/run.dir/runner/run.cpp.s

CMakeFiles/run.dir/runner/run.cpp.o.requires:

.PHONY : CMakeFiles/run.dir/runner/run.cpp.o.requires

CMakeFiles/run.dir/runner/run.cpp.o.provides: CMakeFiles/run.dir/runner/run.cpp.o.requires
	$(MAKE) -f CMakeFiles/run.dir/build.make CMakeFiles/run.dir/runner/run.cpp.o.provides.build
.PHONY : CMakeFiles/run.dir/runner/run.cpp.o.provides

CMakeFiles/run.dir/runner/run.cpp.o.provides.build: CMakeFiles/run.dir/runner/run.cpp.o


# Object files for target run
run_OBJECTS = \
"CMakeFiles/run.dir/runner/run.cpp.o"

# External object files for target run
run_EXTERNAL_OBJECTS =

run: CMakeFiles/run.dir/runner/run.cpp.o
run: CMakeFiles/run.dir/build.make
run: biClique/libBCListPlusPlus.a
run: biClique/libBK.a
run: biClique/librawEdgePivot.a
run: biClique/libfastEdgePivot.a
run: biClique/libedgePivotSpecificPQ.a
run: biClique/libcolorPath.a
run: biClique/libpivotAndPath.a
run: CMakeFiles/run.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/yexw/biclique/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable run"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/run.dir/link.txt --verbose=$(VERBOSE)
	/usr/local/bin/cmake -E make_directory ../bin
	/usr/local/bin/cmake -E copy run ../bin/.

# Rule to build all files generated by this target.
CMakeFiles/run.dir/build: run

.PHONY : CMakeFiles/run.dir/build

CMakeFiles/run.dir/requires: CMakeFiles/run.dir/runner/run.cpp.o.requires

.PHONY : CMakeFiles/run.dir/requires

CMakeFiles/run.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/run.dir/cmake_clean.cmake
.PHONY : CMakeFiles/run.dir/clean

CMakeFiles/run.dir/depend:
	cd /home/yexw/biclique/src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/yexw/biclique/src /home/yexw/biclique/src /home/yexw/biclique/src /home/yexw/biclique/src /home/yexw/biclique/src/CMakeFiles/run.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/run.dir/depend

