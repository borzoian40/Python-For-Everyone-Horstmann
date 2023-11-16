"""
••• P6.20 In this assignment, you will model the game of Bulgarian Solitaire. The game starts 
with 45 cards. (They need not be playing cards. Unmarked index cards work just as 
well.) Randomly divide them into some number of piles of random size. For example, you might start with piles ofsize 20, 5, 1, 9, and 10. In each round, you take one 
card from each pile, forming a new pile with these cards. For example, the sample 
starting configuration would be transformed into piles ofsize 19, 4, 8, 9, and 5. The
solitaire is over when the piles have size 1, 2, 3, 4, 5, 6, 7, 8, and 9, in some order. (It 
can be shown that you always end up with such a configuration.)
In your program, produce a random starting configuration and print it. Then keep 
applying the solitaire step and print the result. Stop when the solitaire final configuration is reached.

"""
