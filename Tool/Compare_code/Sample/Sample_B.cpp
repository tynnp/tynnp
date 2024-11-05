#include <bits/stdc++.h>
using namespace std;

int tong(int n) {
    int ketqua = 0;
    while (n) {
        ketqua += n % 10;
        n /= 10;
    }
    return ketqua;
}

bool check(int n) {
    if (n <= 1)
        return false;
    if (n == 2)
        return true;
    for (int i = 2; i <= sqrt(n); ++i) {
        if (n % i == 0)
            return false;
    }
    return true;
}

bool check(int a, int b) {
    if (tong(a) < tong(b)) return true;
    if (tong(a) == tong(b)) return a > b;
    return false;
} 

void reverseSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int j = i;
        while (j > 0 && check(arr[j-1], arr[j])) {
            swap(arr[j-1], arr[j]);
            j--;
        }
    }
}
 
int main() {
    int n;
    cin >> n;
    
    int arr[n];
    for (int i = 0; i < n; i++) 
        cin >> arr[i];
    
    for (int i = 0; i < n; i++) 
        if (check(tong(arr[i])))
            cout << arr[i] << " ";
    cout << endl;
    
    reverseSort(arr, n);
    for (int x : arr)
        cout << x << " ";
    
    return 0;
}