# ADealerForThePeople
***Author: Kevin Castell***

This project scrapes reviews on DealerRater.com for McKaig Chevrolet Buick to uncover the most overly positive comments.

## Positivity Criteria
In order to determine the most overly positive comments the first five pages of reviews is gathered.
Once gathered, the reviews are sorted based on the number of '!' in the review.
The top 3 reviews based on the number of '!' are returned to the console in ranked order.

This metric was determined based on a visual inspection of a subset of the reviews. It appeared that the reviews with more '!' stood out
at first glance. These reviews would likely draw unwanted attention to the dealership.

## Running the Project
This project is developed using python3 with dependencies installed using pip.

In order to run the project the necessary dependencies must be installed. 
This can be done by executing the following command at from the root directory:
```pip install -r requirements.txt```

To run the project use the following command in the root directory based on your operating system. 
A python IDE may also be used.

Windows:
```py src/a_dealer_for_the_people.py```

MacOs/Linux:
```python3 src/a_dealer_for_the_people.py```


**NOTE**: This project was developed and tested on a Windows machine.

## Running the Test Suite
Unit tests for this project were developed using the python3 unittest module.

Further documentation on the unittesting module can be found [here](https://docs.python.org/3/library/unittest.html).

Unit tests can be run using the following command in the root directory. Use ```-v``` for verbose test output.

Windows:
```py -m unittest```

MacOS/Linux:
```python3 -m unittest```
