all: main.pdf
	latexmk -c && xdg-open main.pdf

main.pdf: main.tex 1a.tex 1b.tex 2a.tex 2b.tex 3a.tex 3b.tex
	latexmk -pdf --shell-escape main.tex
