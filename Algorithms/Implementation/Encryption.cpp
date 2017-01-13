// https://www.hackerrank.com/challenges/encryption
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main(){
    string s;
    cin >> s;
    int len = s.length();
    int r = floor(sqrt(len));
    int c = ceil(sqrt(len));
    if(r*c < len) r = c;
  
    for(int i=0;i<c;i++){
        for(int j=0;j<r;j++){
            if(i+j*c < len) cout << s[i+j*c];
        }
        cout << " ";
    }
    return 0;
}
