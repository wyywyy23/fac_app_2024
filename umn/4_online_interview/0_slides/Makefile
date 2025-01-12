SRC_SLIDES    = research_overview
PDF_SLIDES	= $(SRC_SLIDES).pdf
SRC_HANDOUT = research_overview_handout
PDF_HANDOUT = $(SRC_HANDOUT).pdf
STY_DIR = ../../../9_interview/0_slides_common
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf
FIG_DIR = fig
FIG_CONVERT = inkscape --export-type=pdf --export-area-page --export-dpi=1200
PDF_COMPRESS = gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/prepress -dColorImageResolution=600 -dNOPAUSE -dQUIET -dBATCH

FIG1_1_SVG = $(FIG_DIR)/growth-1.svg
FIG1_1_PDF = $(FIG1_1_SVG:.svg=.pdf)
FIG1_SVG = $(FIG_DIR)/growth.svg
FIG1_PDF = $(FIG1_SVG:.svg=.pdf)
FIG2_1_SVG = $(FIG_DIR)/bottleneck-1.svg
FIG2_1_PDF = $(FIG2_1_SVG:.svg=.pdf)
FIG2_SVG = $(FIG_DIR)/bottleneck.svg
FIG2_PDF = $(FIG2_SVG:.svg=.pdf)

.PHONY: all clean clean-cache

all: slides figs

slides: $(PDF_SLIDES) $(PDF_HANDOUT)

$(PDF_SLIDES): figs $(SRC_SLIDES).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_SLIDES).tex
	@cp $(CACHE_DIR)/$(SRC_SLIDES).pdf .

$(PDF_HANDOUT): figs $(SRC_HANDOUT).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_HANDOUT).tex
	@cp $(CACHE_DIR)/$(SRC_HANDOUT).pdf .

figs: $(FIG1_1_PDF) $(FIG1_PDF) $(FIG2_1_PDF) $(FIG2_PDF)

$(FIG1_1_PDF): $(FIG1_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_1_PDF) $(FIG1_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_1_PDF))_compressed.pdf $(FIG1_1_PDF)

$(FIG1_PDF): $(FIG1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_PDF) $(FIG1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_PDF))_compressed.pdf $(FIG1_PDF)

$(FIG2_1_PDF): $(FIG2_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG2_1_PDF) $(FIG2_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG2_1_PDF))_compressed.pdf $(FIG2_1_PDF)

$(FIG2_PDF): $(FIG2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG2_PDF) $(FIG2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG2_PDF))_compressed.pdf $(FIG2_PDF)

clean: clean-cache

clean : clean-cache
	@$(RM) $(SRC_SLIDES).pdf
	@$(RM) *.sty

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log