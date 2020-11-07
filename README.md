# paper-4-altlocs
Data storage for paper 4 (alternate locations)

1aie.mtz,1aie.pdb   ----from PDB database (phenix.fetch_pdb --mtz 1aie)

1aie_refine_001.mtz,1aie_refine_001.pdb  ----run PDB file through phenix.refine (phenix.refine 1aie.pdb 1aie_phases.mtz )

1aie_refine_001_complete.pdb  ----run 1aie_refine_001.pdb through qr.finalise ( qr.finalise 1aie_refine_001.pdb), this also remove three waters on special positions (A1009, A1035 and A1036)

1aie_refine_001_complete_modified.pdb  ----set occupancies of H to 0 in finalised model (phenix.pdbtools 1aie_refine_001_complete.pdb occupancies.set=0 modify.selection="element H")
 
-----------------------
Refinement with Phenix 1.19rc5-4044 & Q|R v1.0-196-g1cccac-dirty (or newer) starting from 1aie_refine_001_complete_modified.pdb
-----------------------

3q8j is a high resolution structure found by Pavel.
It is 0.87 A resolution, P1 symmetry. 
