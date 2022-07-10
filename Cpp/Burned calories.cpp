#include <iostream>
using namespace std;

int main()
{
 const double buring_cal=3.6;
 double number_of_cal_burned= 0;
 
 for(int i=5; i<=30; i+=5)
 {
    number_of_cal_burned= (i* buring_cal);
     cout << "You burned about " <<number_of_cal_burned<< " after "<<i<<" mintues of runing"<<endl;
 }
    return 0;
}
