CV_DIR = 0_curriculum_vitae

.PHONY: all clean clean-cache

all: cv

cv:
	$(MAKE) -C $(CV_DIR)

clean:
	$(MAKE) -C $(CV_DIR) clean

clean-cache:
	$(MAKE) -C $(CV_DIR) clean-cache