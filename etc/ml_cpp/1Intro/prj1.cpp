#include <iostream>
#include <eigen3/Eigen/Dense>
#include <vector>

using namespace std;

typedef Eigen::Matrix<float, 3, 3> MyMatrix33f;
typedef Eigen::Matrix<float, 3, 1> MyVector3f;
typedef Eigen::Matrix<float, Eigen::Dynamic, Eigen::Dynamic> MyMatrix;


int main() {
    
    MyMatrix33f a;
    MyVector3f vec;
    MyMatrix m(10, 15);

    a = MyMatrix33f::Zero();
    a = MyMatrix33f::Identity();
    vec = MyVector3f::Random();


    a <<    1,2,3,
            4,5,6,
            7,8,9;

    a(0,0) = 3;

    int data[] = {1,2,3, 4};
    Eigen::Map<Eigen::RowVectorXi> v_map(data, 4);

    vector<float> data2 = {1,2,3,4,5,6,7,8,9};

    Eigen::Map<MyMatrix33f> a_new(data2.data());
    

    return 0;
}
