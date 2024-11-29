# variables
RM = rm -rf
FIG_CONVERT = inkscape --export-type=pdf --export-area-page --export-dpi=1200
PDF_COMPRESS = gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dPDFSETTINGS=/prepress -dColorImageResolution=600 -dNOPAUSE -dQUIET -dBATCH

RS_FIG1_SVG = rs_fig_1_empho.svg
RS_FIG1_PDF = $(RS_FIG1_SVG:.svg=.pdf)
RS_FIG2_SVG = rs_fig_2_3dpho.svg
RS_FIG2_PDF = $(RS_FIG2_SVG:.svg=.pdf)

# rules
.PHONY : all clean clean-cache

all : figs

figs : $(RS_FIG1_PDF) $(RS_FIG2_PDF)

$(RS_FIG1_PDF) : $(RS_FIG1_SVG)
	$(FIG_CONVERT) --export-filename=$(RS_FIG1_PDF) $(RS_FIG1_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(RS_FIG1_PDF))_compressed.pdf $(RS_FIG1_PDF)

$(RS_FIG2_PDF) : $(RS_FIG2_SVG)
	$(FIG_CONVERT) --export-filename=$(RS_FIG2_PDF) $(RS_FIG2_SVG)
	$(PDF_COMPRESS) -sOutputFile=$(basename $(RS_FIG2_PDF))_compressed.pdf $(RS_FIG2_PDF)

clean : clean-cache
	@$(RM) *.pdf

clean-cache :
	@$(RM) *_compressed.pdf