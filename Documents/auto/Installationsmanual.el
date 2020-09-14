(TeX-add-style-hook
 "Installationsmanual"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "swedish")))
   (TeX-run-style-hooks
    "latex2e"
    "TDP003mall"
    "TDP003mall10"
    "inputenc"
    "babel"
    "graphicx")
   (TeX-add-symbols
    "version")
   (LaTeX-add-labels
    "fig"))
 :latex)

