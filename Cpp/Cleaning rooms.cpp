#include <iostream>

using namespace std;

int main() {
    int number;
    int big_rooms;
    int small_rooms;
    const double tax = 6.6;
    cout << "Welcome to Mohamed's carpet cleaing service" << endl;
    cout << "\n Charges: \n";
    cout << "       $25 per small room \n       $35 per large room \n";
    
    cout << " \nEnter the number of samll rooms: ";
    cin >> small_rooms;
    cout << "Enter the number of large rooms: ";
    cin>> big_rooms;

    
    if (big_rooms && small_rooms !=number){ 
    cout<< "================================\n";
    cout << "Your Totalestmited carpet cleanig cost is: $"<<(small_rooms*25)+(big_rooms*35)+tax;
    cout << "\nThis estimate is valid for 30 days\n";
    } else { cout<< "Error: This number is not vaild\n";
    
    }
    return 0;
}
