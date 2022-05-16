#! /usr/bin/env python3

class XYZAtom():
    """Single atom object in PDB file format
    """
    def __init__(self, element:str, x:float, y:float, z:float) -> None:
        self.element   = element
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self) -> str:
        atom = f"{self.element:>3s}{self.x:>10.3f}{self.y:>10.3f}{self.z:>10.3f}\n"
        return atom

          
class XYZ():
    """Class to hold a PDB file consistant of multiple atoms
    """
    def __init__(self) -> None:
        self.atoms = []
        
    def add_atom(self, atom: XYZAtom) -> None:
        self.atoms.append(atom)
        
    def write_xyz(self, filename) -> None:
        n_atoms = len(self.atoms)
        comment_line = " "
        
        with open(filename, "w") as f:
            f.write(f"{n_atoms}\n")
            f.write(f"{comment_line}\n")
            for atom in self.atoms:
                f.write(str(atom))
                
          
if __name__ == "__main__":
    pass
    
    

