# 알고리즘 이론 및 정리

#### Modular 규칙
```
(a + b)%c == ((a % c) + (b % c)) % c
```


## K번째 수
[문제 링크 (프로그래머스)](https://programmers.co.kr/learn/courses/30/lessons/42748?language=cpp)

```c++
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    vector<int> temp;
    for(int i = 0; i < commands.size(); i ++){
        for(int j = commands[i][0] - 1; j < commands[i][1]; j++){
            temp.push_back(array[j]);
        }
        sort(temp.begin(), temp.end());
        answer.push_back(temp[commands[i][2] - 1]);
        temp.clear();
    }
    
    return answer;
}
```
#### 피드백
`commands[i][0]`와 같은 구문은 길어지면 알아보기 힘들기 때문에 이전에
```c++
int start_point = commands[i][0];
int end_point = commands[i][1];
int anwser_point = commands[i][2];
```
와 같이 정의해주면 좋다.

## 가장 큰 수
c++
```c++
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(vector<int> numbers) {
    string answer = "";
    
    sort(begin(numbers), end(numbers), [](int a, int b){
        return to_string(a) + to_string(b) > to_string(b) + to_string(a);
    });
    
    for (int i = 0; i < numbers.size();i++){
        string s = to_string(numbers[i]);
        answer += s;
    }
    return to_string(stoi(answer));  // int로 만들고 다시 string ("00" 과 같은 값을 처리하기 위해서)
}
```
python
```python
def solution(numbers):
    return str(int("".join(sorted(map(str,numbers), key = lambda number : number * 3, reverse=True))))
```