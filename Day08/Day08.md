###  What I Learned
```
How to generate a random float using random.random()
How to generate numbers in a range using random.randrange()
How to pick multiple unique items using random.sample()
What a random seed is and how it affects randomness
```

###  What I Built
```
A small Python script that:
Generates a random float
Generates a random number from a range
Selects multiple random items from a list
Demonstrates repeatable output using a seed
```

###  What Failed
```
Got the same random output repeatedly when using a fixed seed
Confusion about why random.sample() does not repeat items
```

###  How I Fixed It
```
Removed or changed the seed to get different results
Understood that random.sample() always returns unique values
```
###  Security Insight
```
Predictable randomness can be exploited
Using fixed seeds makes values guessable
The random module should not be used for passwords or tokens
```
