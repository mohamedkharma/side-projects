#include <iostream>
using namespace std;

int main(){
    const int increase_rate= 2;
    float penny=0.01;
    int number_of_days;
    float total=0;
    
    cout<< "Enter the number of days you worked for: ";
    while(!(cin>>number_of_days)||(number_of_days<1)){
        cout<< "ERROR: enter an acceptable nuber: ";
        cin.clear();
        cin.ignore();
    }
    
    cout<<"\n  Days    Salary\n";
    cout<< "----------------------\n";
//   cout << setprecision(2)<<fixed;
    for(int i=0; i<number_of_days; i++)
    {
        total += penny;
        cout <<"  "<<(i+1)<<"      $";
        cout<< penny <<endl;
        penny *= increase_rate;
    }
     cout <<"\nTotal salary for "<<number_of_days<<" days= $"<<total<<endl; 
    return 0;
}