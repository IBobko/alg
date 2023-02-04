#include <iostream>

struct State {
    bool matched;
    State *FALSE = nullptr;
    State *TRUE = nullptr;
    std::string msg;
};

bool isCorrect1(const bool param[], int index) {
    bool correct = true;
    if (param[index] == correct) {
        if (index + 1 < 5) {
            return isCorrect1(param, index + 1);
        }
        return true;
    } else {
        return false;
    }
}

bool isCorrect2(const bool param[], int index) {
    bool correct = false;
    if (param[index] == correct) {
        if (index + 1 < 5) {
            return isCorrect2(param, index + 1);
        }
        return true;
    } else {
        return false;
    }
}


/*bool traverse(State * t, bool p[],index) {
    if (t->matched == p[0])
    if (p) {
        if (t->TRUE!= nullptr) {
            traverse(t->TRUE, p);
        }
    } else {
        if (t->FALSE!= nullptr) {
            traverse(t->FALSE, p);
        }
    }
    std::cout << t->msg << std::endl;
}
 */

int main() {
    bool *inputs = new bool[5];
    inputs[0] = true;
    inputs[1] = true;
    inputs[2] = true;
    inputs[3] = true;
    inputs[4] = true;

    bool *inputs2 = new bool[5];
    inputs2[0] = false;
    inputs2[1] = false;
    inputs2[2] = false;
    inputs2[3] = false;
    inputs2[4] = false;

    if (isCorrect1(inputs, 0)) {
        std::cout << "Полет нормальный" << std::endl;
    }

    if (isCorrect2(inputs2, 0)) {
        std::cout << "Полет ненормальный" << std::endl;
    }


    return 0;
}
