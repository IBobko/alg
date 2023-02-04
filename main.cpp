#include <iostream>
#include <vector>

int STR_SIZE = 5;

class State {
    char _match;
public:
    explicit State(char match) : _match(match) {}

    bool isMatch(char value) {
        return value == _match;
    }

    std::vector<State *> possibleNext;
};


bool traverse(State *s, const char param[], int index) {
    if (s->isMatch(param[index])) {
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

int main() {
    State T('a');
    T.possibleNext.push_back(&T);
    State F('b');
    F.possibleNext.push_back(&F);

    char const *inputsTrue = "aaaaa";
    char const *inputsFalse = "bbbbb";


    if (traverse(&T, inputsTrue, 0)) {
        std::cout << "Result: true+" << std::endl;
    }

    if (traverse(&F, inputsFalse, 0)) {
        std::cout << "Result: false+" << std::endl;
    }


    return 0;
}
