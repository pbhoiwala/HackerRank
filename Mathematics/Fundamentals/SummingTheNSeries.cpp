// https://www.hackerrank.com/challenges/summing-the-n-series
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int T; cin >> T;
    const long x = 1000000000 + 7;
    // Tn = [n^2 - (n-1)^2] = [2n-1]
    // Sn = n^2 = n*n - Arithmetic progression
    for(int i=0; i<T; i++){
        long n; cin >> n;
      // Sn = n*n
        cout << ((n%x) * (n%x)) % x << endl;
    }
    return 0;
}
