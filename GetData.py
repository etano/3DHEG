import sys
import os

def PrintData(pol,rs,ToTF,Observable,channel,exact):
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
      if not pol:
        guu,gud,dguu,dgud = {},{},{},{}
        if channel == 0:
          f = open(dirname+'PairCorrelation_0.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            guu[x] = y/2.
            dguu[x] = dy/2.
          f = open(dirname+'PairCorrelation_2.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            guu[x] += y/2.
            dguu[x] += dy/2.
          f = open(dirname+'PairCorrelation_1.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            gud[x] = y
            dgud[x] = dy
          for x in sorted(gud.iterkeys()):
            print x,0.5*(gud[x]+guu[x]),0.5*(dgud[x]+dguu[x])
        elif channel == 1:
          f = open(dirname+'PairCorrelation_0.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            guu[x] = y/2.
            dguu[x] = dy/2.
          f = open(dirname+'PairCorrelation_2.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            guu[x] += y/2.
            dguu[x] += dy/2.
          for x in sorted(guu.iterkeys()):
            print x,guu[x],dguu[x]
        elif channel == 2:
          f = open(dirname+'PairCorrelation_1.dat')
          for line in f:
            print line,
        else:
          print 'Error with spin channel'
      else:
        f = open(dirname+'PairCorrelation.dat')
        for line in f:
          print line,
    elif Observable == 'sf':
      if not pol:
        suu,sud,dsuu,dsud = {},{},{},{}
        if channel == 0:
          f = open(dirname+'StructureFactor_0.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            suu[x] = y/2.
            dsuu[x] = dy/2.
          f = open(dirname+'StructureFactor_2.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            suu[x] += y/2.
            dsuu[x] += dy/2.
          f = open(dirname+'StructureFactor_1.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            sud[x] = y
            dsud[x] = dy
          for x in sorted(sud.iterkeys()):
            print x,sud[x]+suu[x],dsud[x]+dsuu[x]
        elif channel == 1:
          f = open(dirname+'StructureFactor_0.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            suu[x] = y/2.
            dsuu[x] = dy/2.
          f = open(dirname+'StructureFactor_2.dat')
          for line in f:
            [x,y,dy] = map(float,line.split())
            suu[x] += y/2.
            dsuu[x] += dy/2.
          for x in sorted(suu.iterkeys()):
            print x,suu[x],dsuu[x]
        elif channel == 2:
          f = open(dirname+'StructureFactor_1.dat')
          for line in f:
            print line,
        else:
          print 'Error with spin channel'
      else:
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
    print 'ERROR: Data does not exist in '+dirname+' !'

def usage():
  print "Usage:  %s pol rs T/TF Observables (spin channel) (exact)" % os.path.basename(sys.argv[0])
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
  print 'Possible spin channels: 0 (total, default), 1 (up-up or down-down), 2 (up-down)'
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
    channel = int(sys.argv[5])
  except:
    channel = 0

  try:
    exact = int(sys.argv[6])
  except:
    exact = 0

  PrintData(pol,rs,ToTF,Observable,channel,exact)

if __name__ == "__main__":
  sys.exit(main())
