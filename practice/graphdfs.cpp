#include <iostream>
#include <stack>
#include <string>
using namespace std;
int arr[10][10];
int visited[10], visit[10];
int n;
stack<int> s;
int k=0;
void dfs(int v)
{

    for (int i = 0; i < n; i++)
    {
        if(arr[v][i]==1 && visited[i]==0)
            s.push(i);
        
            
        
        if(!s.empty())
        {
            visited[s.top()]=1;
            visit[k++]=s.top();
            s.pop();
            dfs(s.top());
        }
    }
}
int main()
{
    cout << "Enter The Number OF Vertices: ";
    cin >> n;

    int m, l;

    for (int i = 0; i < n; i++)
    {
        visited[i] = 0;
        visit[i] = 0;
        for (int j = 0; j < n; j++)
        {
            arr[i][j] = 0;
        }
    }

    int e;
    cout << "Enter The Number Of Edges : ";
    cin >> e;

    for (int i = 0; i < e; i++)
    {
        cout << "Enter The Two Vertices Which Have Edge : ";
        cin >> l >> m;
        arr[m][l] = 1;
        arr[l][m] = 1;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;
    int v;
   

    cout << "Enter The Initial Node to Start : ";
    cin >> v;

    dfs(v);
    for (int i = 0; i < n; i++)
    {
        cout << visit[i] << " ";
    }
    cout << endl;

    return 0;
}