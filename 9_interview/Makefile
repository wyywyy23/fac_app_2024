# variables
TEXFILE = online_interview
JSONFILE = online_interview.json
PYFILE = json2tex.py
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
