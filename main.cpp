#include <iostream>
#include <vector>

#include "ShuntingYardAlgorithm.h"

#include "Solution224.h"
int main() {
//    std::string s;
//    s.push_back('1');
//    s.push_back('2');
//    s.push_back('a');
//    s.push_back('%');
//    std::cout << s << std::endl;

    Solution224 * solution224 = new Solution224();
    //int result = solution224->calculate("(1+(4+5+2)-3)+(6+8)");
//    int result1 = solution224->calculate("(1+(2+3))");
//    int result2 = solution224->calculate("2*2+2");
//    int result3 = solution224->calculate("2+2*2");
//    int result4 = solution224->calculate("2*(2+2)");
    int result5 = solution224->calculate(" 2-1 + 2 ");
//    std::cout << result4 << std::endl;
//    std::cout << result3 << std::endl;
//    std::cout << result2 << std::endl;
//    std::cout << result1 << std::endl;
    std::cout << result5 << std::endl;


//    ShuntingYardAlgorithm *s = new ShuntingYardAlgorithm();
//    s->start("");

    return 0;
}
