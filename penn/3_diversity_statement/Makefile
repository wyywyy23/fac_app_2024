# variables
SRC_DS = diversity_statement_yw
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : diversity_statement

diversity_statement : $(SRC_DS).tex
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_DS).tex
	@cp $(CACHE_DIR)/$(SRC_DS).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_DS).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
