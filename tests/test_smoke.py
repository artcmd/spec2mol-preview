from rdkit import Chem


def test_rdkit_parses_smiles():
    mol = Chem.MolFromSmiles("CCO")
    assert mol is not None
    assert mol.GetNumAtoms() == 3
