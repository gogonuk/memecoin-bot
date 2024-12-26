`python
import unittest
from src.verify_contracts import ContractAnalyzer

class TestContractAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ContractAnalyzer("https://api.mainnet-beta.solana.com", "test_api_key")

    def test_fetch_contract_code(self):
        # Mock the response and test fetch_contract_code method
        pass  # Implement your test logic here

    def test_analyze_contract(self):
        # Test analyze_contract method with sample contract code
        contract_code = "contract with reentrancy"
        vulnerabilities = self.analyzer.analyze_contract(contract_code)
        self.assertIn("Potential reentrancy vulnerability detected.", vulnerabilities)

if name == 'main':
    unittest.main()