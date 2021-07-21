#! /usr/bin/env python3

class PDBAtom():
    """Single atom object in PDB file format
    """
    def __init__(self, serial:int, name:str, x:float, y:float, z:float, element:str, 
                 occupancy=1, bfactor=1, segid=None, charge=None, record="ATOM", altloc=None, 
                 chain="A", resid=1, insertion=None, resname="MOL") -> None:
        self.record    = record
        self.serial    = serial
        self.name      = name
        self.altloc    = self.xstr(altloc)
        self.resname   = resname
        self.chain     = chain
        self.resid     = resid
        self.insertion = self.xstr(insertion)
        self.x = x
        self.y = y
        self.z = z
        self.occupancy = occupancy
        self.bfactor   = bfactor
        self.segid     = self.xstr(segid)
        self.element   = element
        self.charge    = self.xstr(charge)
        
    def __str__(self) -> str:
        space = " "
        atom = f"{self.record:6s}{self.serial:>5d}{space}{self.name:<4s}{self.altloc:1s}{self.resname:>3s}{space}\
{self.chain:1s}{self.resid:>4d}{self.insertion:1s}{space*3}{self.x:>8.3f}{self.y:>8.3f}{self.z:>8.3f}{self.occupancy:>6.2f}\
{self.bfactor:>6.2f}{space*6}{self.segid:<4s}{self.element:>2s}{self.charge:2s}\n"
        return atom
    
    def xstr(self, value):
        """Convert an empty atom property to empty string
        """
        return "" if value is None else value

          
class PDB():
    """Class to hold a PDB file consistant of multiple atoms
    """
    def __init__(self) -> None:
        self.atoms = []
        
    def add_atom(self, atom: PDBAtom) -> None:
        self.atoms.append(atom)
        
    def write_pdb(self, filename) -> None:
        with open(filename, "w") as f:
            f.write("CRYST1    0.000    0.000    0.000  90.00  90.00  90.00 P 1           1\n")
            for atom in self.atoms:
                f.write(str(atom))
            f.write("END")
                
          
if __name__ == "__main__":
    pass
    
    

