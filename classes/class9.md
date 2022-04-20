# Python for Linguists

## Class 9
1. Mini-exam 8 + discussion
2. Admin: homework time?  7 hours
3. Homework discussion (13.9-13.35 and section 14)
--- break
4. Adventure continued: Similarity
5. Homework for next time (in *two* weeks time again): sections 15, 16, 17.

------

## Homework discussion

return:  escapes from a function (hence from a containing loop, but that's essentially a side effect)

break: escapes from a loop
continue: skips the remainder of the loop body for the current element, moving to the next element.


for i in range(8):
    print(i)
    if i > 4:
        # break   # will print:  0 0 1 1 2 2 3 3 4 4 5
        continue    # will print: 0 0 1 1 2 2 3 3 4 4 5 6 7
    print(i)


quit()


another thing that came up:
    looping with recursion (instead of for, while)
        i.e., a function calling itself

