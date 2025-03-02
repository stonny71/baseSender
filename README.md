**baseSender**  
A Python-based tool designed to send Base Ethereum (ETH) to multiple wallets concurrently with extremely low gas fees (as low as $0.002). This repository includes scripts to manage wallet configurations (`config.py`), handle the core sending logic (`main.py`), and store wallet information (`wallets.txt`). The project is optimized for efficiency and cost-effectiveness, making it ideal for bulk ETH transactions on the Ethereum (base) network.

#### Features:
- Sends ETH (base) to multiple wallets simultaneously.
- Minimizes gas fees, achieving costs as low as $0.002 per transaction.
- Configurable settings for wallet management and transaction parameters via `config.py`.
- Main processing logic in `main.py` for executing bulk transactions.
- Supports storing wallet addresses and related data in a simple text format (`wallets.txt`).

#### Getting Started:
1. Install required dependencies (e.g., Web3.py for Ethereum interactions):
   ```
   pkg install python
   pip install web3
 
2. Clone the repository:
   ```
   git clone https://github.com/stonny71/baseSender.git
   cd baseSender
   ```
   
3. Configure your wallet data in `wallets.txt` and settings in `config.py`.
4. Run the main script:
   ```
   python main.py
   ```

#### Prerequisites:
- A funded Ethereum wallet with sufficient ETH for gas fees and transactions.
- Access to the Ethereum network (e.g., via an Infura, Alchemy, or local node).
- Basic understanding of Ethereum and wallet management.


#### Disclaimer:
Use this tool responsibly and in compliance with all applicable laws and regulations. The developers are not liable for any losses or damages incurred from using this software.
