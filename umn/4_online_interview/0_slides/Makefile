SRC_SLIDES    = research_overview
STY_DIR = ../../../9_interview/0_slides_common
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

.PHONY: all clean clean-cache

all: slides

slides: $(SRC_SLIDES).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_SLIDES).tex
	@cp $(CACHE_DIR)/$(SRC_SLIDES).pdf .

clean: clean-cache

clean : clean-cache
	@$(RM) $(SRC_SLIDES).pdf
	@$(RM) *.sty

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log