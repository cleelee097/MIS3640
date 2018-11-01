# Exercise 5 (group work)¶
# Write a definition for a class of anything you want. You have to use the following methods:
# __init__ method that initializes some attributes. One of the attributes has to be an empty list.
# __str__ method that returns a string that reasonably represent the thing.
# A special method that overloads the one type of operators.
# Some other methods that reasonably represent the thing's actions, inclduing one method that takes an object of any type and adds it to the attribute of type list.


# class student:
    
#     def__init__(self, first=christine, last=christine, currentclasses=[]):
#         self.first=first
#         self.last=last
#         self.year=year

#     # def__str__(self):
#     #     return 'I can print myself this way: 


class Person(object):

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return str(self.name)

    def get_details(self):
        "Returns a string containing name of the person"
        return self.name


class Student(Person):

    def __init__(self, name, branch, year):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year

    def get_details(self):
        "Returns a string containing student's details."
        return "%s studies %s and is in %s year." % (self.name, self.branch, self.year)


class Teacher(Person):

    def __init__(self, name, papers):
        Person.__init__(self, name)
        self.papers = papers

    def get_details(self):
        return "%s teaches %s" % (self.name, ','.join(self.papers))


person1 = Person('Christine')
student1 = Student('Abby', 'QTM', 2018)
teacher1 = Teacher('Li', ['C', 'C++'])

print(person1.get_details())
print(student1.get_details())
print(teacher1.get_details())