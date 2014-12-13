# 3DHEG

Energies, pair correlation functions, and structure factors for the 3-dimensional homogeneous electron gas (3DHEG)

## Use

### Directory structure

The directory structure is as follows:

* polarization
    * r_{s}
        * T/T_{F}
            * exact (for specific points)

### Retrieving data

To access the data, I have provided a simple python script (GetData.py) which grabs data from the files and outputs it to the screen.

#### Inputs

Its arguments are:

`python GetData.py polarization r_{s} T/T_{F} Observable (spin channel) (exact)`

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

Possible spin channels: 0 (total, default), 1 (up-up or down-down), 2 (up-down)

The optional exact flag (1 - true, 0 - false (default)) will output signful calculations where possible.

#### Outputs

All data is given in the following format:

`x f(x) err(f(x))`

### Citation

If you find this data useful in your research, please cite the original reference:

  E. W. Brown, B. K. Clark, J. L. DuBois, and D. M. Ceperley  
  [Path Integral Monte Carlo simulation of the warm-dense homogeneous electron gas](http://prl.aps.org/abstract/PRL/v110/i14/e146405)  
  Phys. Rev. Lett. 110, 146405 (2013)
  
Also please cite this repository:

[![DOI](https://zenodo.org/badge/7803/etano/3DHEG.svg)](http://dx.doi.org/10.5281/zenodo.13241)

Bibtex:

    @article{PhysRevLett.110.146405,
      title = {Path-Integral Monte~Carlo Simulation of the Warm Dense Homogeneous Electron Gas},
      author = {Brown, Ethan W. and Clark, Bryan K. and DuBois, Jonathan L. and Ceperley, David M.},
      journal = {Phys. Rev. Lett.},
      volume = {110},
      issue = {14},
      pages = {146405},
      numpages = {5},
      year = {2013},
      month = {Apr},
      doi = {10.1103/PhysRevLett.110.146405},
      url = {http://link.aps.org/doi/10.1103/PhysRevLett.110.146405},
      eprint = {1211.6130},
      publisher = {American Physical Society}
    }

