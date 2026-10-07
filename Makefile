SNAPSHOT = $(shell grep -Po 'SNAPSHOT=\$$HUNGRYHORACE_HOME/\K.*' .ddiffsrc)
T2S = hungry_horace.t2s

MK = $(SKOOLKIT_HOME)/tools/disassembly.mk
ifeq ($(wildcard $(MK)),)
    $(error $(MK): file not found)
endif
include $(MK)
