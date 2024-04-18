import unittest
from src.tanimoto import tanimoto_distance

class TestTanimoto(unittest.TestCase):
    def test_tanimoto_distance(self):
        """
        Test that the returned Tanimoto distance is correct.
        """
        smiles1 = "CC(O)=O"
        smiles2 = "c1ccccc1"
        result = tanimoto_distance(smiles1, smiles2)
        self.assertEqual(result, 0.96, msg="Tanimoto passed.")

if __name__ == '__main__':
    unittest.main()