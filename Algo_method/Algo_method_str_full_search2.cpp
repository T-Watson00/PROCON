#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<numeric>
#include<algorithm>
using namespace std;

int main() {
    string S ;
    cin >> S ;
    string S_reverse (S.rbegin(),S.rend()) ;
    if (S == S_reverse) {
        cout << "Yes" << endl ;
    }
    else {
        cout << "No" << endl ;
    }

    return 0;
}