# CollatzProblem
A brute force script to find a solution to the Collatz Problem

## Wikipedia
The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1. 

## Info
Currently, this script uses brute force to find a number that does not lead to 1, by testing every positive full number. If the number being tested reaches 1, it prints out the number and how many steps it took to reach 1. Theoretically if the the number wont reach number, the script will freeze as it tries to break out of the loop, and thus a solution is found
