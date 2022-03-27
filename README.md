# TutoringDatabase
This in an example implementation of a database to keep track of students I tutor using python (3.9.9)

There are two classes defined in Student.py: 
- The Student class defines the datatype for students
- The StudentDB class defines the database (JSON format) to hold Student datatypes

## Student class
Students are initialized with their name and functions exist to
- add parents names (stored as a list of strings)
- change their address (stored as a string)
- add events to their calander (stored as a nested dictionary)
  - events consist of a date (key) and the price of the session, along with whether or not they've paid
- pay for an event
- list all events
- calculate how much they owe

## StudentDB class
The database is initialized with a file location
 - If the database already exists, load it
 - If the database doesn't exist, create it 

Students can be entered into, read from, and modified in the database. 

Examples and demonstrations of the functionality of this setup are given in \
[test1_setupDB.py](./test1_setupDB.py) and \
[test2_editDB.py](./test2_editDB.py)

