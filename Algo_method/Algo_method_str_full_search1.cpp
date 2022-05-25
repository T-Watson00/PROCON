#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;

int main() {
    string S ;
    cin >> S ;
    string c ;
    cin >> c ;
    int place ;
    place = S.find(c);
    if (place == string::npos ) {
        cout << "No" << endl ;
    }
    else {
        cout << "Yes" << endl ;
    }

    return 0;
}