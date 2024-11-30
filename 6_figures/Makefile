# variables
RM = rm -rf
FIG_CONVERT_PDF = inkscape --export-type=pdf --export-area-page --export-dpi=1200
FIG_CONVERT_PNG = inkscape --export-type=png --export-area-page --export-dpi=600
PDF_COMPRESS = gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/prepress -dColorImageResolution=600 -dNOPAUSE -dQUIET -dBATCH

RS_FIG1_SVG = rs_fig_1_empho.svg
RS_FIG1_PDF = $(RS_FIG1_SVG:.svg=.pdf)
RS_FIG1_PNG = $(RS_FIG1_SVG:.svg=.png)
RS_FIG2_SVG = rs_fig_2_3dpho.svg
RS_FIG2_PDF = $(RS_FIG2_SVG:.svg=.pdf)
RS_FIG2_PNG = $(RS_FIG2_SVG:.svg=.png)
RS_FIG3_SVG = rs_fig_3_comppho.svg
RS_FIG3_PDF = $(RS_FIG3_SVG:.svg=.pdf)
RS_FIG3_PNG = $(RS_FIG3_SVG:.svg=.png)

# rules
.PHONY : all clean clean-cache

all : figs

figs : $(RS_FIG1_PDF) $(RS_FIG1_PNG) $(RS_FIG2_PDF) $(RS_FIG2_PNG) $(RS_FIG3_PDF) $(RS_FIG3_PNG)

$(RS_FIG1_PDF) : $(RS_FIG1_SVG)
	$(FIG_CONVERT_PDF) --export-filename=$(RS_FIG1_PDF) $(RS_FIG1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(RS_FIG1_PDF))_compressed.pdf $(RS_FIG1_PDF)

$(RS_FIG1_PNG) : $(RS_FIG1_SVG)
	$(FIG_CONVERT_PNG) --export-filename=$(RS_FIG1_PNG) $(RS_FIG1_SVG)

$(RS_FIG2_PDF) : $(RS_FIG2_SVG)
	$(FIG_CONVERT_PDF) --export-filename=$(RS_FIG2_PDF) $(RS_FIG2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(RS_FIG2_PDF))_compressed.pdf $(RS_FIG2_PDF)

$(RS_FIG2_PNG) : $(RS_FIG2_SVG)
	$(FIG_CONVERT_PNG) --export-filename=$(RS_FIG2_PNG) $(RS_FIG2_SVG)

$(RS_FIG3_PDF) : $(RS_FIG3_SVG)
	$(FIG_CONVERT_PDF) --export-filename=$(RS_FIG3_PDF) $(RS_FIG3_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(RS_FIG3_PDF))_compressed.pdf $(RS_FIG3_PDF)

$(RS_FIG3_PNG) : $(RS_FIG3_SVG)
	$(FIG_CONVERT_PNG) --export-filename=$(RS_FIG3_PNG) $(RS_FIG3_SVG)

clean : clean-cache
	@$(RM) *.pdf

clean-cache :
	@$(RM) *_compressed.pdf *.png