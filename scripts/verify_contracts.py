import requests

class ContractAnalyzer:
    def __init__(self, rpc_url, solsniffer_api_key):
        self.rpc_url = rpc_url
        self.solsniffer_api_key = solsniffer_api_key
        self.solsniffer_url = "https://api.solsniffer.com/v1/"

    def fetch_contract_code(self, contract_address):
        """Fetch the contract code from the blockchain."""
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "getAccountInfo",
            "params": [contract_address, {"encoding": "base64"}]
        }
        response = requests.post(self.rpc_url, json=payload)
        if response.status_code == 200:
            data = response.json()
            return data.get("result", {}).get("value", {}).get("data", [None])[0]
        else:
            raise Exception("Failed to fetch contract code")

    def analyze_contract(self, contract_code):
        """Analyze the contract code for vulnerabilities."""
        # Placeholder for analysis logic
        vulnerabilities = []
        if "reentrancy" in contract_code:
            vulnerabilities.append("Potential reentrancy vulnerability detected.")
        if "delegatecall" in contract_code:
            vulnerabilities.append("Use of delegatecall detected, which may be unsafe.")
        # Add more analysis checks as needed
        return vulnerabilities

    def verify_with_solsniffer(self, contract_address):
        """Verify the contract with SolSniffer API."""
        headers = {
            "Authorization": f"Bearer {self.solsniffer_api_key}"
        }
        response = requests.get(f"{self.solsniffer_url}check/{contract_address}", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Failed to verify with SolSniffer API")

    def analyze_and_verify(self, contract_address):
        """Main method to analyze and verify a contract."""
        try:
            contract_code = self.fetch_contract_code(contract_address)
            vulnerabilities = self.analyze_contract(contract_code)
            solsniffer_result = self.verify_with_solsniffer(contract_address)
            return {
                "vulnerabilities": vulnerabilities,
                "solsniffer_verification": solsniffer_result
            }
        except Exception as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    rpc_url = "https://api.mainnet-beta.solana.com"
    solsniffer_api_key = "YourSolSnifferAPIKeyHere"  # Replace with your SolSniffer API key
    contract_address = "YourContractAddressHere"  # Replace with the actual contract address
    
    analyzer = ContractAnalyzer(rpc_url, solsniffer_api_key)
    result = analyzer.analyze_and_verify(contract_address)
    print(result)
    