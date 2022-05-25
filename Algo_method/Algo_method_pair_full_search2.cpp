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
    int L,R ;
    cin >> L >> R ;
    vector<int> A(10) ;
    int count = 0 ;
    for (int i=L ; i <= R ;i++) {
        int x = i % 10 ;
        A[x]++ ;
    }
    for (int j=0 ; j <10 ; j++) {
        if (A[j] > 0) {
            count = count + A[j]*(A[j]-1)/2 ;
        }
    }
    cout << count << endl;
    return 0;
}