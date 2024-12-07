# variables
SRC_LS = leadership_statement_yw
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : leadership_statement

leadership_statement : $(SRC_LS).tex
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_LS).tex
	@cp $(CACHE_DIR)/$(SRC_LS).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_LS).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
