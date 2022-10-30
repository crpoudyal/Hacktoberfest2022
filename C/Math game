#include <iostream> 
#include <windows.h>
#include <cmath>
#include <time.h>
#include <conio.h>
#include <fstream>
#include <string>
#include <iomanip>
#include <cstdio>


using namespace std;

int j;
int score(0);
string FF;

int main() 
{ 
cout << endl;
while (true)
{

j=0;
score=0;


/* Introduction : */ 
	{
	Beep(0,300);Beep(2000,100);
	cout<<"Welcome to";
	Beep(0,600);
	cout<<" MATH QUIZ GAME!                                           ";
	Beep(2000,100);Beep(1500,100);Beep(2000,100);Beep(1500,100);Beep(2000,700);Beep(0,400);
	cout<<"\n\n=========================\n\nPleas enter your name : ";
	cin>>FF;
	cout<<"\n\n=========================\n\nHello "<<FF<<" !\n\n";
	Beep(0,700);
	for (int a=5; a>0 ; a--)
	{
		cout<<"\rGet ready to play in :  "<<a;
    	Beep(2000,300);Beep(0,700);
	}
    cout<<"\r=========================\n\n";
    Beep(0,500);
	}


/* Level 1 */
	{
		cout << "LEVEL 1 : Adding Quiz ( YOU HAVE ONLY 5 SECONDS TO SOLVE EACH QUESTION )\n-----------------------------------------------------------------------\n\n";
		Beep(0,4000);
		for ( int i=1; i<=5; i++)
		{
			srand(time(0));
			int A = rand()%10+1+10*(i-1);
			int B = rand()%10+1+10*(i-1);
			cout << "Question" << i << " ::  " << A << " + " << B << " = ";
			int numInput;
    		time_t start = time(0);
			int y=5;
    		while ( !kbhit() )
    		{
        		if (abs(time(0) - start) > 5)
				{
					j=1;
					break;
				}
    		}
    		if (j==1)
			{
				cout << "Time's Up!!";
				j=2;
 			}
			 else
			{
 				cin >> numInput;
				if ((time(0)-start)>5)
				{
					cout << "Time's Up!!";
					j=2;
				}
    			else if ( numInput == A+B ) cout << " GOOOOD!!!!\n\n";
    			else
				{
					cout << "Wrong Answer!!";
					j=2;
				}
			}
			if (j==2) break;
			{
				Beep(2000,100);Beep(1500,100);Beep(2000,100);Beep(1500,100);Beep(2000,700);Beep(0,400);
			}
			score+=10;
		}
	}
	
	
/* Level 2 */
	
		for (int Y=1 ; j!=2 && Y!=2 ; Y++)
		{
		cout << "LEVEL 2 : Subtracting Quiz ( YOU HAVE ONLY 5 SECONDS TO SOLVE EACH QUESTION )\n-----------------------------------------------------------------------\n\n";
		Beep(0,4000);
		for ( int i=1; i<=5; i++)
		{
			srand(time(0));
			int A,B;
			int H = rand()%100+1;
			int K = rand()%100+1;
			if (H>=K)
			{
			 A=H;
			 B=K;
			}
			else
			{
				A=K;
				B=H;
			}
			cout << "Question" << i << " ::  " << A << " - " << B << " = ";
			int numInput;
    		time_t start = time(0);
			int y=5;
    		while ( !kbhit() )
    		{
        		if (abs(time(0) - start) > 5)
				{
					j=1;
					break;
				}
    		}
    		if (j==1)
			{
				cout << "Time's Up!!";
				j=2;
 			}
			 else
			{
 				cin >> numInput;
				if ((time(0)-start)>5)
				{
					cout << "Time's Up!!";
					j=2;
				}
    			else if ( numInput == A-B ) cout << " GOOOOD!!!!\n\n";
    			else
				{
					cout << "Wrong Answer!!";
					j=2;
				}
			}
			if (j==2) break;
			{
				Beep(2000,100);Beep(1500,100);Beep(2000,100);Beep(1500,100);Beep(2000,700);Beep(0,400);
			}
			score+=10;
		}
		}
    
    
    
   
    
/* Level 3  */
	
		for (int Y=1 ; j!=2 && Y!=2 ; Y++)
		{
		cout << "LEVEL 3 : Multiplication Quiz ( YOU HAVE ONLY 5 SECONDS TO SOLVE EACH QUESTION )\n-----------------------------------------------------------------------\n\n";
		Beep(0,4000);
		for ( int i=1; i<=5; i++)
		{
			srand(time(0));
			int A = rand()%(5*i)+1;
			int B = rand()%(5*i)+1;
			cout << "Question" << i << " ::  " << A << " x " << B << " = ";
			int numInput;
    		time_t start = time(0);
			int y=5;
    		while ( !kbhit() )
    		{
        		if (abs(time(0) - start) > 5)
				{
					j=1;
					break;
				}
    		}
    		if (j==1)
			{
				cout << "Time's Up!!";
				j=2;
 			}
			 else
			{
 				cin >> numInput;
				if ((time(0)-start)>5)
				{
					cout << "Time's Up!!";
					j=2;
				}
    			else if ( numInput == A*B ) cout << " GOOOOD!!!!\n\n";
    			else
				{
					cout << "Wrong Answer!!";
					j=2;
				}
			}
			if (j==2) break;
			{
				Beep(2000,100);Beep(1500,100);Beep(2000,100);Beep(1500,100);Beep(2000,700);Beep(0,400);
			}
			score+=10;
		}
		}
	
	
	
/* Level 4  */
	for (int Y=1 ; j!=2 && Y!=2 ; Y++)
	{
	
	
		cout << "LEVEL 4 : FINAL QUESTION ( 10 SECONDS TO SOLVE!!!!! )\n-----------------------------------------------------------------------\n\n";
		Beep(0,4000);
			srand(time(0));
			int A = rand()%(10)+6;
			cout << "Final Question" << " ::  " << A << " + " << A << " x " << A << " = ";
			int numInput;
    		time_t start = time(0);
			int y=5;
    		while ( !kbhit() )
    		{
        		if (abs(time(0) - start) > 10)
				{
					j=1;
					break;
				}
    		}
    		if (j==1)
			{
				cout << "Time's Up!!";
				j=2;
 			}
			 else
			{
 				cin >> numInput;
				if ((time(0)-start)>10)
				{
					cout << "Time's Up!!";
					j=2;
				}
    			else if ( numInput == A+A*A ) cout << " GOOOOD!!!!\n\n";
    			else
				{
					cout << "Wrong Answer!!";
					j=2;
				}
			}
			if (j==2) break;
			{
				Beep(2000,100);Beep(1500,100);Beep(2000,100);Beep(1500,100);Beep(2000,700);Beep(0,400);
			}
			score+=10;
	}
	
/* Game Over */
{
	if (j==2)
			{
				cout << "\n\nGAME OVER!!!!!\nYour Score (( " << score << " ))\n\n";
				Beep(2000,300);Beep(1700,300);Beep(1400,300);Beep(1100,1000);	
			}
}

/* Top */
{
	string names[3], firstname, secondname, thirdname;
	int scores[3]; 
	int test,first(-1),second(-1),third(-1);
	
	ifstream xx;
	xx.open("Top.txt");
	for (int i=0; i<=2 ;i++)
	{
		xx >> names[i];
		xx >> scores[i];
	}
	
	cout << " -------BEST SCORES-------\n\n     Names     Scores\n\n";
		
	for (int h=0 ; h<=3 ; h++)
	{
		if (h==3) test = score;
		else test = scores[h];
		if ( test > first )
		{
			first = test;
			if (h==3) firstname = FF;
			else firstname = names[h];
		}
	}
	
	for (int h=0 ; h<=3 ; h++)
	{
		if (h==3) test = score;
		else test = scores[h];
		if ( test > second && test != first )
		{
			second = test;
			if (h==3) secondname = FF;
			else secondname = names[h];
		}
	}
	for (int h=0 ; h<=3 ; h++)
	{
		if (h==3) test = score;
		else test = scores[h];
		if ( test > third && test != first && test != second)
		{
			third = test;
			if (h==3) thirdname = FF;
			else thirdname = names[h];
		}
	}
	xx.close();
	ofstream yy;
	yy.open("Top.txt");	
	yy << firstname << " " << first << " " << secondname << " " << second << " " << thirdname << " " << third;
	cout << setw(10) << firstname << setw(11) << first << endl;
	cout << setw(10) << secondname << setw(11) << second << endl;
	cout << setw(10) << thirdname << setw(11) << third << endl;
	
}

cout << "\n\nPRESS ( THE FIRST LETTER OF YOUR NAME ) TO PLAY AGAIN!";
while (true)
{
	if ( kbhit() )
	{
		cout << "\r";
		break;
	}
}
}

return 0;
}
