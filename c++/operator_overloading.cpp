#include<iostream>
using namespace std;
class A
{
    int n;
    public : 
    A()
    {
        n=0;
    }
    void get()
    {
        cout<<"Enter any number : ";
        cin>>n;
    }
    void operator ++ (int a)
    {
        n+=1;
    }
    void display()
    {
        cout<<"The number is : "<<n<<endl;
    }
};
int main()
{
    A a1;
    a1.get();
    a1++;
    a1.display();
}