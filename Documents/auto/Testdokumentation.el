(TeX-add-style-hook
 "Testdokumentation"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "swedish")))
   (TeX-run-style-hooks
    "latex2e"
    "TDP003mall"
    "TDP003mall10"
    "inputenc"
    "babel")
   (TeX-add-symbols
    "version")
   (LaTeX-add-labels
    "fig:2"))
 :latex)

