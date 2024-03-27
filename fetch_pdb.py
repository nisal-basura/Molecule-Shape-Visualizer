import requests

def fetch_pdb_file(molecule_name):
    """
    Downloads a PDB file for the specified molecule by PDB ID.
    Args:
        molecule_name (str): The PDB ID of the molecule.
    Returns:
        str: Path to the downloaded PDB file.
    """
    url = f"https://files.rcsb.org/download/{molecule_name}.pdb"
    response = requests.get(url)
    
    # Check if the request was successful (HTTP status code 200)
    if response.status_code == 200:
        filename = f"{molecule_name}.pdb"
        with open(filename, 'wb') as file:
            file.write(response.content)
        return filename
    else:
        print("Error fetching the PDB file.")
        return None

# Example usage
molecule_name = input("Enter the PDB ID of the molecule: ").strip()
pdb_file_path = fetch_pdb_file(molecule_name)

if pdb_file_path:
    print(f"PDB file downloaded: {pdb_file_path}")
    # You can now load this file into MDAnalysis or another analysis tool
    # u = mda.Universe(pdb_file_path)
else:
    print("Failed to download the PDB file.")
