# include <iostream>
# include <vector>
using namespace std;

void output_vector(vector<int> Vector){
    for(int i=0;i<Vector.size(); i++){
        cout << Vector[i] ;
        if (i!=Vector.size()-1) cout << " ";
        cout << endl ;
    }
}


int main() {
    int N ;
    cin >> N ;
    vector<int> A(N) ;
    for(int i=0;i<N;i++) cin >> A[i] ;
    int X = N / 2;
    


}