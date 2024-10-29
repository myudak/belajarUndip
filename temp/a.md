Sure! Let's tackle this problem step by step, ensuring that each part of the solution is thoroughly explained. We'll break down the problem, understand the rules, and then design an algorithm to determine the winner for each test case.

**Problem Recap:**

- **Players:** Anda and Kamu, taking turns to play, with Anda going first.
- **Initial Setup:** A number `N` containing only non-zero digits.
- **Move Rules:**
  1. Choose three consecutive digits in `N` that form a three-digit number divisible by 3.
  2. Remove the middle digit of these three digits.
  3. Concatenate the remaining digits to form the new `N` with one fewer digit.
- **Winning Condition:** If a player cannot make a valid move on their turn, they lose.

**Objective:** For each test case, determine whether Anda (the first player) or Kamu (the second player) will win, assuming both play optimally.

**Understanding the Problem:**

To solve this, we need to model the game and determine the winner based on the initial number `N`. The key observations are:

1. **Valid Moves:** A move is only possible if there are three consecutive digits that form a number divisible by 3.
2. **Optimal Play:** Both players will make the best possible moves to maximize their chances of winning.

Given these observations, we'll use concepts from **game theory**, specifically the **Sprague-Grundy theorem**, to model the game and determine the winner.

**Sprague-Grundy Theorem Overview:**

The Sprague-Grundy theorem is a fundamental result in combinatorial game theory. It states that every impartial game (where both players have the same moves available) under the normal play convention (the player who makes the last move wins) is equivalent to a Nimber (a heap in the game of Nim). The Grundy number (or Nimber) of a position in the game helps determine the winning strategy.

**Applying Sprague-Grundy to This Problem:**

- **Game State:** The current number `N`.
- **Moves:** Removing the middle digit of a valid triplet.
- **Subgames:** After a move, the number splits into two parts, which can be considered independent subgames.
- **Grundy Number:** The Grundy number for a game state helps determine if the current player can force a win.

Our task is to:

1. **Identify all valid moves** by finding triplets divisible by 3.
2. **Model the game** by determining how these moves affect the remaining number.
3. **Calculate the Grundy number** for each connected component of moves.
4. **Determine the winner** based on the total Grundy number.

**Step-by-Step Solution:**

Let's break down the solution into manageable steps.

### 1. Reading Input:

We have multiple test cases. For each test case, we read the number `N`.

```cpp
#include <bits/stdc++.h>
using namespace std;
```

### 2. Identifying Valid Triplet Centers:

We need to find all triplet centers where the three-digit number formed is divisible by 3.

- A triplet is formed by three consecutive digits.
- The center of the triplet is the second digit.
- A triplet is valid if the sum of its digits is divisible by 3.

### 3. Grouping Overlapping Triplets:

After identifying all valid triplet centers, we group overlapping triplets into connected components. Two triplets overlap if their centers are at most 2 positions apart.

### 4. Calculating Grundy Numbers:

For each connected component:

- If the number of triplet centers in the component is odd, it contributes a Grundy number of 1.
- If even, it contributes 0.
- The total Grundy number is the XOR of all Grundy numbers from connected components.

### 5. Determining the Winner:

- If the total Grundy number is non-zero, the first player (Anda) can force a win.
- Otherwise, the second player (Kamu) will win.

### 6. Implementing the Algorithm:

Now, let's implement the above steps in C++.

```cpp
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    int T;
    cin >> T;
    while(T--){
        string N;
        cin >> N;
        int n = N.size();
        vector<int> centers;
        // Identify all valid triplet centers
        for(int i=0; i <= n-3; ++i){
            int sum = (N[i]-'0') + (N[i+1]-'0') + (N[i+2]-'0');
            if(sum % 3 == 0){
                centers.push_back(i+1); // Center index (0-based)
            }
        }
        // Now, group centers into connected components
        int total_xor = 0;
        if(!centers.empty()){
            // Initialize the first connected component
            int current_k = 1;
            int prev_center = centers[0];
            for(int i=1; i < centers.size(); ++i){
                if(centers[i] - prev_center <= 2){
                    current_k++;
                }
                else{
                    // Assign Grundy number for the current connected component
                    if(current_k % 2 == 1){
                        total_xor ^= 1;
                    }
                    // Start a new connected component
                    current_k = 1;
                }
                prev_center = centers[i];
            }
            // After loop, assign Grundy number for the last connected component
            if(current_k % 2 == 1){
                total_xor ^= 1;
            }
        }
        // Determine the winner based on total_xor
        if(total_xor == 1){
            cout << "Anda\n";
        }
        else{
            cout << "Kamu\n";
        }
    }
}
```

### 7. Explanation of the Code:

Let's go through the code line by line.

```cpp
#include <bits/stdc++.h>
using namespace std;
```
We include all standard libraries using the `bits/stdc++.h` header for convenience and use the `std` namespace to avoid prefixing standard library names with `std::`.

```cpp
int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
```
We define the `main` function and optimize input/output by untieing `cin` from `cout` and turning off synchronization with C-style I/O for faster execution.

```cpp
    int T;
    cin >> T;
```
We read the number of test cases `T`.

```cpp
    while(T--){
        string N;
        cin >> N;
        int n = N.size();
        vector<int> centers;
```
We start processing each test case. We read the number `N` as a string and determine its length `n`. We also initialize a vector `centers` to store the indices of valid triplet centers.

```cpp
        // Identify all valid triplet centers
        for(int i=0; i <= n-3; ++i){
            int sum = (N[i]-'0') + (N[i+1]-'0') + (N[i+2]-'0');
            if(sum % 3 == 0){
                centers.push_back(i+1); // Center index (0-based)
            }
        }
```
We iterate through the string `N` to find all valid triplet centers:

- We loop from `i = 0` to `i = n-3` to cover all possible triplets.
- For each triplet starting at index `i`, we calculate the sum of its digits.
- If the sum is divisible by 3 (`sum % 3 == 0`), we add the center index (`i+1`) to the `centers` vector.

```cpp
        // Now, group centers into connected components
        int total_xor = 0;
        if(!centers.empty()){
            // Initialize the first connected component
            int current_k = 1;
            int prev_center = centers[0];
            for(int i=1; i < centers.size(); ++i){
                if(centers[i] - prev_center <= 2){
                    current_k++;
                }
                else{
                    // Assign Grundy number for the current connected component
                    if(current_k % 2 == 1){
                        total_xor ^= 1;
                    }
                    // Start a new connected component
                    current_k = 1;
                }
                prev_center = centers[i];
            }
            // After loop, assign Grundy number for the last connected component
            if(current_k % 2 == 1){
                total_xor ^= 1;
            }
        }
```
Here’s how we group the triplet centers into connected components:

- We initialize `total_xor` to 0, which will hold the cumulative XOR of Grundy numbers.
- If there are any centers:
  - We start with the first center, setting `current_k` to 1 and `prev_center` to its index.
  - We iterate through the remaining centers:
    - If the current center is within 2 positions of the previous center (`centers[i] - prev_center <= 2`), it belongs to the same connected component, so we increment `current_k`.
    - Otherwise, it starts a new connected component:
      - If the previous connected component had an odd `k` (number of triplet centers), we XOR `total_xor` with 1.
      - We reset `current_k` to 1 for the new component.
    - We update `prev_center` to the current center.
  - After the loop, we handle the last connected component:
    - If `current_k` is odd, we XOR `total_xor` with 1.

**Why XOR?**

In the Sprague-Grundy theorem, the XOR of Grundy numbers determines the outcome:

- If the XOR (or Nim-sum) is non-zero, the first player can force a win.
- If the XOR is zero, the second player can force a win.

In our problem, connected components with an odd number of triplet centers contribute a Grundy number of 1, and those with even contribute 0. XORing these values gives us the total Grundy number.

```cpp
        // Determine the winner based on total_xor
        if(total_xor == 1){
            cout << "Anda\n";
        }
        else{
            cout << "Kamu\n";
        }
    }
}
```
Finally, based on the cumulative XOR:

- If `total_xor == 1`, Anda can force a win, so we print "Anda".
- Otherwise, Kamu will win, so we print "Kamu".

**Sample Walkthrough:**

Let's verify the solution with one of the sample inputs.

**Sample Input:**
```
5
19823
2651265
9
73
123
```

**Sample Output:**
```
Anda
Kamu
Kamu
Kamu
Anda
```

- **Test Case 1: "19823"**
  - Valid triplet centers: position 1 (`'198'` → sum=18, divisible by 3).
  - Only one connected component with `k=1` (odd).
  - `total_xor = 1`, so **Anda** wins.

- **Test Case 2: "2651265"**
  - Valid triplet centers: positions 2 (`'651'` → sum=12) and 4 (`'126'` → sum=9).
  - These centers are within 2 positions of each other (overlapping).
  - One connected component with `k=2` (even).
  - `total_xor = 0`, so **Kamu** wins.

- **Test Case 3: "9"**
  - No triplet possible.
  - `total_xor = 0`, so **Kamu** wins.

- **Test Case 4: "73"**
  - No triplet possible.
  - `total_xor = 0`, so **Kamu** wins.

- **Test Case 5: "123"**
  - Valid triplet centers: position 1 (`'123'` → sum=6).
  - Only one connected component with `k=1` (odd).
  - `total_xor = 1`, so **Anda** wins.

**Conclusion:**

This solution effectively models the game using combinatorial game theory principles, specifically the Sprague-Grundy theorem. By identifying valid triplet centers and grouping overlapping triplets into connected components, we can determine the winner based on the XOR of their Grundy numbers. This approach ensures optimal play by both players and efficiently determines the outcome for each test case.