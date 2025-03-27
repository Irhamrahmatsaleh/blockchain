TARGET_BLOCK_TIME = 10  # dalam detik, target waktu ideal antar block
MAX_DIFFICULTY = 32
MIN_DIFFICULTY = 1

def adjust_difficulty(previous_duration: float, current_difficulty: int) -> int:
    if previous_duration < TARGET_BLOCK_TIME:
        new_difficulty = current_difficulty + 1
    elif previous_duration > TARGET_BLOCK_TIME:
        new_difficulty = current_difficulty - 1
    else:
        new_difficulty = current_difficulty

    # Batasi dalam range aman
    return max(MIN_DIFFICULTY, min(MAX_DIFFICULTY, new_difficulty))
