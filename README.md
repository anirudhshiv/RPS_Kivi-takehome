# RPS_game

## Implementation
Rock Paper Scissors game implemented with standard rules:
* Rock>Scissors
* Scissors>Paper
* Paper>Rock

This is the core fn, script calls in in a while loop:
> play_rps("","")
* Accepts only lower case "r","p","s"
* While loop terinates only when user picks "n" or "N" for "Play again? (Y/N)" prompt, any other other input triggers a new game

## Testing
play_rps is called with all different permutations so it is exhaustively tested
