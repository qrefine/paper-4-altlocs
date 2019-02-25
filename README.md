# paper-4-altlocs
Data storage for paper 4 (alternate locations)

1aie.mtz,1aie.pdb   ----from PDB database 

1aie_refine_001.mtz,1aie_refine_001.pdb  ----run PDB file through phenix.refine

1aie_refine_001_complete.pdb  ----run 1aie_refine_001.pdb through qr.finalise

1aie_refine_001_complete_modified.pdb  ----set occupancies of H to 0 in finalised model

1aie_trim - removal of three waters on special positions as indicated in the refinement of 1aie.pdb

Each step was repeated on 1aie_trim.pdb to produce 1aie_trim_refine_001_complete_modified.pdb

------------------------
Terachem refinement with phenix-dev-3407 & Q|R v1.0-39-g395e87 starting from 1aie_trim_refine_001_complete.pdb_modified.pdb

HF-D3/6-31G+COSMO water solvent

-----------------------

3q8j is a high resolution structure found by Pavel.
It is 0.87 A resolution, P1 symmetry. 
