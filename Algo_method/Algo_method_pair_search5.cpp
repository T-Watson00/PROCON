#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

//回文判定

bool palindrome_str(string x) {
    int a = x.size() ;
    bool b = true ;
    for (int j=0 ; j<(a+1)/2; j++) {
    if (x[j] != x[a-1-j]) {
            b = false ;
        }
    }
    return b ;
}

bool palindrome_int(int x) {
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
    int N ;
    cin >> N ;
    string S ;
    cin >> S ;
    int count=0 ;
    for (int i=0 ; i<N-1 ; i++) {
        for (int j=i+1 ; j<N ; j++) {
            if (S.at(i)==S.at(j)) {
                count++ ;
            }
        }
    }
    cout << count << endl;
    return 0;
}