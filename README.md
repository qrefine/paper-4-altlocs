# paper-4-altlocs
Data storage for paper 4 (alternate locations)

1aie.mtz,1aie.pdb   ----from PDB database 

1aie_refine_001.mtz,1aie_refine_001.pdb  ----run PDB file through phenix.refine

1aie_refine_001_complete.pdb  ----run 1aie_refine_001.pdb through qr.finalise

1aie_refine_001_complete_modified.pdb  ----set occupancies of H to 0 in finalised model

1aie_trim - removal of three waters on special positions 

------------------------
Terachem refinement with phenix-dev-3407 & starting from 1aie_trim_refine_001_complete.pdb_modified.pdb

HF-D3/6-31G+COSMO water solvent
