#include <iostream>
using namespace std;

int main()
{
    const double in_level =1.5;
    double millimeters_each_year = 0;
    
    cout <<"-----------------------------------------\n";
    for (int i=1; i<=25; i++)
    {
        millimeters_each_year += in_level;
        cout <<"Year" <<i<<": "<<millimeters_each_year<<" mm"<<endl;
    }
    cout <<"-----------------------------------------\n";
    return 0;
}
