all: book_main.pdf

book_main.pdf: book_main.tex rel_preamble.tex rel_framework_*.tex rel_chapter_*.tex
	pdflatex -interaction=nonstopmode book_main.tex
	pdflatex -interaction=nonstopmode book_main.tex

clean:
	rm -f *.aux *.log *.toc *.out
