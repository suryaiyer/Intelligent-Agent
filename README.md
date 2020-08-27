Mancala AI

Creating and intelligent Agent which plays the Mancala game and selects moves using search algorithms

Python files:
- mancala.py: basic simulation, board design, and random moves.
- Minimax.py: has minimax algorithm
- abpruning.py: has alpha beta pruning algorithm
- eval_functions.py: calculate the score, utility, move
- h_abpruning.py: has heuristic alpha beta pruning algorithm
- h_minimax.py: has heuristic minimax algorithm

Other files:
- AlphaBeta_4_2.txt: program output for experiment with 4 pits with 2 stones each running alpha beta pruning
- Minimax_4_2.txt: program output for experiment with 4 pits with 2 stones each running minimax
- heuristic_alphabeta_4_2.txt: program output for experiment with 4 pits with 2 stones each running heuristic alpha beta pruning
- heuristic_minimax_4_2.txt: program output for experiment with 4 pits with 2 stones each running heuristic minimax
- heuristic_alphabeta_6pits_4stones.txt: program output for experiment with 6 pits with 4 stones each running heuristic alpha beta pruning
- heuristic_minimax_6pits_4stones.txt: program output for experiment with 6 pits with 4 stones each running heuristic minimax


Player options:
- Human: hu
- Random: ra
- Minimax: mi
- Alpha Beta Pruning: ab
- Heuristic Minimax: hm
- Heuristic Alpha Beta Pruning: ha

To play:
  - python mancala.py player1 player2 filename.type
  - i.e. python mancala.py ra ra test.txt  //this will play random vs random and save output to a txt file
  - Player 1 plays first!! Also corresponds to p1 , Player 2 corresponds to p0 in the game 
