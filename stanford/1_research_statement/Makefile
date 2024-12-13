# variables
SRC_RS = research_statement_yw
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : research_statement

research_statement : $(SRC_RS).tex
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_RS).tex
	@cp $(CACHE_DIR)/$(SRC_RS).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_RS).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
