#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int number, guess, nguesses = 1;
    srand(time(0));
    number = rand() % 100 + 1; //generates random number between 1 and 100

    do
    {

        printf("Guess the number between 1 to 100\n");
        scanf("%d", &guess);
        if (guess < number)
        {

            printf("Please put a higher number\n");
        }
        else if (guess > number)
        {

            printf("Please enter a smaller number\n");
        }
        else
        {

            printf("You guessed it in %d attempts\n", nguesses);
        }
        nguesses++;

    } while (guess != number);

    return 0;
}