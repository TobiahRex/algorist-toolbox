## Algorist-Toolbox
A collection of **Jupyter Notebooks** focused on providing an intuitive understanding of key ideas & principles.  We use Jupyter Notebooks to enhance the learning experience by separating code from pro's but giving proper attention to the requirement for exploring concepts with enhance descriptions and articulations. Further, we can __pictoraly illustrate__ Time Complexities and Key ideas using libraries like `plotly` or `matplotlib` with enhanced `pandas` features.

<img src="https://imgur.com/NoMkck6.png">

## Setup
1. Run `./setup.sh`
    - Ensure you see the environment activated in your IDE.
    - ****WARNING**** : If you're using _**VSCode**_ You'll have to close and re-open the IDE due to a bug in VSCode regarding Jupyter Notebook Kernel setups before the setup changes will be seen.
    - Re-activate the environment if you had to re-open the IDE. `source env/bin/activate`
2. Open any Jupyter Notebook and select the Kernel **before** running any code.
3. Choose `algorist-toolbox` Kernel from the dropdown menu.
4. Run any code & have fun 😊


### Sorting
##### Theory
- [ ] _Brute Force Algo's_
    *  [ ] Bubble Sort
    *  [ ] Selection Sort
    *  [ ] Insertion Sort
- [ ] _Divide & Conquer_
  - [ ] Quick Sort
        - [ ] Lomuto's Partition
        - [ ] Hoare's Partition
  - [ ] Merge Sort
- [ ] _Transform & Conquer_
  * [ ] Heap Sort
##### Problems | Technique | Tool

1. [Polish/Dutch National Flag](solution) | [LeetCode]((https://leetcode.com/problems/sort-colors/)):
    - **Divide & Conqueor** | Lomuto's Partition
    - [ ] Solved
2. [Merge K Sorted Linked Lists]() | [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists/)
    - **Divide & Conqueor** | MergeSort's `merge` function.
    - [ ] Solved
    - **Transform & Conqueor** | Min Heap + K nodes.
    - [ ] Solved
3. [Median of Two Sorted Arrays]() | [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays)
    - **Transform & Conqueor** | Min & Max Heap
    - [ ] Solved
4. [Top K Frequent Elements]() |[LeetCode](https://leetcode.com/problems/top-k-frequent-elements)
    - **Transform & Conqueor** | Max Heap
    - [ ] Solved
    - **Divide & Conqueor** | _Quick Select_ + Lomuto's Partition
    - [ ] Solved
5. [Kth Largest in Stream]() | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream)
    - **Transform & Conqueor** | Min Heap + K nodes.
    - [ ] Solved
5. [Median in Stream]() | [LeetCode](https://leetcode.com/problems/find-median-from-data-stream/)
    - **Transform & Conqueor** | Max & Min Heap
    - [ ] Solved

### Recursion
##### Theory

- [ ] Head & Tail
- [ ] Nested Recursion | Compositional Recursion
- [ ] Tree | _Exhaustive Search_
    - [ ] Slates
    - [ ] Dynamic Slates
    - [ ] Backtracking
    - [ ] Backtracking + Slates
- [ ] Math
    - [ ] Sum of K nums
    - [ ] Fibonacci
    - [ ] Exponent
    - [ ] Taylor Series
    - [ ] Factorial
    - [ ] nCr

#### Problems | Technique | Tool
1. [Towers of Hanoi]() | [LeetCode]()
    - <**Technique**> | <Tool>
2. [Character Permuations]() | [LeetCode]()
    - <**Technique**> | <Tool>
3. [Well Formed Parens of K length]() | [LeetCode]()
    - <**Technique**> | <Tool>
4. [Binary Strings of Length N]() | [LeetCode]()
    - <**Technique**> | <Tool>
5. [List Permutations]() | [LeetCode]()
    - <**Technique**> | <Tool>
6. [All Subsets of a Set]() | [LeetCode]()
    - <**Technique**> | <Tool>
