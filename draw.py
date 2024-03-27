
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib.lines import Line2D

def read_pdb(filepath):
    """Reads a PDB file and returns a list of atomic coordinates, atom names, and the molecule name."""
    coordinates = []
    atom_names = []
    molecule_name = "Molecule"  # Default name
    with open(filepath, 'r') as file:
        for line in file:
            if line.startswith("TITLE"):
                molecule_name = line[10:].strip()  # Assuming TITLE information is here
            elif line.startswith("ATOM") or line.startswith("HETATM"):
                x, y, z = float(line[30:38]), float(line[38:46]), float(line[46:54])
                atom_name = line[76:78].strip()
                coordinates.append((x, y, z))
                atom_names.append(atom_name)
    return coordinates, atom_names, molecule_name

def plot_structure_with_legend_and_bonds(coordinates, atom_names, molecule_name):
    """Plots the molecular structure with a legend for atom types and detailed bonds."""
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title(molecule_name)
    
    atom_colors = {
        'H': 'gray', 'C': 'black', 'N': 'green', 'O': 'red', 'S': 'yellow',
    }
    
    # Plot atoms
    for atom_type, color in atom_colors.items():
        filtered_coords = [coord for coord, name in zip(coordinates, atom_names) if name == atom_type]
        if filtered_coords:  # Check if there are atoms to plot
            xs, ys, zs = zip(*filtered_coords)
            ax.scatter(xs, ys, zs, c=color, label=atom_type)

    # Plot bonds - specify color here, e.g., 'blue'
    bond_color = 'blue'  # Change this to your desired color
    max_bond_length = 1.6
    for i, coord_i in enumerate(coordinates):
        for j, coord_j in enumerate(coordinates[i+1:], start=i+1):
            dist = np.linalg.norm(np.array(coord_i) - np.array(coord_j))
            if dist <= max_bond_length:
                ax.plot([coord_i[0], coord_j[0]], [coord_i[1], coord_j[1]], [coord_i[2], coord_j[2]], color=bond_color, linestyle='--')

    # Legend for atoms
    legend_elements = [Line2D([0], [0], marker='o', color='w', label=k, markerfacecolor=v, markersize=10) for k, v in atom_colors.items()]
    ax.legend(handles=legend_elements, title="Atoms", loc='upper right')

    # Additional legend for bonds
    ax.plot([], [], color=bond_color, linestyle='--', label='Bond (~1.6 Å)')
    ax.legend(loc='upper right')

    plt.show()

# Path to your PDB file
pdb_path = 'D:/python/GSOC/1MBN.pdb'  # Update this path

# Read and plot
coords, atom_names, molecule_name = read_pdb(pdb_path)
plot_structure_with_legend_and_bonds(coords, atom_names, molecule_name)

