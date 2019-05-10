/* Rotate Array - GeeksforGeeks
. 
This is a problem for rotate an array.
   
We need to use vector & rotate function.  

Problem Link - https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0
*/



#include <bits/stdc++.h>

using namespace std;

int
main ()
{

  vector < int >myvector;

  int T, N, D;

  cin >> T;

  while (T--)
    {
      cin >> N >> D;
      for (int i = 0; i < N; i++)
	{
	  int input;
	  cin >> input;
	  myvector.push_back (input);
	}

      rotate (myvector.begin (), myvector.begin () + D, myvector.end ());

      for (int i = 0; i < N; i++)
	{
	  cout << myvector[i] << ' ';
	}
      cout << endl;
      myvector.clear ();
    }
}
