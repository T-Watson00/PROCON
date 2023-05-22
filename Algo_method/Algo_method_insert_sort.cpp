# include <vector>
# include <iostream>

using namespace std;

void output_vector(vector<int> A){
    for (int i=0;i<A.size();i++){
        cout << A[i] ;
        if (i != A.size()-1) cout << " ";

    }
    cout << endl ;
}


int main() {
    int N;
    cin >> N ;
    vector<int> A(N) ;
    for (int i=0;i<N;i++) cin >> A[i] ;
    for (int j=1;j<N;j++) {
        int k = j ;
        while (k>0 && A[k-1]>A[k]) {
            int tmp = A[k] ;
            A[k] = A[k-1] ;
            A[k-1] = tmp ;
            k-- ;
        }
        output_vector(A) ;
    }



}
