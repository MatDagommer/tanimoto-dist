import numpy
from rdkit import Chem, DataStructs
from rdkit.Chem import AllChem

def tanimoto_distance(smiles1, smiles2):
    ms = [Chem.MolFromSmiles(smiles1), Chem.MolFromSmiles(smiles2)]
    
    fpgen = AllChem.GetRDKitFPGenerator()
    fps = [fpgen.GetFingerprint(x) for x in ms]
    
    # Compute Tanimoto similarity
    tanimoto_similarity = DataStructs.TanimotoSimilarity(fps[0], fps[1])
    # Compute Tanimoto distance (1 - similarity)
    tanimoto_distance = 1 - tanimoto_similarity
    
    return tanimoto_distance