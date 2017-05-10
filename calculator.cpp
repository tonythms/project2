// Copyright [2017] <Tony>
# include <iostream>
using std::cout;
using std::cin;

int main() {
    char op;
    float num1, num2;

    cout << "Enter operator either + or - or * or /: ";
    cin >> op;

    cout << "Enter two operands: ";
    cin >> num1 >> num2;

    switch (op) {
        case '+':
            cout << num1+num2;
            break;

        case '-':
            cout << num1-num2;
            break;

        case '*':
            cout << num1*num2;
            break;

        case '/':
            cout << num1/num2;
            break;

        default:
            // If other operator then an error message is shown
            cout << "Error! operator is not correct";
            break;
    }

    return 0;
}
