from backend.core.blockchain.block import Block
from backend.core.blockchain.transaction import Transaction
from backend.core.mining.pow import proof_of_work
from backend.core.mining.difficulty import adjust_difficulty
from backend.core.mining.reward import calculate_reward

class Miner:
    def __init__(self, blockchain, mining_address: str):
        self.blockchain = blockchain
        self.mining_address = mining_address
        self.difficulty = 4  # awal

    def mine_block(self, pending_transactions: list):
        # 🪙 Tambah reward untuk penambang
        reward_amount = calculate_reward(len(self.blockchain))
        reward_tx = Transaction("NEUTRON_REWARD", self.mining_address, reward_amount, "reward-signature")
        transactions = pending_transactions + [reward_tx]

        # ⛏️ Buat block baru
        previous_block = self.blockchain[-1]
        new_block = Block(
            index=previous_block.index + 1,
            transactions=transactions,
            previous_hash=previous_block.hash
        )

        # 🚀 Mulai mining
        nonce, block_hash, duration = proof_of_work(new_block, self.difficulty)
        self.difficulty = adjust_difficulty(duration, self.difficulty)

        print(f"✅ Block mined! Hash: {block_hash}")
        print(f"⛏️ Nonce: {nonce}, Duration: {duration}s, Difficulty: {self.difficulty}")

        # Tambahkan ke blockchain
        self.blockchain.append(new_block)
