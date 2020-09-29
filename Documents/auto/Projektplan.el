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
    "xcolor"
    "tabularx"
    "enumitem"
    "makecell")
   (TeX-add-symbols
    "version")
   (LaTeX-add-labels
    "tab:1"
    "tab:2"
    "tab:3"
    "tab:4"
    "tab:5"
    "tab:6"
    "tab:7"
    "tab:8"))
 :latex)

