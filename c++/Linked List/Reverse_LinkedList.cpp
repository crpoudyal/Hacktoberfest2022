#include <bits/stdc++.h>
using namespace std;

class Node
{
    public:
    int data;
    Node *next;
    Node(int data)
    {
        this->data = data;
        next = NULL;
    }
};

class LinkedList
{
    public:
    Node *head;
    LinkedList()
     { 
        head = NULL; 
     }

    //  Function to reverse the linked list 

    void reverseLinkedList()
    {
        
        Node *current = head;
        Node *prev = NULL, *next = NULL;

        while (current != NULL)
        {
            
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }

    //  Function to print linked list 

    void print()
    {
        struct Node *temp = head;
        while (temp != NULL)
        {
            cout << temp->data << " ";
            temp = temp->next;
        }
    }

    void push(int data)
    {
        Node *temp = new Node(data);
        temp->next = head;
        head = temp;
    }
};


int main()
{

    LinkedList ll;
    ll.push(10);
    ll.push(20);
    ll.push(30);
    ll.push(40);

    cout << "Original Linked List-"<<endl;
    ll.print();
    cout<<endl;

    ll.reverseLinkedList();

    cout << "Reversed linked list-"<<endl;
    ll.print();
    return 0;
}