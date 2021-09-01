all: main.pdf
	latexmk -c && xdg-open main.pdf

main.pdf: main.tex 1a.tex 1b.tex
	latexmk -pdf --shell-escape main.tex
