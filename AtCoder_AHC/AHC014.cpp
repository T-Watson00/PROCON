#include <iostream>
#include <vector>
#include <tuple>
#include <string>
#include <set>


using std::cin;
using std::cout;
using std::endl;
using node_pair = std::pair<std::tuple<int,int>,std::tuple<int,int>> ;
using coordinate = std::tuple<int,int> ;

//座標と重みのstruct
struct coordinates_and_distance {
        int x;
        int y;
        int distance_second; // (x-Center)^2+(y-Center)^2+1
    };

//座標とその状態
struct coordinates_and_the_state {
    int x;
    int y;
    std::string coordinate_state = "able"; //状態は "able","disable","marked"の3つ
}
//重みの計算
int Distance_second_from_center(int x,int y,int c) {
    return std::pow(x-c,2)+std::pow(y-c,2)+1;
}


int main() {

    //入力を受ける
    int N,M ;
    cin >> N >> M ;
    int Center = (N-1)/2 ; //中心の座標

    //座標と重みのobjectのsortの関数object
    struct coordinates_and_the_state_sort_by_x {
        bool operator() (const coordinates_and_the_state& a, const coordinates_and_the_state& b) const noexcept {
            return std::tie(a.x,a.y) < std::tie(b.x,b.y) ;
        }
    };
    struct coordinates_and_the_state_sort_by_y {
        bool operator() (const coordinates_and_the_state& a, const coordinates_and_the_state& b) const noexcept {
            return std::tie(a.y,a.x) < std::tie(b.y,b.x) ;
        }
    };
    struct coordinates_and_distance_sort_by_distance {
        bool operator() (const coordinates_and_distance& a, const coordinates_and_distance& b) const noexcept {
            return std::tie(a.distance_second,a.x,a.y) < std::tie(b.distance_second,b.x,b.y) ;
        }
    };


    //座標の入力
    std::set<coordinate> Spotted_Coordinates_set ;
    for (int i=0;i<M;i++) {
        int x,y;
        cin >> x >> y ;
        Spotted_Coordinates_set.insert(std::tie(x,y)) ;
    }

    //処理
    std::vector<coordinates_and_the_state> Coordinates_and_the_state_vector(std::pow(N,2));
    for (int i=0;i<std::pow(N,2);i++) {
        int coordinate_x = i/N ;
        int coordinate_y = i%N ;
        if (Spotted_Coordinates_set.find(std::tie(coordinate_x,coordinate_y)) != end()) {
            Coordinates_and_the_state_vector[i].coordinate_state = "marked" ;
        }
    }
    //斜め方向と水平鉛直方向を分けて考える

    //水平方向
    std::vector<coordinates_and_the_state> Coordinates_and_the_state_for_horizontal_vector = Coordinates_and_the_state_vector ;
    //xの値によってsort
    std::sort(Coordinates_and_the_state_for_horizontal_vector.begin(),Coordinates_and_the_state_for_horizontal_vector.end(),coordinates_and_the_state_sort_by_x{});

    //鉛直方向
    std::vector<coordinates_and_the_state> Coordinates_and_the_state_for_vertical_vector = Coordinates_and_the_state_vector ;
    //yの値によってsort
    std::sort(Coordinates_and_the_state_for_vertical_vector.begin(),Coordinates_and_the_state_for_vertical_vector.end(),coordinates_and_the_state_sort_by_y{}) ;

    std::vector<coordinates_and_the_state> Coordinates_and_the_state_for_diagonal_plus_vector = Coordinates_and_the_state_vector ; //右あがりの辺
    std::vector<coordinates_and_the_state> Coordinates_and_the_state_for_diagonal_minus_vector = Coordinates_and_the_state_vector ;//右下がりの辺

    std::vector<coordinate> Spotted_Coordinates_vector = std::vec(Spotted_Coordinates_set.begin(), Spotted_Coordinates_set.end());
    std::sort(Spotted_Coordinates_vector.begin(),Spotted_Coordinates_vector.end(),coordinates_and_distance_sort_by_distance{});




    //鉛直水平方向の処理










    return 0;
}