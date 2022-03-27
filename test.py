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


#
#
#
#persona = st.Student("Tom")
#persona.addparent("Bob")
#persona.addparent("Kathy")
#persona.changeaddress("123 disneyland street")
###print("\n")
###print( persona.name )
###print( persona.parents )
###print( persona.address )
##
##info = persona.storeinfo()
##print(info)
##
##personb = st.Student("Tomddd")
##personb.addparent("Bobddd")
##personb.addparent("Kathyddd")
##personb.changeaddress("ddd 123 disneyland street")
#
#theDB = st.StudentDB("./studentdatabase.db")
##theDB.set(persona.storeinfo())
#
#
##theDB.set(persona.storeinfo())
##theDB.set(personb.storeinfo())
#me = theDB.getstudent("Tom")
#print(me.name)
#print(me.address)
#print(me.parents)
#me.listallevents()
#me.oweshowmuch()
#
##me.addevent(date="21 March 2022", price=170, paid=False)
##me.addevent(date="22 March 2022", price=170, paid=False)
##me.addevent(date="23 March 2022", price=170, paid=False)
##
##me.paidevent(date="21 March 2022")
##theDB.set(me.storeinfo())
#
#
#
