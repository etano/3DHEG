import sys
import os

rss = [1.0,2.0,4.0,6.0,8.0,10.0,40.0]
pols = [0,1]
polnames = ['unpol','pol']
exacts = ['signful','restricted']
ToTFs = [0.0625,0.125,0.25,0.5,1.0,2.0,4.0,8.0]

def GetRefData(rs,ToTF,pol,exact):
  if pol:
    N = 33
    MinM = 8
    if rs in [1.0]:
      RefM = 64
    elif rs in [2.0]:
      RefM = 64
    elif rs in [4.0,6.0,8.0,10.0,40.0]:
      RefM = 32
    if exact:
      if rs in [1.0]:
        RefM = 128
      if rs in [10.0]:
        RefM = 64
  else:
    N = 66
    MinM = 8
    if rs in [1.0]:
      RefM = 128
    elif rs in [2.0,4.0,6.0,8.0,10.0]:
      RefM = 64
    elif rs in [40.0]:
      RefM = 32

  RefToTF = 1.0
  M = int((RefToTF/ToTF)*RefM) # Number of Time Slices
  if M < MinM:
    M = MinM
  return N,M


def CreateDir(prefix,name):
  dirname = prefix+str(name)
  try:
    os.makedirs(dirname)
    print 'Creating directory',dirname
  except:
    print 'Directory',dirname,'exists'
  return dirname+'/'

import shutil
from scipy.misc import comb

def WriteData(filename,exact):
  f = open(filename,'r')
  for line in f:
    line = line.split()
    rs = float(line[0])
    ToTF = float(line[1])
    e = float(line[2])
    eerr = float(line[3])
    k = float(line[4])
    kerr = float(line[5])
    dU = float(line[6])
    dUerr = float(line[7])
    v = float(line[8])
    verr = float(line[9])
    dE_N = float(line[10])
    dk_N = float(line[11])
    dv_N = float(line[12])
    kf = float(line[13])
    kf0 = float(line[14])
    exf = float(line[15])
    exf0 = float(line[16])
    ec0 = float(line[17])
    sgn = float(line[18])
    dsgn = float(line[19])
    N,M = GetRefData(rs,ToTF,pol,exact)
    if exact:
      remotedir = '../3dheg/exact/data/heg-'+str(rs)+'-4-'+str(ToTF)+'-'+str(pol)+'-'+str(N)+'-'+str(M)+'/'
      localdir = polStr+'/'+str(rs)+'/'+str(ToTF)+'/exact/'
    else:
      remotedir = '../3dheg/'+polStr+'/data/heg-'+str(rs)+'-4-'+str(ToTF)+'-'+str(pol)+'-'+str(N)+'-'+str(M)+'/'
      localdir = polStr+'/'+str(rs)+'/'+str(ToTF)+'/'

    # Energies
    e += dE_N
    k += dk_N
    v += dv_N
    dU += dv_N

    ec = e-kf-exf
    ecerr = eerr

    if ToTF <= 8.0:
      try:
        g = open(localdir+'Energy.dat','w')
      except:
        os.makedirs(localdir)
        g = open(localdir+'Energy.dat','w')
      g.write('E %f %f\n'%(e,eerr))
      g.write('K %f %f\n'%(k,kerr))
      g.write('V %f %f\n'%(v,verr))
      g.write('dU %f %f\n'%(dU,dUerr))
      g.write('Ec %f %f\n'%(ec,ecerr))
      g.close()

    # Pair Correlation and Structure Factor
    speciesStr = ''
    if pol:
      nSpecies = 1
    else:
      nSpecies = 2
    nCombos = int(nSpecies + comb(nSpecies,2))
    for iCombo in range(0,nCombos):
      if (nCombos > 1):
        speciesStr = '_'+str(iCombo)
      if exact:
        try:
          shutil.copy(remotedir+'AdjPairCorrelation'+speciesStr+'.dat',localdir)
          shutil.copy(remotedir+'AdjStructureFactor'+speciesStr+'.dat',localdir)
        except:
          print remotedir, 'lacking adjusted correlation values'
      else:
        shutil.copy(remotedir+'PairCorrelation'+speciesStr+'.dat',localdir)
        shutil.copy(remotedir+'StructureFactor'+speciesStr+'.dat',localdir)

    # Sign
    if exact:
      g = open(remotedir+'AvgSigns.dat','r')
      data = [float(x) for x in g.readline().split()[1:]]
      g.close()
      g = open(localdir+'Sign.dat','w')
      g.write('%f %f\n'%(data[0],data[1]))

  f.close()

rss = [1.0,2.0,4.0,6.0,8.0,10.0,40.0]
pols = [0,1]
for pol in pols:
  if pol:
    polStr = 'pol'
  else:
    polStr = 'unpol'

  WriteData('Es-'+str(pol)+'.dat',0)
  WriteData('EXCTs-'+str(pol)+'.dat',1)


