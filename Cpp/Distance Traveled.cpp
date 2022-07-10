#include <iostream>
using namespace std;

int main(){
    int speed;
    int hours_traveled;
    int distance= 0;
   
    cout <<"Enter the speed of the vehical: ";
    while(!(cin>>speed)||(speed<0))
    {
        cout <<"ERROR: number of speed must be greater than 0: ";
        cin.clear();
        cin.ignore();
    }
    cout <<"Enter the hours_traveled of the vehical: ";
    while(!(cin>>hours_traveled)||(hours_traveled<0))
    {
        cout <<"ERROR: number of hours_traveled must be greater than 0: ";
        cin.clear();
        cin.ignore(1200,'\n');
    }
    cout<< "Hours | distance traveled\n";
    cout <<"------------------------\n";
    for (int i=1; i<=hours_traveled; i++){

        distance+= speed;
        cout<< "    " <<(i)<< "    "<<distance<<endl;
    }
    
    
    return 0;
}