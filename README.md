# modified-chess-game-python


 **Brief Description of How our Program Works and How we formulated each problem:**
	*In the given problem, Initially we defined all the pieces i.e pichu, Pikachu and raichu.
	* We created functions for each element where in we defined their positions and the eligible movements from which they can move or attack the opponent.
	* Later we defined these elements in the successor function where in it appends to the next possible move to a new list.
	* The approach we used here was the ideology of Min-Max algorithm with weights. So we basically gave weights to each elements which helps in taking a sensible move as per the priority set.
	* The cost function we defined gives the cost of each possible move and returns the same with the successor function which helps in making sensible moves in the game.
	* With this approach we were able to achieve a solution that can challenge other models considerably.
**Problems we Faced while Execution:**	
*	We face many problems, while designing the algorithm for the game. The main problem was to define each successor’s movement as it became very lengthy.
	The second problem was to calculate cost and integrating the same for a better move was a bit difficult as the hierarchy we had set with considering the cost was not the best which we updated by trial and error to find the optimal cost.
* 	The execution with considering the opponent’s move was very challenging and took the most part of our time.
*	The map was difficult to traverse and had to be converted into an array. We also faced error in which our player attacking the other didn’t jump in an empty space sometimes and used to jump on the enemy player.
