import  iotbx.pdb
import time
import sys
import qrefine.completion as completion

log = sys.stdout

def run(pdb_file, log, ref_file):
  pdb_inp = iotbx.pdb.input(pdb_file)
  ph = pdb_inp.construct_hierarchy()
  cs = pdb_inp.crystal_symmetry()
  capped_ph=completion.run(pdb_hierarchy=ph,
                      crystal_symmetry=cs,
                      model_completion=False,
                      original_pdb_filename=ref_file)
  capped_ph.write_pdb_file(file_name="capped_ref.pdb")

if (__name__ == "__main__"):
  t0 = time.time()
  args = sys.argv[1:]
  del sys.argv[1:]
  run(args[0], log, args[1])
  print >> log, "Time: %6.4f" % (time.time() - t0)
