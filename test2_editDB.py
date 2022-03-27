import Student as st

# Read database from file
db_location="./mystudents.db"
theDB = st.StudentDB(db_location)

# list all students
theDB.liststudents()
# >> List of all students:
# >>   Alice
# >>   Bob


# Some examples of things we can do with students
# First we need to get the student from the DB
alice = theDB.getstudent("Alice")

# Add some events to their schedule
alice.addevent(date="21 March 2022", price=170, paid=False)
alice.addevent(date="22 March 2022", price=100, paid=True)
alice.addevent(date="23 March 2022", price=200, paid=False)

# Print out their current schedule
alice.listallevents()
# >> List of Tutoring Events for Alice:
# >> 
# >> Date:     21 March 2022
# >>   Price:  170
# >>   Paid:   False
# >> 
# >> Date:     22 March 2022
# >>   Price:  100
# >>   Paid:   True
# >> 
# >> Date:     23 March 2022
# >>   Price:  200
# >>   Paid:   False

# Calculate how much she owes me
alice.oweshowmuch()
# >> Alice owes:  370

# Update after she pays for one of the sessions
alice.paidevent("23 March 2022")
alice.oweshowmuch()
# >> Alice owes:  170

# Don't forget to update the database with the new info
theDB.set(alice.storeinfo())

