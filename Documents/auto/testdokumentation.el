(TeX-add-style-hook
 "testdokumentation"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("inputenc" "utf8") ("babel" "swedish")))
   (TeX-run-style-hooks
    "latex2e"
    "TDP003mall"
    "TDP003mall10"
    "inputenc"
    "babel"
    "listings"
    "xcolor")
   (TeX-add-symbols
    "version")
   (LaTeX-add-labels
    "fig:1"
    "fig:2"
    "fig:3"
    "fig:4"
    "fig:5"
    "fig:6"
    "fig:7"
    "fig:8"
    "fig:9"
    "json"
    "fig:10"))
 :latex)

