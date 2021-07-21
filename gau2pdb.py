#! /usr/bin/env python3

from utils import GaussianParser
from utils import PDBParser
import sys, argparse

# Handle CLI arguments
ap = argparse.ArgumentParser(description="")
ap.add_argument('input', type=str, help='Gaussian input file (*.com or *.gif)')
ap.add_argument('output', type=str, help='Output PDB file name')
args = ap.parse_args()

gau_input_file = args.input
pdb_output_file = args.output

gau = GaussianParser.Gaussian(gau_input_file)
pdb = PDBParser.PDB()

# clean coordinates and prepare the PDB
for idx, line in enumerate(gau._coordinates):
    atom_data, freeze, x, y, z, oniom_layer = line.strip().split()
    atom_data = atom_data.split("-")
    try:
        element= atom_data[0]
        name = atom_data[1]
    except IndexError:
        name = atom_data[0]
    
    atom = PDBParser.PDBAtom(
        serial=idx+1,
        name=name,
        chain=oniom_layer,
        x=float(x),
        y=float(y),
        z=float(z),
        segid=freeze,
        element=element)
    pdb.add_atom(atom)
    
pdb.write_pdb(pdb_output_file)
    