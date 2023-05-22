#include <iostream>
#include <string>
using namespace std;

class node
{
public:
    string name;
    node *child[10];
    
};
class GT
{
    node *root;

public:
    void create_tree()
    {
        int ch;
        node *root = new node;
        cout << "\nEnter The Name Of Unit :";
        cin >> root->name;
        cout << "Enter The No. Of Chapter  :";
        cin >> ch;
        cout << "Enter The Name Of Chapters";
        for (int i = 0; i < ch; i++)
        {
            node *temp = new node;
            cin >> temp->name;
            temp->child[i] = temp;
        }
    }
    void insert()
    {
        string nm;
        cout<<"Enter The Name Of Chapter to add Topic to it : ";
        cin>>nm;
        // if()pa

        cout<<"Enter The Name Of Topics In chater";

    }
};

int main()
{
    GT a;
    a.create_tree();


    return 0;
}