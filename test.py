import Student as st

#persona = st.Student("Tom")
#persona.addparent("Bob")
#persona.addparent("Kathy")
#persona.changeaddress("123 disneyland street")
##print("\n")
##print( persona.name )
##print( persona.parents )
##print( persona.address )
#
#info = persona.storeinfo()
#print(info)
#
#personb = st.Student("Tomddd")
#personb.addparent("Bobddd")
#personb.addparent("Kathyddd")
#personb.changeaddress("ddd 123 disneyland street")

theDB = st.StudentDB("./studentdatabase.db")
#theDB.set(persona.storeinfo())
#theDB.set(persona.storeinfo())
#theDB.set(personb.storeinfo())
me = theDB.getstudent("Tom")
print(me.name)
print(me.address)
print(me.parents)

