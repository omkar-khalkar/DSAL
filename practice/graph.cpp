#include <iostream>
#include <deque>
#include <string>
using namespace std;

int main()
{
    int n;
    cout << "Enter The Number OF Vertices: ";
    cin >> n;
    int arr[n][n];
    int m, l;

    for (int i = 0; i < n; i++)
    {
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
    int visited[10], visit[10];
    for (int i = 0; i < n; i++)
    {
        visited[i] = 0;
        visit[i] = 0;
    }
    cout << endl;
    int v, k;
    k = 0;
    deque<int> dq;
    cout << "Enter The Starting Node to Start : ";
    cin >> v;
    dq.push_back(v);
    visit[k] = dq.front();
    dq.pop_back();
    visited[v] = 1;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (arr[i][j] == 1 && visited[j] == 0)
            {
                dq.push_back(j);
                visited[j] = 1;
            }
        }
        visit[++k] = dq.front();
        dq.pop_front();
    }

    for (int i = 0; i < n; i++)
    {
        cout << visit[i] << " ";
    }
    cout << endl;

    return 0;
}