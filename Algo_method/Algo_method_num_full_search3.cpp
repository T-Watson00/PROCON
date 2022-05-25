#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main() {
    int N ;
    cin >> N ;
    int n ;
    n = (sqrt(N)*10)/10 ;
    string result ;
    result = "Yes";
    if (N == 1) {
        result = "No";
    }
    else {
        for (int i = 1 ; i <= n ; i++) {
            if (i == 1) {
                continue;
            }
            if (N % i == 0) {
                result = "No";
                break;
            }
        }
    }
    cout << result << endl;
    return 0;
}
