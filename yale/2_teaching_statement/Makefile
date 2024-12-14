# variables
SRC_TS = teaching_statement_yw
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : teaching_statement

teaching_statement : $(SRC_TS).tex
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_TS).tex
	@cp $(CACHE_DIR)/$(SRC_TS).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_TS).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
