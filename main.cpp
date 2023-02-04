#include <iostream>
#include <vector>

int BOOL_SIZE = 5;

struct State {
    bool match;

    bool isMatch(bool value) {
        return value == match;
    }

    std::vector<State *> possibleNext;
};


bool traverse(State *s, const bool param[], int index) {
    if (index == BOOL_SIZE) {
        std::cout << "The end." << std::endl;
        return true;
    }
    if (s->isMatch(param[index])) {
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

int main() {
    State T;
    T.match = true;
    T.possibleNext.push_back(&T);

    State F;
    F.match = false;
    F.possibleNext.push_back(&F);

    bool *inputsTrue = new bool[BOOL_SIZE];
    inputsTrue[0] = true;
    inputsTrue[1] = true;
    inputsTrue[2] = true;
    inputsTrue[3] = true;
    inputsTrue[4] = true;

    bool *inputsFalse = new bool[BOOL_SIZE];
    inputsFalse[0] = false;
    inputsFalse[1] = false;
    inputsFalse[2] = false;
    inputsFalse[3] = false;
    inputsFalse[4] = false;

    if (traverse(&T, inputsTrue, 0)) {
        std::cout << "Result: true+" << std::endl;
    }

    if (traverse(&F, inputsFalse, 0)) {
        std::cout << "Result: false+" << std::endl;
    }


    return 0;
}
