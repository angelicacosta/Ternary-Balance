# Project Title

Ternary Balance problem -  source code file "balance.py"

## Getting Started

### Prerequisites

The program is written in Python (version 3.5.2),
downloaded from https://www.python.org/downloads/

### Installing

Follow the instructions at the web site.

## Running the tests

You can test the functions by typing:
```
$ make test
```

### Unit tests

In the file test_balance.py you can see the tests made for the following functions:

- summing: Given an array of integers, returns the sum of its values.
- stringarray: Given an array of integers, returns a string made of those integer with the following format. eg: 
    ```
    stringarray([1,2,3])
    1, 2, 3
    ```
- need: Given a positive integer value, returns the maximum power of 3 to represent such value and the result of the corresponding power.
- weighting: Given a positive integer value, returns two arrays with integers that represent the weights needed to weight such value in a ternary balance. The first array represents the weights in the left side of the balance (where the initial weight is) and the second array represents the weight in the right side.

### Validation tests

When you execute the program you can check that the answer is correct by checking the output on the screen, eg:


```
$ make 
Please write how much you want to weight: 100
right: 81 27 1 
left: 100 9 

```

## Built With

```
python  --version
Python 3.5.2

```

## Versioning

You can find the program in the following GitHub repository
https://github.com/angelicacosta/Ternary-Balance

Version 1 - balance.py - does not handle invalid inputs
Version 2 - balance.py - restructuring of version 1 and invalid inputs handling

## Authors

### Primary Author

Angelica Acosta Arteta

### Additional Contributions

J Paul Gibson

## License

This project is licensed under the MIT License - see the license.txt file for details
