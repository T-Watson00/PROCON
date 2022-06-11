#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
using namespace std;

int main() {
    double X,A,D;
    int N ;
    cin>>X>>A>>D>>N ;
    double delta_min = pow(10,20) ;
    for (int n= 0 ; n<N ; n++){
        double delta = A+D*n-X ;
        if (delta == lround(delta)){
            delta_min = min(delta_min,fabs(lround(delta))) ;
        }
    }
    cout << delta_min << endl;
    return 0;
}