#include <iostream>
using namespace std;

int main() {
    int SecretNum =7;
    int Guess;
	int guessCount=0;
	int guesslimit=3;
	bool outofguesses= false;
    
    do {
    
	if(guessCount < guesslimit){
	cout << "Enter your guess: ";
    cin >>Guess;
	guessCount++;
	} else{
	outofguesses= true;
	}
    }
    while (SecretNum != Guess && !outofguesses);
    
    if(outofguesses){
	cout<<"you lose!";
	} else{
	cout<<" you Win!!"<<endl;
    }  return 0;

}