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
include biClique/CMakeFiles/pivotAndPath.dir/depend.make

# Include the progress variables for this target.
include biClique/CMakeFiles/pivotAndPath.dir/progress.make

# Include the compile flags for this target's objects.
include biClique/CMakeFiles/pivotAndPath.dir/flags.make

biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o: biClique/CMakeFiles/pivotAndPath.dir/flags.make
biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o: biClique/pivotAndPath.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/yexw/biclique/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o"
	cd /home/yexw/biclique/src/biClique && g++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o -c /home/yexw/biclique/src/biClique/pivotAndPath.cpp

biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.i"
	cd /home/yexw/biclique/src/biClique && g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/yexw/biclique/src/biClique/pivotAndPath.cpp > CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.i

biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.s"
	cd /home/yexw/biclique/src/biClique && g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/yexw/biclique/src/biClique/pivotAndPath.cpp -o CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.s

biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.requires:

.PHONY : biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.requires

biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.provides: biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.requires
	$(MAKE) -f biClique/CMakeFiles/pivotAndPath.dir/build.make biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.provides.build
.PHONY : biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.provides

biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.provides.build: biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o


# Object files for target pivotAndPath
pivotAndPath_OBJECTS = \
"CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o"

# External object files for target pivotAndPath
pivotAndPath_EXTERNAL_OBJECTS =

biClique/libpivotAndPath.a: biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o
biClique/libpivotAndPath.a: biClique/CMakeFiles/pivotAndPath.dir/build.make
biClique/libpivotAndPath.a: biClique/CMakeFiles/pivotAndPath.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/yexw/biclique/src/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX static library libpivotAndPath.a"
	cd /home/yexw/biclique/src/biClique && $(CMAKE_COMMAND) -P CMakeFiles/pivotAndPath.dir/cmake_clean_target.cmake
	cd /home/yexw/biclique/src/biClique && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pivotAndPath.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
biClique/CMakeFiles/pivotAndPath.dir/build: biClique/libpivotAndPath.a

.PHONY : biClique/CMakeFiles/pivotAndPath.dir/build

biClique/CMakeFiles/pivotAndPath.dir/requires: biClique/CMakeFiles/pivotAndPath.dir/pivotAndPath.cpp.o.requires

.PHONY : biClique/CMakeFiles/pivotAndPath.dir/requires

biClique/CMakeFiles/pivotAndPath.dir/clean:
	cd /home/yexw/biclique/src/biClique && $(CMAKE_COMMAND) -P CMakeFiles/pivotAndPath.dir/cmake_clean.cmake
.PHONY : biClique/CMakeFiles/pivotAndPath.dir/clean

biClique/CMakeFiles/pivotAndPath.dir/depend:
	cd /home/yexw/biclique/src && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/yexw/biclique/src /home/yexw/biclique/src/biClique /home/yexw/biclique/src /home/yexw/biclique/src/biClique /home/yexw/biclique/src/biClique/CMakeFiles/pivotAndPath.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : biClique/CMakeFiles/pivotAndPath.dir/depend

