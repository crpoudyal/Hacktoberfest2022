// Create game c++
#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(){
    srand(time(0));
    int number = rand() % 100 + 1;
    int guess;
    int tries = 10;
    bool win = false;
    cout << "Guess My Number Game" << endl;
    while (win == false){
        cout << "Enter a guess between 1 and 100: ";
        cin >> guess;
        tries --;
        if (guess == number){
            win = true;
            break;
        }
        else{
            if (number % 2 == 0 && guess % 2 == 0){
                cout << "You are on the right track, the number is even!" << endl;
            }
            else if (number % 2 == 0 && guess % 2 != 0){
                cout << "The number is even. Try guessing even numbers!" << endl;
            }
            else if (number % 2 != 0 && guess % 2 == 0){
                cout << "The number is odd. Try guessing odd numbers!" << endl;
            }
            else if (number % 2 != 0 && guess % 2 != 0){
                cout << "You are on the right track, the number is odd!" << endl;
            }
            cout << "You have " << tries << " tries left!" << endl << endl;
        }

        cout << "Enter a guess between 1 and 100: ";
        cin >> guess;
        tries --;
        if (guess == number){
            win = true;
            break;
        }
        else{
            if (number % 3 == 0 && guess % 3 == 0){
                cout << "You are on the right track, the number is a multiple of 3!" << endl;
            }
            else if (number % 3 == 0 && guess % 3 != 0){
                cout << "The number is a  multiple of 3. Try guessing such numbers!" << endl;
            }
            else if (number % 5 == 0 && guess % 5 == 0){
                cout << "You are on the right track, the number is a multiple of 5!" << endl;
            }
            else if (number % 5 == 0 && guess % 5 != 0){
                cout << "The number is a  multiple of 5. Try guessing such numbers!" << endl;
            }
            else if (number % 7 == 0 && guess % 7 == 0){
                cout << "You are on the right track, the number is a multiple of 7!" << endl;
            }
            else if (number % 7 == 0 && guess % 7 != 0){
                cout << "The number is a  multiple of 7. Try guessing such numbers!" << endl;
            }
            else{
                cout << "The number is not a multiple of 3, 5 and 7! Try guessing such numbers!" << endl;
            }
            cout << "You have " << tries << " tries left!" << endl << endl;
        }

        while (tries > 0){
            cout << "Enter a guess between 1 and 100: ";
            cin >> guess;
            tries --;
            if (guess > number)        {
                cout << "Too high!" << endl;
                cout << "You have " << tries << " tries left!" << endl << endl;
            }
            else if (guess < number)        {
                cout << "Too low!" << endl;
                cout << "You have " << tries << " tries left!" << endl << endl;
            }
            else        {
                win = true;
                break;
            }
        }
    }

    if (win == true){
        if (10 - tries == 1){
            cout << "Correct! You guessed the number " << number << " in " << 10 - tries << " guess!" << endl << endl;
        }
        else{
            cout << "Correct! You guessed the number " << number << " in " << 10 - tries << " guesses!" << endl << endl;
        }
    }
    else{
        cout << "You were not able to guess the number!" << endl << "The number was " << number << "!" << endl;
    }
    return 0;
}