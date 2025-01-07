# variables
TEXFILE = online_interview_prep
JSONFILE = ../../9_interview/online_interview.json
PYFILE = ../../9_interview/json2tex.py
CACHE_DIR = .cache
COMPILE = latexmk 
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : intv

intv : $(JSONFILE) $(PYFILE)
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(TEXFILE).tex
	@cp $(CACHE_DIR)/$(TEXFILE).pdf .

clean : clean-cache
	@$(RM) $(TEXFILE).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
