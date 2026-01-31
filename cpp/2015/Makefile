CXX := g++
CXXFLAGS := -std=c++11 -O2 -Wall -Wextra -pedantic

BUILD_DIR := build
ALL_TARGETS := $(BUILD_DIR)/01 $(BUILD_DIR)/02

.PHONY: all clean

all: $(ALL_TARGETS)

$(BUILD_DIR)/01: 01.cpp common.h
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) 01.cpp -o $(BUILD_DIR)/01

$(BUILD_DIR)/02: 02.cpp common.h
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) 02.cpp -o $(BUILD_DIR)/02

clean:
	rm -f $(ALL_TARGETS)
