//only postive number and if you enter number like 4 it will do 1+2+3+4=10
#include <iostream>
using namespace std;

int main(){
    int user_num;
    int total =0;
    
    cout <<"\nEnter a postive number number: ";
    cin>> user_num;
    
    while (user_num < 0){
        cout<< "ERROR: postive number must be chosen\n";
        cout << "Enter a positve number: ";
        cin>>user_num;
    }
    for (int i=1; i<=user_num; i++){
        total +=i;
    }
    
    cout<< "Total= "<<total<<endl;
    return 0;
}