#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

bool palindrome(string x) {
        int a = x.size() ;
        bool b = true ;
        for (int j=0 ; j<(a+1)/2; j++) {
            if (x[j] != x[a-1-j]) {
                b = false ;
            }
        }
        return b ;
    }

int main() {
    int N ;
    cin >> N ;
    vector<string> S(N) ;
    for (int i=0 ;i<N ; i++) {
        cin >> S[i] ;
    }
    int count= 0 ;
    for(int i=0 ; i<N ; i++) {
        if (palindrome(S[i]) == true) {
            count++ ;
        }
    }
    cout << count << endl;
    return 0;
}