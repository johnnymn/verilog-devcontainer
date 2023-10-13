.PHONY:	test

SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/example.v
TOPLEVEL = example
MODULE = test_example

include $(shell cocotb-config --makefiles)/Makefile.sim
