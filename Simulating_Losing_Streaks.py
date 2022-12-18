import numpy as np

def loss_streak_simulator(n_games=100, p_win_game=0.367):
    """
    This function generates a string of W's (wins) and losses (L's) and counts maximal L-streaks of each size >=3.
    :param n_games: number of games played in 1 iteration of the simulation, representing 1 day of n_games games
    :param p_win_game: winning probability for each game in the simulation
    :return: counts of maximal loss streaks of sizes 3 to 10
    """

    # Generate a string of W's (wins) and L's (losses), e.g. 'WWLLLWL'
    result_string = ''
    for i in range(n_games):
        result = np.random.binomial(1, p_win_game)
        if result == 0:
            result_string += 'L'
        if result == 1:
            result_string += 'W'

    # Eliminate the W's to investigate the losing streaks.
    loss_streak_array = result_string.split('W')
    loss_streak_array = np.array(loss_streak_array)
    loss_streak_array = loss_streak_array[loss_streak_array != '']

    # Count how many maximal losing streaks there are for each length from 4 to 10.
    for loss_streak in loss_streak_array:
        count_3_loss_streak = len(loss_streak_array[loss_streak_array == 'LLL'])
        count_4_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLL'])
        count_5_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLLL'])
        count_6_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLLLL'])
        count_7_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLLLLL'])
        count_8_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLLLLLL'])
        count_9_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLLLLLLL'])
        count_10_loss_streak = len(loss_streak_array[loss_streak_array == 'LLLLLLLLLL'])

    return np.array([count_3_loss_streak, count_4_loss_streak, count_5_loss_streak, count_6_loss_streak,
                    count_7_loss_streak, count_8_loss_streak, count_9_loss_streak, count_10_loss_streak])

# Playing for 10000000 days and averaging how many daily loss streaks there are of each size for different p_win_game
# values (e.g. how many 3-loss streaks on average per day, how many 4-loss streaks on average per day, etc.)

loss_streak_array = np.array([0,0,0,0,0,0,0,0])
for day in range(10000000):
    loss_streak_array += loss_streak_simulator(p_win_game=0.36)
loss_streak_array = loss_streak_array/10000000
print('p_win_game = 0.36:', loss_streak_array)

loss_streak_array = np.array([0,0,0,0,0,0,0,0])
for day in range(10000000):
    loss_streak_array += loss_streak_simulator(p_win_game=0.367)
loss_streak_array = loss_streak_array/10000000
print('p_win_game = 0.367:', loss_streak_array

loss_streak_array = np.array([0,0,0,0,0,0,0,0])
for day in range(10000000):
    loss_streak_array += loss_streak_simulator(p_win_game=0.37)
loss_streak_array = loss_streak_array/10000000
print('p_win_game = 0.37:', loss_streak_array)

loss_streak_array = np.array([0,0,0,0,0,0,0,0])
for day in range(10000000):
    loss_streak_array += loss_streak_simulator(p_win_game=0.375)
loss_streak_array = loss_streak_array/10000000
print('p_win_game = 0.375:', loss_streak_array)