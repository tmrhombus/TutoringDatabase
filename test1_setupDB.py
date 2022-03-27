import Student as st


# Define two students
alice = st.Student("Alice")
bob   = st.Student("Bob")

# Add parent names to students
alice.addparent("Gigi")
alice.addparent("Mike")

bob.addparent("Alex")
bob.addparent("Wendy")

# Add addresses to students
alice.changeaddress("123 Disneyland Drive")
bob.changeaddress("456 Christmas Tree Lane")


# Enter students into database
# Since database doesn't yet exist, create it first

db_location="./mystudents.db"

theDB = st.StudentDB(db_location)

# Add students to database
theDB.set( alice.storeinfo() )
theDB.set( bob.storeinfo()   )

