3DHEG
=====

Energies, pair correlation functions, and structure factors for the 3-dimensional homogeneous electron gas (3DHEG)

USE
---

The directory structure is as follows:

* polarization
  * rs
    * T/TF
      * exact (for specific points)

To access the data, I have provided a simple python script (GetData.py) which grabs data from the files and outputs it to the screen. Its arguments are:

'python GetData.py polarization r_{s} T/T_{F} Observable'

Possible observables:
* E
* K
* V
* U
* Ec
* PairCorrelation
* StructureFactor
* Sign
