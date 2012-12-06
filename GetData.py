import sys
import os

def PrintData(pol,rs,ToTF,Observable,exact):
  if pol:
    polStr = 'pol'
  else:
    polStr = 'unpol'
  if exact:
    dirname = polStr+'/'+str(rs)+'/'+str(ToTF)+'/exact/'
  else:
    dirname = polStr+'/'+str(rs)+'/'+str(ToTF)+'/'
  try:
    EnergyStrs = ['e','k','v','u','ec']
    if Observable in EnergyStrs:
      f = open(dirname+'Energy.dat')
      data = f.readlines()
      x = float(data[EnergyStrs.index(Observable)].split()[-2])
      dx = float(data[EnergyStrs.index(Observable)].split()[-1])
      print x,dx
    elif Observable == 'pc':
      f = open(dirname+'PairCorrelation.dat')
      for line in f:
        print line,
    elif Observable == 'sf':
      f = open(dirname+'StructureFactor.dat')
      for line in f:
        print line,
    elif Observable == 'sgn':
      if exact:
        f = open(dirname+'Sign.dat')
        print f.readline(),
      else:
        print '1.0 0.0'
    else:
      print 'ERROR: Unrecognized Observable!'
  except:
    print 'ERROR: Data does not exist!'


def usage():
  print "Usage:  %s pol rs T/TF Observables (exact)" % os.path.basename(sys.argv[0])
  print 'Possible polarizations: 0, 1'
  print 'Possible r_{s}: 1.0, 2.0, 4.0, 6.0, 8.0, 10.0, 40.0'
  print 'Possible T/T_{F}: 0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0'
  print 'Possible observables (note all energies given in Rydbergs):'
  print '* e (Total energy)'
  print '* k (Kinetic energy)'
  print '* v (Bare coulomb energy)'
  print '* u ("Potential" energy, dU/d\Beta)'
  print '* ec (Correlation energy)'
  print '* pc (Pair correlation function)'
  print '* sf (Structure factor)'
  print '* sgn (Average value of the sign)'
  print 'The optional exact flag (1 - true, 0 - false (default)) will output signful calculations where possible.'
  sys.exit(2)

def main(argv=None):
  if argv is None:
    argv = sys.argv
  if "-h" in argv or "--help" in argv:
    usage()

  try:
    pol = int(sys.argv[1])
    rs = float(sys.argv[2])
    ToTF = float(sys.argv[3])
    Observable = str(sys.argv[4])
  except:
    usage()

  try:
    exact = int(sys.argv[5])
  except:
    exact = 0

  PrintData(pol,rs,ToTF,Observable,exact)

if __name__ == "__main__":
  sys.exit(main())
