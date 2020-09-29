(TeX-add-style-hook
 "Projektplan"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "swedish")))
   (TeX-run-style-hooks
    "latex2e"
    "TDP003mall"
    "TDP003mall10"
    "inputenc"
    "babel"
    "tabularx"
    "enumitem"
    "makecell")
   (TeX-add-symbols
    "version")
   (LaTeX-add-labels
    "table:1"
    "table:2"
    "tabell:3"
    "tabell:4"
    "table:5"
    "table:6"
    "table:7"
    "table:8"))
 :latex)

