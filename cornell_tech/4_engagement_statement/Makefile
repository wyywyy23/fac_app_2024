# variables
SRC_ES = engagement_statement_yw
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : engagement_statement

engagement_statement : $(SRC_ES).tex
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_ES).tex
	@cp $(CACHE_DIR)/$(SRC_ES).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_ES).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
