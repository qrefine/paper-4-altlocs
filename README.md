# paper-4-altlocs
Data storage for paper 4 (alternate locations)

1aie.mtz,1aie.pdb   ----from PDB database (phenix.fetch_pdb --mtz 1aie)

1aie_refine_001.mtz,1aie_refine_001.pdb  ----run PDB file through phenix.refine (phenix.refine 1aie.pdb 1aie.mtz )

1aie_refine_001_complete.pdb  ----run 1aie_refine_001.pdb through qr.finalise ( qr.finalise 1aie_refine_001.pdb)

1aie_refine_001_complete_modified.pdb  ----set occupancies of H to 0 in finalised model (phenix.pdbtools 1aie_refine_001_complete.pdb occupancies.set=0 modify.selection="element H")

1aie_trim_g - removal of three waters on special positions from 1aie.pdb as indicated in the refinement of 1aie.pdb (A1009, A1035 and A1036)

Each step was repeated on 1aie_trim_g.pdb 

1. phenix.refine 1aie_trim_g.pdb 1aie.mtz  - > 1aie_trim_g_refine_001.pdb 1aie_trim_g_refine_001.mtz
2. qr.finalise 1aie_trim_g_refine_001.pdb -> 1aie_trim_g_refine_001_complete.pdb
3. phenix.pdbtools 1aie_trim_g_refine_001_complete.pdb occupancies.set=0 modify.selection="element H" -> 1aie_trim_g_refine_001_complete.pdb_modified.pdb
 
----------------
cp 1aie_trim_g_refine_001_complete.pdb_modified.pdb 1aie_trim_g_19Aug.pdb
-----------------------
Terachem refinement with phenix-dev-3407 & Q|R v1.0-39-g395e87 starting from 1aie_trim_refine_001_complete.pdb_modified.pdb

HF-D3/6-31G+COSMO water solvent

-----------------------

3q8j is a high resolution structure found by Pavel.
It is 0.87 A resolution, P1 symmetry. 
