# variables
SRC_TE = teaching_evaluation_yw
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : teaching_evaluation

teaching_evaluation : $(SRC_TE).tex
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_TE).tex
	@cp $(CACHE_DIR)/$(SRC_TE).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_TE).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
