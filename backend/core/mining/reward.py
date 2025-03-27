# 💰 Konfigurasi dasar
INITIAL_REWARD = 50.0  # NTR per block
HALVING_INTERVAL = 100000  # block (bisa disesuaikan)

def calculate_reward(block_height: int) -> float:
    halvings = block_height // HALVING_INTERVAL
    reward = INITIAL_REWARD / (2 ** halvings)
    return round(reward, 8)  # agar tetap akurat seperti Chip (0.00000001)
