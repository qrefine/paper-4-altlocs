run gradient 
$multibasis 
Se lanl2dz_ecp
Cl lanl2dz_ecp
Cd lanl2dz_ecp
Zn lanl2dz_ecp
Mg lanl2dz_ecp 
$end 
basis 6-31g 
scf diis 
coordinates /home/qr/paper-4-altlocs/1bdw/qm_ala/ase/2/2_capping.xyz 
gpumem 512 
charge 3 
seed 1351351 
maxit 200 
threall 1e-12 
pointcharges /home/qr/paper-4-altlocs/1bdw/qm_ala/ase/2/2_qxyz_cctbx.dat 
gpus 4 
watcheindiis no 
method rhf 
dftd yes 
scrdir /tmp/qr/paper-4-altlocs/1bdw/qm_ala/ase/2/scr 
end