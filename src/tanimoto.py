import numpy
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem

def tanimoto_distance(smiles1, smiles2):
    # ms = [Chem.MolFromSmiles(smiles1), Chem.MolFromSmiles(smiles2)]
    
    # fpgen = AllChem.GetRDKitFPGenerator()
    # fps = [fpgen.GetFingerprint(x) for x in ms]
    
    # # Compute Tanimoto similarity
    # tanimoto_similarity = DataStructs.TanimotoSimilarity(fps[0], fps[1])
    # # Compute Tanimoto distance (1 - similarity)
    # tanimoto_distance = 1 - tanimoto_similarity

    # Convert molecules to fingerprints
    mol1 = Chem.MolFromSmiles(smiles1)
    mol2 = Chem.MolFromSmiles(smiles2)
    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 2, nBits=1024)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 2, nBits=1024)

    # Compute Tanimoto distance
    tanimoto_distance = 1.0 - DataStructs.TanimotoSimilarity(fp1, fp2)
    
    return tanimoto_distance