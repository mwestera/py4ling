### Python for Linguists ###
# Class 3 # 

1. Time spent on self-study this week? ~5 hours
2. Mini-exam 2
3. Discuss exercises 4.28, 4.29, 4.30 and 5.22
4. Short lecture on programs + demo
5. Work on exercises: remainder of 5, start section 6 (functions)
6. Homework for next time: Exercises section 6, and 7 until 7.10 (<- easier).
   - Exercises 6.25, 6.32, 6.34 will be discussed in class.
   - For all other questions, see office hours/forum.


### TODOs
- share the twitter csv 

### Some code snippets from class

```python
# 4.28.
time = int(input('What is the current time in hours?'))

hours_until_alarm = int(input('How long shall we wait until the alarm sounds?'))

print('alarm will go off at:', (time + hours_until_alarm) % 24)
```


```python
# 5.22
n = 123

if n % 2 == 1 and n > 10:
    print('ALARM!!!')
    quit()  # inside a function, you'd typically use 'return' instead; inside a loop (later section), `continue` or `break`

if n % 2 == 1:
    print('Odd', end='')
else:
    print('Even', end='')

if n > 10:
    print(', and greater than 10!')
elif n == 10:
    print(', and equal to 10!')
else:
    print(', and smaller than 10!')
```