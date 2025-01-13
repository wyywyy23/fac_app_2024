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
FIG3_SVG = $(FIG_DIR)/cpo.svg
FIG3_PDF = $(FIG3_SVG:.svg=.pdf)
FIG4_2_SVG = $(FIG_DIR)/dwdm-2.svg
FIG4_2_PDF = $(FIG4_2_SVG:.svg=.pdf)
FIG4_1_SVG = $(FIG_DIR)/dwdm-1.svg
FIG4_1_PDF = $(FIG4_1_SVG:.svg=.pdf)
FIG4_SVG = $(FIG_DIR)/dwdm.svg
FIG4_PDF = $(FIG4_SVG:.svg=.pdf)
FIG5_2_SVG = $(FIG_DIR)/package-2.svg
FIG5_2_PDF = $(FIG5_2_SVG:.svg=.pdf)
FIG5_1_SVG = $(FIG_DIR)/package-1.svg
FIG5_1_PDF = $(FIG5_1_SVG:.svg=.pdf)
FIG5_SVG = $(FIG_DIR)/package.svg
FIG5_PDF = $(FIG5_SVG:.svg=.pdf)

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

figs: $(FIG1_1_PDF) $(FIG1_PDF) $(FIG2_1_PDF) $(FIG2_PDF) $(FIG3_PDF) $(FIG4_2_PDF) $(FIG4_1_PDF) $(FIG4_PDF) $(FIG5_2_PDF) $(FIG5_1_PDF) $(FIG5_PDF)

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

$(FIG3_PDF): $(FIG3_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG3_PDF) $(FIG3_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG3_PDF))_compressed.pdf $(FIG3_PDF)

$(FIG4_2_PDF): $(FIG4_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG4_2_PDF) $(FIG4_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG4_2_PDF))_compressed.pdf $(FIG4_2_PDF)

$(FIG4_1_PDF): $(FIG4_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG4_1_PDF) $(FIG4_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG4_1_PDF))_compressed.pdf $(FIG4_1_PDF)

$(FIG4_PDF): $(FIG4_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG4_PDF) $(FIG4_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG4_PDF))_compressed.pdf $(FIG4_PDF)

$(FIG5_2_PDF): $(FIG5_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_2_PDF) $(FIG5_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_2_PDF))_compressed.pdf $(FIG5_2_PDF)

$(FIG5_1_PDF): $(FIG5_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_1_PDF) $(FIG5_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_1_PDF))_compressed.pdf $(FIG5_1_PDF)

$(FIG5_PDF): $(FIG5_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_PDF) $(FIG5_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_PDF))_compressed.pdf $(FIG5_PDF)

clean: clean-cache

clean : clean-cache
	@$(RM) $(SRC_SLIDES).pdf
	@$(RM) *.sty

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log