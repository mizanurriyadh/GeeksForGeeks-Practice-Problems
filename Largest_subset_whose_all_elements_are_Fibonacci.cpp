#include <bits/stdc++.h>

using namespace std;

int findSubset(int arr[], int n)
{
    int max = *max_element(arr, arr+n);
    
    int a=0, b=1;
    
    unordered_set<int> hash;
    hash.insert(a);
    hash.insert(b);
    
    while(b<max)
    {
        int c = a+b;
        a = b;
        b = c;
        hash.insert(b);
    }
    
    for(int i=0; i<n; i++)
    {
        if(hash.find(arr[i]) != hash.end())
        {
            cout<<arr[i]<<" ";
        }
    }
}


int main()
{
    int arr[] = {4, 2, 8, 5, 20, 1, 40, 13, 23};
    int size = sizeof(arr)/sizeof(arr[0]);
    findSubset(arr, size);
    
    return 0;
}


Output = 2 8 5 1 13 

// Source = https://www.geeksforgeeks.org/largest-subset-whose-all-elements-are-fibonacci-numbers/
