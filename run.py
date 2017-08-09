from __future__ import division
import iotbx.pdb
import os
from scitbx.array_family import flex

def run(f):
  pdb_inp = iotbx.pdb.input(file_name=f)
  o = pdb_inp.get_r_rfree_sigma()
  cntr = 0
  if (o.high>=1.7 and o.high<=3.0):
    if(pdb_inp.atoms().size()<1000):
      h = pdb_inp.construct_hierarchy()
      for rg in h.residue_groups():
        if(len(rg.conformers())>1):
          cntr+=1
      cntr = cntr*100./len(list(h.residue_groups()))
  return cntr, pdb_inp.atoms().size()

if (__name__ == "__main__"):
  pdb_files = "/net/cci/pdb_mirror/pdb/"
  ifn_p = open("/".join([pdb_files,"INDEX"]),"r")
  cntr_total_pdb = 0
  for i, lp in enumerate(ifn_p.readlines()):
    cntr_total_pdb += 1
    lp = lp.strip()
    pdb_file_name = "/".join([pdb_files,lp])
    pdb_code = os.path.basename(pdb_file_name)[3:7]
    if(pdb_file_name.count(".ent")>0):
      r = run(f=pdb_file_name)
      if(r[0]>5):
        print pdb_file_name, cntr_total_pdb, r[0], r[1]
