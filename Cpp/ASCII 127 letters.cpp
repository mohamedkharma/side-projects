#include <iostream>
using namespace std;

int main()
{
    char ascii_number;
    
    for (int i=0; i<=127; i++){
    ascii_number= i;
    cout<< ascii_number<< "";
    
    if ( i%16 ==0)
        cout <<endl;
    }
    cout <<endl;
    cout <<endl;
        return 0;
}
