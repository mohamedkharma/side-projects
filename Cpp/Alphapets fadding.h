#include <iostream>
#include <algorithm>
using namespace std;

void fadding_latters(string str) {
    int len = str.length();
    
    
    for (char i= 'a'; i <= 'z'; i++) {
        for (int j= 0; j<len; j++) {
            if (i == str[j]){
            cout << str << " - no more: "<< i << endl;
            str.erase(remove(str.begin(), str.end(), i), str.end());
            }
        }
    }
}

int main() {
    string str;
    //str = "abcdefghijklmnopqrstuvwxyz";
    str = "i love you";
    fadding_latters(str);
    return 0;
}