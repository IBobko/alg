//
// Created by igor on 2/5/23.
//

#ifndef UNTITLED_SOLUTION224_H
#define UNTITLED_SOLUTION224_H

#include <string>

class Solution224 {
    /**
     * We need to have list of operators and their prioritize.
     */
    std::string operators = "*/-+";
public:
    int calculate(std::string input);
    std::string toPolishNotation(std::string input);
    bool isOperand(char c);
    bool isOperator(char c);
    int getPrecedence(char op);
};

#endif //UNTITLED_SOLUTION224_H
