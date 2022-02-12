#include <iostream>
#include <stack>
using namespace std;

int main(){
    int n;
    int number;
    int sum=0;
    cin >>n;
    stack<int> a;

    for(int i=0; i<n; i++){
        cin >> number;
        if (number != 0){
            a.push(number);
        }
        else{
            a.pop();
        }
    }
    int size =a.size();
    for(int j=0; j< size; j++){
        sum+= a.top();
        a.pop();
    }
    cout << sum<< endl;
    return 0;
}