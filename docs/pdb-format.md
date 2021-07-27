PDB File Format
==

Read more:
 - [Wiki](https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format))
 - [Protein Data Bank Contents Guide](http://www.wwpdb.org/documentation/file-format-content/format33/v3.3.html)

```
            Columns         | Data                             (Justification) DataType
    record    1-4	(:6s)   | ATOM                             ( ) character
    serial    7-11  (:>5d)  | Atom_serial_number	           (right) integer
    [space]
    name      13-16	(:<4s)  | Atom name	                       (left) character
    altloc    17	(:1s)   | Alternate location indicator     ( ) character
    resname   18-20	(:>3s)  | Residue name	                   (right) character
    [space]
    chain     22	(:1s)   | Chain identifier	               ( ) character
    resid     23-26	(:>4d)  | Residue sequence number	       (right) integer
    insertion 27	(:1s)   | Code for insertions of residues  ( ) character
    [space*3]
    x         31-38	(:>8.3f)| X orthogonal Å coordinate	       (right) real (8.3)
    y         39-46	(:>8.3f)| Y orthogonal Å coordinate	       (right) real (8.3)
    z         47-54	(:>8.3f)| Z orthogonal Å coordinate	       (right) real (8.3)
    occupancy 55-60	(:>6.2f)| Occupancy	                       (right) real (6.2)
    bfactor   61-66	(:>6.2f)| Temperature factor	           (right) real (6.2)
    [space*6]
    segid     73-76	(:<4s)  | Segment identifier	           (left) character
    element   77-78	(:>2s)  | Element symbol	               (right) character
    charge    79-80	(:2s)   | Charge	                       ( ) character
```