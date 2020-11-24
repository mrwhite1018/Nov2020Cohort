class Person:
    def __init__(self, name, email, phone): 
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))

Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
Jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

Sonny.greet(Jordan)
Jordan.greet(Sonny)

print(f"Sonny's email: {Sonny.email} and phone: {Sonny.phone}")
print(f"Jordan's email: {Jordan.email} and phone: {Jordan.phone}")
