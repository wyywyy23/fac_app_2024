# variables
REFL_SRC = online_interview_reflection
PREP_SRC = online_interview_preparation
INTV_DEP = online_interview.json json2tex.py
CACHE_DIR = .cache
COMPILE = latexmk 
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : intv_refl intv_prep

intv_refl : $(INTV_DEP)
	$(COMPILE) -lualatex -g -outdir=$(CACHE_DIR) --shell-escape $(REFL_SRC).tex
	@cp $(CACHE_DIR)/$(REFL_SRC).pdf .

intv_prep : $(INTV_DEP)
	$(COMPILE) -lualatex -g -outdir=$(CACHE_DIR) --shell-escape $(PREP_SRC).tex
	@cp $(CACHE_DIR)/$(PREP_SRC).pdf .

clean : clean-cache
	@$(RM) $(REFL_SRC).pdf
	@$(RM) $(PREP_SRC).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
