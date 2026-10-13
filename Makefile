CC ?= cc
CPPFLAGS += -D_POSIX_C_SOURCE=200809L -Iinclude
CFLAGS ?= -std=c11 -Wall -Wextra -Werror -pedantic

BUILD_DIR := build
TARGET := $(BUILD_DIR)/myls
SAN_TARGET := $(BUILD_DIR)/myls-sanitize
SOURCES := $(wildcard src/*.c)

.PHONY: all test sanitize clean

all: $(TARGET)

$(TARGET): $(SOURCES) Makefile
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) $(SOURCES) -o $@

test: all
	sh tests/run.sh "$(abspath $(TARGET))"

$(SAN_TARGET): $(SOURCES) Makefile
	@mkdir -p $(BUILD_DIR)
	$(CC) $(CPPFLAGS) $(CFLAGS) -g -fsanitize=address,undefined -fno-omit-frame-pointer $(SOURCES) -o $@

sanitize: $(SAN_TARGET)
	sh tests/run.sh "$(abspath $(SAN_TARGET))"

clean:
	rm -rf $(BUILD_DIR)
