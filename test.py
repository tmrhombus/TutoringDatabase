import Student as st

persona = st.Student("Tom")

print( persona.name )
print( persona.parents )
print( persona.address )

persona.addparent("Bob")
persona.changeaddress("123 disneyland street")

print("\n")
print( persona.name )
print( persona.parents )
print( persona.address )
