


@
qr.refine ../../1bdw/1bdw_gly_refine_001.mtz ../../1bdw/1bdw_gly_refine_001_complete.pdb_modified.pdb  altloc_method=average restraints=qm clustering=true qm_engine_name=terachem mode=refine maxnum_residues_in_cluster=6 qsub_command='sbatch -p gpu --gres=gpu:4 --exclude=cpu[01-06]  --cpus-per-task=4  --time=1:50:20 ' method=slurm basis=6-31g  stpmax=0.5 max_iterations=100   number_of_macro_cycles=1 two_buffers=false charge_embedding=true    restraints_weight_scale=1.0 charge_cutoff=8.0    > qm_refine.log 2>&1 &

