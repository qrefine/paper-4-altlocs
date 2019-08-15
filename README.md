# paper-4-altlocs
Data storage for paper 4 (alternate locations)

1aie.mtz,1aie.pdb   ----from PDB database (phenix.fetch_pdb --mtz 1aie)

1aie_refine_001.mtz,1aie_refine_001.pdb  ----run PDB file through phenix.refine (phenix.refine 1aie.pdb 1aie.mtz )

1aie_refine_001_complete.pdb  ----run 1aie_refine_001.pdb through qr.finalise ( qr.finalise 1aie_refine_001.pdb)

1aie_refine_001_complete_modified.pdb  ----set occupancies of H to 0 in finalised model (phenix.pdbtools 1aie_refine_001_complete.pdb occupancies.set=0 modify.selection="element H")

1aie_trim - removal of three waters on special positions as indicated in the refinement of 1aie.pdb
-------
At special positions: 3
  Unit cell: (45.5, 45.5, 33.2, 90, 90, 90)
  Space group: P 4 2 2 (No. 89)
  Number of sites at special positions: 3
    Minimum distance between symmetrically equivalent sites: 0.5
    Label                   Mult   Shift    Fractional coordinates
    pdb=" O   HOH A1009 "     2    0.269 ( -0.0032   0.0050  -0.2036) original
                          site sym 4     (  0.0000   0.0000  -0.2036) exact
                                                    0,0,z
    pdb=" O   HOH A1035 "     4    0.171 (  0.0009   0.2072   0.0050) original
                          site sym 2     (  0.0000   0.2072   0.0000) exact
                                                    0,y,0
    pdb=" O   HOH A1036 "     2    0.317 ( -0.0029   0.0063  -0.4472) original
                          site sym 4     (  0.0000   0.0000  -0.4472) exact

Waters removed manually
--------

Each step was repeated on 1aie_trim.pdb to produce 1aie_trim_refine_001_complete_modified.pdb

------------------------
Terachem refinement with phenix-dev-3407 & Q|R v1.0-39-g395e87 starting from 1aie_trim_refine_001_complete.pdb_modified.pdb

HF-D3/6-31G+COSMO water solvent

-----------------------

3q8j is a high resolution structure found by Pavel.
It is 0.87 A resolution, P1 symmetry. 
