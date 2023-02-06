//
// Created by igor on 2/4/23.
//
#include <iostream>
#include "ShuntingYardAlgorithm.h"
#include <vector>


bool isDigit(char c) {
    return c >='0' && c <='9';
}

void ShuntingYardAlgorithm::start(char *) {
    char const * input = "4+5";

    std::string result;
    std::vector<char> operators;


    for (int i = 0; i < 4; i++) {
        if (isDigit(input[i])) {
            std::cout << input[i] << " digit." << std::endl;
            result.push_back(input[i]);
        } else {
            std::cout << input[i] << " not digit." << std::endl;
            operators.push_back(input[i]);
        }

    }

    for (int i = 0; i < operators.size(); i++) {
        result.push_back(operators.at(i));
    }

    std::cout << result << std::endl;

    std::string resultStack;

    for (int i = 0; i < result.size(); i++) {
        std::cout << result.at(i) << std::endl;
        if (isDigit(result.at(i))) {
            resultStack.push_back(result.at(i));
        } else {
            if (result.at(i) == '+') {
                char a = resultStack.back();
                resultStack.pop_back();
                char b = resultStack.back();
                resultStack.pop_back();
                int a1 = a - '0';
                int a2 = b - '0';

                std::cout << a1+a2 << std::endl;


            }
        }

    }

}
