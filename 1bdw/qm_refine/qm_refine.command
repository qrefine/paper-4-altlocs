


@
qr.refine ../../1bdw/1bdw_gly_refine_001.mtz ../../1bdw/1bdw_gly_refine_001_complete.pdb_modified.pdb  altloc_method=average restraints=qm clustering=true qm_engine_name=terachem mode=refine maxnum_residues_in_cluster=6 qsub_command='sbatch -p gpu --gres=gpu:4:gpu --exclude=cu[01-12]  --cpus-per-task=4  --time=1:20:20 ' method=slurm basis=6-31g  stpmax=0.5 max_iterations=50   number_of_macro_cycles=1 two_buffers=false charge_embedding=true  charge_cutoff=8.0  restraints_weight_scale=8.0   > qm_refine.log 2>&1 &

