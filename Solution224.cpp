//
// Created by igor on 2/5/23.
//

#include <iostream>
#include <algorithm>
#include <stack>
#include "Solution224.h"

int Solution224::calculate(std::string input) {
    std::cout << "Original expression: " << input << std::endl;
    std::cout << "Polish notation: " << toPolishNotation(input) << std::endl;

    const std::string &polish = toPolishNotation(input);
    std::stack<int> operands;
    for (char current: polish) {
        if (isOperand(current)) {
            operands.push(current - '0');
        }
        if (isOperator(current)) {
            int &op1 = operands.top();
            operands.pop();
            int &op2 = operands.top();
            operands.pop();
            switch (current) {
                case '+': {
                    operands.push(op1 + op2);
                    break;
                }
                case '-': {
                    operands.push(op2 - op1);
                    break;
                }
                case '*': {
                    operands.push(op1 * op2);
                    break;
                }
                case '/': {
                    operands.push(op2 / op1);
                    break;
                }
            }
        }
    }

    return operands.top();
}

std::string Solution224::toPolishNotation(std::string input) {
    std::string tmpOperators;
    std::string output;
    for (char currentSymbol: input) {
        if (isOperand(currentSymbol)) {
            output.push_back(currentSymbol);
        }
        if (isOperator(currentSymbol)) {
            if (!tmpOperators.empty()) {
                char &backOp = tmpOperators.back();
                if (backOp != '(') {
                    if (getPrecedence(backOp) >= getPrecedence(currentSymbol)) {
                        output.push_back(backOp);
                        tmpOperators.pop_back();
                    }
                }
            }
            tmpOperators.push_back(currentSymbol);
        }
        if (currentSymbol == '(') {
            tmpOperators.push_back(currentSymbol);
            continue;
        }
        if (currentSymbol == ')') {
            while (true) {
                if (tmpOperators.empty()) {
                    break;
                }
                char &backOp = tmpOperators.back();
                if (backOp != '(') {
                    output.push_back(backOp);
                    tmpOperators.pop_back();
                } else {
                    tmpOperators.pop_back();
                    break;
                }
            }
        }
    }
    while (!tmpOperators.empty()) {
        output.push_back(tmpOperators.back());
        tmpOperators.pop_back();
    }
    return output;
}

bool Solution224::isOperand(char c) {
    return c >= '0' && c <= '9';
}

bool Solution224::isOperator(char c) {
    for (int i = 0; i < 5; i++) {
        if (c == operators[i]) return true;
    }
    return false;
}

int Solution224::getPrecedence(char op) {
    for (int i = 0; i < 5; i++) {
        if (op == operators[i]) return (i - 5) * -1;
    }
    return -1;
}
