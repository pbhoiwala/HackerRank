// https://www.hackerrank.com/challenges/sherlock-and-divisors
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int T;
    cin >> T;      
    for(int i=0; i<T; i++){
        int ctr = 0;
        int j = 2;
        int N;
        cin >> N;
        double k = (double)N;
        while(j < k && N%2 == 0){
            k = (double)N/j;
            if(j %2 == 0 && ceil(k) == k) ctr++;
            if(ceil(k) == k && int(k)%2 == 0 && k > j) ctr++;
            j+=1;
        }
        if(N%2 == 0) ctr++;
        cout << ctr << endl;
    }
    return 0;
}