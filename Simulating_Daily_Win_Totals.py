import numpy as np

def win_simulator(n_games=100, p_win_game=0.367, min_prop_games_won=0.3551, n_days=1000000):
    """
    This function calculates the proportion of days in which the proportion of games won is at least min_prop_games_won.
    :param min_prop_games_won: only days where the proportion of wins is at least this value are counted;
                               0.3551 is the pre-bonus break-even rate for the $100 games.
    :param n_games: number of games played in 1 iteration of the simulation, representing 1 day of n_games games
    :param p_win_game: winning probability for each game in the simulation
    :param n_days: number of days of play in the full simulation
    :return: proportion of days where proportion of games won is at least min_prop_games_won
    """

    daily_win_count_array = np.random.binomial(n_games, p_win_game, n_days)
    prop_days_win_at_least_min_prop = len(daily_win_count_array[daily_win_count_array >= min_prop_games_won * n_games]) / n_days

    return prop_days_win_at_least_min_prop

print('p_win_game: 0.36, prop_days:', win_simulator(p_win_game=0.36))
print('p_win_game: 0.363, prop_days:', win_simulator(p_win_game=0.363))
print('p_win_game: 0.367, prop_days:', win_simulator(p_win_game=0.367))
print('p_win_game: 0.370, prop_days:', win_simulator(p_win_game=0.370))
print('p_win_game: 0.373, prop_days:', win_simulator(p_win_game=0.373))