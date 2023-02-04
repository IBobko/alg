#include <iostream>

struct State {
    bool match;
};


bool isCorrect(State *s, const bool param[], int index) {
    bool correct = s->match;
    if (param[index] == correct) {
        if (index + 1 < 5) {
            return isCorrect(s, param, index + 1);
        }
        return true;
    } else {
        return false;
    }
}

int main() {
    State T;
    T.match = true;

    State F;
    F.match = false;

    bool *inputsTrue = new bool[5];
    inputsTrue[0] = true;
    inputsTrue[1] = true;
    inputsTrue[2] = true;
    inputsTrue[3] = true;
    inputsTrue[4] = true;

    bool *inputsFalse = new bool[5];
    inputsFalse[0] = false;
    inputsFalse[1] = false;
    inputsFalse[2] = false;
    inputsFalse[3] = false;
    inputsFalse[4] = false;

    if (isCorrect(&T, inputsTrue, 0)) {
        std::cout << "Result: true+" << std::endl;
    }

    if (isCorrect(&F, inputsFalse, 0)) {
        std::cout << "Result: false+" << std::endl;
    }


    return 0;
}
