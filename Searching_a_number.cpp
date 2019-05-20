/* Problem Source-  https://practice.geeksforgeeks.org/problems/searching-a-number/0   */  

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, m = -1;
    long int n, k;
    long int a[100000];
    scanf("%d", &t);
    while(t--){
        scanf("%ld %ld", &n, &k);
        for(int i=1; i<=n; i++){
            scanf("%ld", &a[i]);
        }
        for(int j=1; j<=n; j++){
            if(a[j]==k){
                m = j;
                break;
              }
            }
        printf("%d \n", m);
                m = -1;
        }
    }
