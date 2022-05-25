#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;


bool palindrome(int x) {
    string y = to_string(x) ;
    int a = y.size() ;
    bool b = true ;
    if (a == 1) {
        return b ;
    }
    else {
        for (int j=0 ; j<(a+1)/2; j++) {
            if (y[j] != y[a-1-j]) {
                b = false ;
                }
            }
        return b ;
    }
}

int main() {
    int L,R ;
    cin >> L >> R ;
    int count = 0 ;
    for (int i=L ; i <= R ; i++) {
        if (palindrome(i) == true) {
            count++;
        }
    }
    cout << count << endl ;
    return 0;
}