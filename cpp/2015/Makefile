CXX := g++
CXXFLAGS := -std=c++11 -O2 -Wall -Wextra -pedantic
LDLIBS := -lcrypto

BUILD_DIR := build
ALL_TARGETS := $(BUILD_DIR)/01 $(BUILD_DIR)/02 $(BUILD_DIR)/03 $(BUILD_DIR)/04

.PHONY: all clean 04

all: $(ALL_TARGETS)

04: $(BUILD_DIR)/04

$(BUILD_DIR)/01: 01.cpp common.h
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) 01.cpp -o $(BUILD_DIR)/01

$(BUILD_DIR)/02: 02.cpp common.h
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) 02.cpp -o $(BUILD_DIR)/02

$(BUILD_DIR)/03: 03.cpp common.h
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) 03.cpp -o $(BUILD_DIR)/03

$(BUILD_DIR)/04: 04.cpp common.h
	mkdir -p $(BUILD_DIR)
	$(CXX) $(CXXFLAGS) 04.cpp -o $(BUILD_DIR)/04 $(LDLIBS)

clean:
	rm -f $(ALL_TARGETS)
