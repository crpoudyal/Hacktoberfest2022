// rock,paper,scissors.....

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
	int i, n, comp, countComWin = 0, countYouWin = 0;
	char stone, paper, scissor;

	srand(time(NULL));

	printf("\n LET'S PLAY ROCK PAPER SCISSORS!");
	printf("\n THERE WILL BE A TOTAL OF NINE ROUNDS AND YOU HAVE TO SCORE 5");
	printf("\n HERE ARE THE RULES...");
	printf("\n TYPE '0' FOR ROCK, '1' FOR PAPER AND '2' FOR SCISSORS");
	printf("\n LET'S SEE WHO WINS!!!");
	for (i = 1; i < 10;)
	{ 
		comp = rand() % 3;
		if (i == 1)
			printf("\n ....FIRST ROUND....");
		if (i == 2)
			printf("\n ....SECOND ROUND....");
		if (i == 3)
			printf("\n ....THIRD ROUND....");
		if (i == 4)
			printf("\n ....FOURTH ROUND....");
		if (i == 5)
			printf("\n ....FIFTH ROUND....");
		if (i == 6)
			printf("\n ....SIXTH ROUND....");
		if (i == 7)
			printf("\n ....SEVENTH ROUND....");
		if (i == 8)
			printf("\n ....EIGHTH ROUND....");
		if (i == 9)
			printf("\n ....NINTH ROUND....");
		    printf("\n I HAVE CHOSEN A NUMBER ... I GUESS YOU HAVE TOO ... LET'S SEE WHO WINS... : ");
		    scanf("%d", &n);

		if (n == 0)
			printf("\n You have chosen Rock");
		else if (n == 1)
			printf("\n You have chosen Paper");
		else if (n == 2)
			printf("\n You have chosen Scissor");
		else
			printf("\n Wrong Input");

		if (comp == 0)
			printf("\n Computer have chosen Rock");
		else if (comp == 1)
			printf("\n Computer have chosen Paper");
		else if (comp == 2)
			printf("\n Computer have chosen Scissor");
		else
			printf("\n Wrong Input");

		if (n == comp)
		{
			printf("\n\n\t Tie\n");
		}
		if ((n == 0 && comp == 1) || (n == 1 && comp == 2) || (n == 2 && comp == 0))
		{
			printf("\n\n\t Computer won the round\n");
			i++;
			countComWin++;
		}
		if ((n == 0 && comp == 2) || (n == 1 && comp == 0) || (n == 2 && comp == 1))
		{
			printf("\n\n\t You won the round\n");
			i++;
			countYouWin++;
		}

		if (countComWin == 5 || countYouWin == 5)
		{
			printf("\n COMP=%d and YOU=%d", countComWin, countYouWin);

			break;
		}
	}

	if (countComWin > countYouWin)
		printf("\n\n\n\t\t*SORRY...COMPUTER WINS THE MATCH*\n\n\n");
	else if (countComWin < countYouWin)
		printf("\n\n\n\t\t**CONGRATS...YOU WIN THE MATCH*\n\n\n");
	else
		printf("\n\n\n\t\t**MATCH DRAW*\n\n\n");

	return 0;
}

