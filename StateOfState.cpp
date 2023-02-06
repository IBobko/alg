//
// Created by igor on 2/4/23.
//

#include "StateOfState.h"

#include <iostream>
#include <vector>

/**
 * The start state cannot be an accepting state, because that would imply that an empty string (ε)
 * would accept the language. However, because we need at least an a in the string, an empty
 * string cannot be valid.
 */

int STR_SIZE = 5;

class State {
    char _match;
public:
    explicit State(char match) : _match(match) {}

    bool validate(char value) {
        return value == _match;
    }

    std::vector<State *> possibleNext;
};


bool traverse(State *s, const char param[], int index) {
    if (s->validate(param[index])) {
        if (index + 1 == STR_SIZE) {
            std::cout << "The end." << std::endl;
            return true;
        }
        for (auto &i: s->possibleNext) {
            if (traverse(i, param, index + 1)) {
                return true;
            }
        }
        return false;
    } else {
        return false;
    }
}
//
//int main() {
//    State T('a');
//    T.possibleNext.push_back(&T);
//    State F('b');
//    F.possibleNext.push_back(&F);
//
//    auto *initial = new State('\0');
//    initial->possibleNext.push_back(&T);
//    initial->possibleNext.push_back(&F);
//
//    char const *inputsTrue = "\0aaaaa";
//    char const *inputsFalse = "\0bbbbb";
//
//    if (traverse(initial, inputsTrue, 0)) {
//        std::cout << "Result: a+" << std::endl;
//    }
//
//    if (traverse(initial, inputsFalse, 0)) {
//        std::cout << "Result: b+" << std::endl;
//    }
//    return 0;
//}
