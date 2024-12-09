SUBDIRS := $(wildcard */)

.PHONY: all $(SUBDIRS) clean clean-cache

all: $(SUBDIRS)

$(SUBDIRS):
	@if [ -f $@/Makefile ]; then $(MAKE) -C $@; fi

clean:
	@for dir in $(SUBDIRS); do \
		if [ -f $$dir/Makefile ]; then $(MAKE) -C $$dir clean; fi; \
	done

clean-cache:
	@for dir in $(SUBDIRS); do \
		if [ -f $$dir/Makefile ]; then $(MAKE) -C $$dir clean-cache; fi; \
	done