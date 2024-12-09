# variables
SRC_CL = cover_letter_yw
LH_FONT_DIR = ../../1_letterhead/font
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : cover_letter

cover_letter : $(SRC_CL).tex
	@cp -r $(LH_FONT_DIR) .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(SRC_CL).tex
	@cp $(CACHE_DIR)/$(SRC_CL).pdf .
	
clean : clean-cache
	@$(RM) $(SRC_CL).pdf
	@$(RM) font

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
