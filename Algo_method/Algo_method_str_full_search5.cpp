#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    string S,T ;
    cin >> S >> T ;
    if (S.find(T) == string::npos) {
        cout << "No"<< endl ;
    }
    else {
        cout << "Yes" << endl ;
    }


    return 0;
}