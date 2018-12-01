#include <iostream>
#include <fstream>
using namespace std;

ifstream f("in.txt");

int main(){

    int x, s = 0;
    while (!f.eof()){
        f >> x;
        s+= x;
    }
    cout << s;
}
