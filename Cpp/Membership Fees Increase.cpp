#include <iostream>
using namespace std;

int main(){
    const double charges= 2500;
    const double increase_by_year=.04;
    double fee= charges;
    
    for (int i=1; i<6; i++)
    {
        fee += (fee* increase_by_year);
        cout <<"Fees for Year "<<i<<" = "<<fee<<endl;
    }

    return 0;
}