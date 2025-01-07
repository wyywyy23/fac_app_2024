# variables
TCPMT_SRC = t-cpmt
CICC_SRC = cicc
JLT_SRC = jlt
CACHE_DIR = .cache
COMPILE = latexmk 
RM = rm -rf

# rules
.PHONY : all clean clean-cache

all : t-cpmt cicc jlt

t-cpmt :
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(TCPMT_SRC).tex
	@cp $(CACHE_DIR)/$(TCPMT_SRC).pdf .

cicc :
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(CICC_SRC).tex
	@cp $(CACHE_DIR)/$(CICC_SRC).pdf .

jlt :
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) $(JLT_SRC).tex
	@cp $(CACHE_DIR)/$(JLT_SRC).pdf .

clean : clean-cache
	@$(RM) $(TCPMT_SRC).pdf
	@$(RM) $(CICC_SRC).pdf
	@$(RM) $(JLT_SRC).pdf

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log
