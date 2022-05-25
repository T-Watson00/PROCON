#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include<numeric>
using namespace std;

int main() {
    string S ;
    cin >> S ;
    int N = S.size();
    int count = 0 ;
    for (int i = 0; i < N -1 ; i++){
        if (S[i] == S[i+1]){
            count++ ;
        }
    }
    cout << count << endl ;


    return 0;
}