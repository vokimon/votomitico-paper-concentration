pandoc -s \
 article.md \
 -o article.pdf \
 --filter pandoc-include \
 --citeproc \
 --from markdown+footnotes+example_lists \
 --pdf-engine=xelatex \
 --variable mainfont="" # --csl=path/to/csl-style.csl 


