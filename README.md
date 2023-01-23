# Game_Simulations

Consider a 3-person game that is played multiple times per day. This game involves various random factors that are outside the control of the players of the game, so it is not guaranteed that the best-performing player will win each game. Suppose furthermore that, based on tens of thousands of games of historical data, a player can estimate his or her probability of winning a particular game independently of all other games as the proportion of historical games that he or she won. A player's day is considered to be successful if and only if the proportion of games won is above some minimum threshold.

In this project I ran two simulations to explore the following two questions:

1. **On an average day, what is the probability that the player will be successful?**
2. **On an average day, how many maximal losing streaks of various sizes should a player expect?**

## On an average day, what is the probability that the player will be successful?

This question is explored in [Simulating_Daily_Win_Totals.ipynb](https://github.com/nateofspades/Game_Simulations/blob/master/Simulating_Daily_Win_Totals.ipynb). The simulation assumes that the player plays **n_games** = 100 games per day for **n_days** = 100000000 days, and that the player must win a minimum proportion of **min_prop_games_won** = 0.3551 of his or her games in a day for that day to be successful. At the bottom of the notebook you can see, **prop_days**, the proportion of successful days in the simulation, for various values of **p_win_game**, the player's probability of winning a particular game independently of all other games.

## On an average day, how many maximal losing streaks of various sizes should a player expect?

This question is explored in [Simulating_Losing_Streaks.ipynb](https://github.com/nateofspades/Game_Simulations/blob/master/Simulating_Losing_Streaks.ipynb). A **maximal losing streak** means a losing streak of games that is not contained in a larger losing streak. For example, if we let 'W' represent a game won and 'L' represent a game lost, then the 10-game sequence 'WLLWLLLLWW' has a maximal losing streak of 2 games and a maximal losing streak of 4 games, and no other maximal losing streaks.

The simulation assumes that the player plays **n_games** = 100 games per day for 10000000 days. At the bottom of the notebook you can see various **loss_streak_array**'s, each representing the daily average number of maximal streaks of various sizes for a different value of **p_win_game**, the player's probability of winning a particular game independently of all other games.
