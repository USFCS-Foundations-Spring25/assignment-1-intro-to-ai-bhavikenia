from random import randint

def monte_carlo_approach(n):
    win_table = {i: 0 for i in range(n-5, n+1)}
    
    for hold_val in range(n-5, n+1):
        for _ in range(1000000):  # Run 1,000,000 simulations per hold value
            # Player 1's turn
            player1_score = 0
            while player1_score < hold_val:
                player1_score += randint(1, 6)
                if player1_score > n:  # Player 1 busts
                    break
            
            if player1_score > n:  # Player 1 loses immediately
                continue
            
            # Player 2's turn
            player2_score = 0
            while player2_score <= player1_score:
                player2_score += randint(1, 6)
                if player2_score > n:  # Player 2 busts
                    win_table[hold_val] += 1
                    break
            
            if player1_score > player2_score and player2_score <= n:
                win_table[hold_val] += 1  # Player 1 wins
    
    for item in win_table:
        print(f"{item}: {win_table[item] / 1000000:.6f}")



