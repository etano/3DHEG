3DHEG
=====

Energies, pair correlation functions, and structure factors for the 3-dimensional homogeneous electron gas (3DHEG)

Use
---

The directory structure is as follows:

* polarization
    * r_{s}
        * T/T_{F}
            * exact (for specific points)

To access the data, I have provided a simple python script (GetData.py) which grabs data from the files and outputs it to the screen. Its arguments are:

`python GetData.py polarization r_{s} T/T_{F} Observable (exact)`

Possible polarizations: 0, 1

Possible r_{s}: 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 40.0

Possible T/T_{F}: 0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0

Possible observables (note all energies given in Rydbergs):
* e (Total energy)
* k (Kinetic energy)
* v (Bare coulomb energy)
* u ("Potential" energy, dU/d\Beta)
* ec (Correlation energy)
* pc (Pair correlation function)
* sf (Structure factor)
* sgn (Average value of the sign, only for exact = 1)

The optional exact flag (1 - true, 0 - false (default)) will output signful calculations where possible.


If you find this data useful in your research, please cite the original reference:

  E. W. Brown, B. K. Clark, J. L. DuBois, and D. M. Ceperley  
  [Path Integral Monte Carlo simulation of the warm-dense homogeneous electron gas](http://arxiv.org/abs/1211.6130)  
  arXiv:1211:6130  

Bibtex:

    @ARTICLE{2012arXiv1211.6130B,
       author = {{Brown}, E.~W. and {Clark}, B.~K. and {DuBois}, J.~L. and {Ceperley}, D.~M.},
        title = "{Path Integral Monte Carlo Simulation of the Warm-Dense Homogeneous Electron Gas}",
      journal = {ArXiv e-prints},
    archivePrefix = "arXiv",
       eprint = {1211.6130},
     primaryClass = "cond-mat.str-el",
     keywords = {Condensed Matter - Strongly Correlated Electrons, Condensed Matter - Other Condensed Matter},
         year = 2012,
        month = nov,
       adsurl = {http://adsabs.harvard.edu/abs/2012arXiv1211.6130B},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
    }

