#! /usr/bin/env python3

from utils import GaussianParser
from utils import XYZParser
import sys, argparse

# Handle CLI arguments
ap = argparse.ArgumentParser(description="")
ap.add_argument('input', type=str, help='Gaussian input file (*.com or *.gif)')
# ap.add_argument('output', type=str, help='Output XYZ file name')
args = ap.parse_args()

gau_input_file = args.input
xyz_output_file = f"{gau_input_file[:-4]}.xyz"
# if not args.output:
#     xyz_output_file = f"{gau_input_file[:-4]}.xyz"
# else:
#     xyz_output_file = args.output

gau = GaussianParser.Gaussian(gau_input_file)
xyz = XYZParser.XYZ()

# clean coordinates and prepare the XYZ
for idx, line in enumerate(gau._coordinates):
    atom_data, freeze, x, y, z, oniom_layer = line.strip().split()
    atom_data = atom_data.split("-")
    try:
        element= atom_data[0]
        name = atom_data[1]
    except IndexError:
        name = atom_data[0]
    
    atom = XYZParser.XYZAtom(
        element=element,
        x=float(x),
        y=float(y),
        z=float(z))
    xyz.add_atom(atom)
    
xyz.write_xyz(xyz_output_file)
    