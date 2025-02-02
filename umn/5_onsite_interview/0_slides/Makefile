SRC_SLIDES    = seminar_yw
PDF_SLIDES	= $(SRC_SLIDES).pdf
SRC_HANDOUT = seminar_yw_handout
PDF_HANDOUT = $(SRC_HANDOUT).pdf
SRC_NOTES = seminar_yw_notes
PDF_NOTES = $(SRC_NOTES).pdf
SRC_FULL = seminar_yw_full
PDF_FULL = $(SRC_FULL).pdf
STY_DIR = ../../../9_interview/0_slides_common
COMPILE = latexmk 
CACHE_DIR = .cache
RM = rm -rf
FIG_DIR = fig
FIG_CONVERT = inkscape --export-type=pdf --export-area-page --export-dpi=1200
PDF_COMPRESS = gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/prepress -dColorImageResolution=600 -dNOPAUSE -dQUIET -dBATCH

FIG1_1_SVG = $(FIG_DIR)/bw_taper-1.svg
FIG1_1_PDF = $(FIG1_1_SVG:.svg=.pdf)
FIG1_2_SVG = $(FIG_DIR)/bw_taper-2.svg
FIG1_2_PDF = $(FIG1_2_SVG:.svg=.pdf)
FIG1_3_SVG = $(FIG_DIR)/bw_taper-3.svg
FIG1_3_PDF = $(FIG1_3_SVG:.svg=.pdf)
FIG1_4_SVG = $(FIG_DIR)/bw_taper-4.svg
FIG1_4_PDF = $(FIG1_4_SVG:.svg=.pdf)
FIG1_5_SVG = $(FIG_DIR)/bw_taper-5.svg
FIG1_5_PDF = $(FIG1_5_SVG:.svg=.pdf)
FIG2_1_SVG = $(FIG_DIR)/model_growth-1.svg
FIG2_1_PDF = $(FIG2_1_SVG:.svg=.pdf)
FIG2_2_SVG = $(FIG_DIR)/model_growth-2.svg
FIG2_2_PDF = $(FIG2_2_SVG:.svg=.pdf)
FIG2_3_SVG = $(FIG_DIR)/model_growth-3.svg
FIG2_3_PDF = $(FIG2_3_SVG:.svg=.pdf)
FIG3_1_SVG = $(FIG_DIR)/energy_growth-1.svg
FIG3_1_PDF = $(FIG3_1_SVG:.svg=.pdf)
FIG3_2_SVG = $(FIG_DIR)/energy_growth-2.svg
FIG3_2_PDF = $(FIG3_2_SVG:.svg=.pdf)
FIG3_3_SVG = $(FIG_DIR)/energy_growth-3.svg
FIG3_3_PDF = $(FIG3_3_SVG:.svg=.pdf)
FIG3_4_SVG = $(FIG_DIR)/energy_growth-4.svg
FIG3_4_PDF = $(FIG3_4_SVG:.svg=.pdf)
FIG4_1_SVG = $(FIG_DIR)/cpo-1.svg
FIG4_1_PDF = $(FIG4_1_SVG:.svg=.pdf)
FIG4_2_SVG = $(FIG_DIR)/cpo-2.svg
FIG4_2_PDF = $(FIG4_2_SVG:.svg=.pdf)
FIG5_1_SVG = $(FIG_DIR)/fom-1.svg
FIG5_1_PDF = $(FIG5_1_SVG:.svg=.pdf)
FIG5_2_SVG = $(FIG_DIR)/fom-2.svg
FIG5_2_PDF = $(FIG5_2_SVG:.svg=.pdf)
FIG5_3_SVG = $(FIG_DIR)/fom-3.svg
FIG5_3_PDF = $(FIG5_3_SVG:.svg=.pdf)
FIG5_4_SVG = $(FIG_DIR)/fom-4.svg
FIG5_4_PDF = $(FIG5_4_SVG:.svg=.pdf)

.PHONY: all clean clean-cache

all: slides figs

slides: $(PDF_SLIDES) $(PDF_HANDOUT) $(PDF_NOTES) $(PDF_FULL)

$(PDF_SLIDES): figs $(SRC_SLIDES).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_SLIDES).tex
	@cp $(CACHE_DIR)/$(SRC_SLIDES).pdf .

$(PDF_HANDOUT): figs $(SRC_HANDOUT).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_HANDOUT).tex
	@cp $(CACHE_DIR)/$(SRC_HANDOUT).pdf .

$(PDF_NOTES): figs $(SRC_NOTES).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_NOTES).tex
	@cp $(CACHE_DIR)/$(SRC_NOTES).pdf .

$(PDF_FULL): figs $(SRC_FULL).tex
	@cp $(STY_DIR)/*.sty .
	$(COMPILE) -lualatex -outdir=$(CACHE_DIR) --shell-escape $(SRC_FULL).tex
	@cp $(CACHE_DIR)/$(SRC_FULL).pdf .

figs: $(FIG1_1_PDF) $(FIG1_2_PDF) $(FIG1_3_PDF) $(FIG1_4_PDF) $(FIG1_5_PDF) $(FIG2_1_PDF) $(FIG2_2_PDF) $(FIG2_3_PDF) $(FIG3_1_PDF) $(FIG3_2_PDF) $(FIG3_3_PDF) $(FIG3_4_PDF) $(FIG4_1_PDF) $(FIG4_2_PDF) $(FIG5_1_PDF) $(FIG5_2_PDF) $(FIG5_3_PDF) $(FIG5_4_PDF)

$(FIG1_1_PDF): $(FIG1_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_1_PDF) $(FIG1_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_1_PDF))_compressed.pdf $(FIG1_1_PDF)

$(FIG1_2_PDF): $(FIG1_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_2_PDF) $(FIG1_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_2_PDF))_compressed.pdf $(FIG1_2_PDF)

$(FIG1_3_PDF): $(FIG1_3_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_3_PDF) $(FIG1_3_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_3_PDF))_compressed.pdf $(FIG1_3_PDF)

$(FIG1_4_PDF): $(FIG1_4_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_4_PDF) $(FIG1_4_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_4_PDF))_compressed.pdf $(FIG1_4_PDF)

$(FIG1_5_PDF): $(FIG1_5_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG1_5_PDF) $(FIG1_5_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG1_5_PDF))_compressed.pdf $(FIG1_5_PDF)

$(FIG2_1_PDF): $(FIG2_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG2_1_PDF) $(FIG2_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG2_1_PDF))_compressed.pdf $(FIG2_1_PDF)

$(FIG2_2_PDF): $(FIG2_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG2_2_PDF) $(FIG2_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG2_2_PDF))_compressed.pdf $(FIG2_2_PDF)

$(FIG2_3_PDF): $(FIG2_3_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG2_3_PDF) $(FIG2_3_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG2_3_PDF))_compressed.pdf $(FIG2_3_PDF)

$(FIG3_1_PDF): $(FIG3_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG3_1_PDF) $(FIG3_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG3_1_PDF))_compressed.pdf $(FIG3_1_PDF)

$(FIG3_2_PDF): $(FIG3_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG3_2_PDF) $(FIG3_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG3_2_PDF))_compressed.pdf $(FIG3_2_PDF)

$(FIG3_3_PDF): $(FIG3_3_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG3_3_PDF) $(FIG3_3_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG3_3_PDF))_compressed.pdf $(FIG3_3_PDF)

$(FIG3_4_PDF): $(FIG3_4_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG3_4_PDF) $(FIG3_4_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG3_4_PDF))_compressed.pdf $(FIG3_4_PDF)

$(FIG4_1_PDF): $(FIG4_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG4_1_PDF) $(FIG4_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG4_1_PDF))_compressed.pdf $(FIG4_1_PDF)

$(FIG4_2_PDF): $(FIG4_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG4_2_PDF) $(FIG4_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG4_2_PDF))_compressed.pdf $(FIG4_2_PDF)

$(FIG5_1_PDF): $(FIG5_1_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_1_PDF) $(FIG5_1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_1_PDF))_compressed.pdf $(FIG5_1_PDF)

$(FIG5_2_PDF): $(FIG5_2_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_2_PDF) $(FIG5_2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_2_PDF))_compressed.pdf $(FIG5_2_PDF)

$(FIG5_3_PDF): $(FIG5_3_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_3_PDF) $(FIG5_3_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_3_PDF))_compressed.pdf $(FIG5_3_PDF)

$(FIG5_4_PDF): $(FIG5_4_SVG)
	$(FIG_CONVERT) --export-filename=$(FIG5_4_PDF) $(FIG5_4_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(FIG5_4_PDF))_compressed.pdf $(FIG5_4_PDF)

clean: clean-cache

clean : clean-cache
	@$(RM) $(SRC_SLIDES).pdf
	@$(RM) $(SRC_FULL).pdf
	@$(RM) *.sty

clean-cache :
	@$(RM) $(CACHE_DIR)
	@$(RM) indent.log