#position, name, age, level, salary

se1 = ['Software Engineer', 'Ravan', '22', 'junior', '5000'];
se2 = ['Software Engineer', 'John', '22', 'senior', '15000'];

#class -> class is blueprint you should define something

class SoftEng:

    #class attribute
    alias = "Keyboard Master";
    def __init__(self, name, age, level, salary):
        #instance attributes
        self.name = name;
        self.age = age;
        self.level = level;
        self.salary = salary;

#instance
se1 = SoftEng('Ravan', '22', 'junior', '5000');
print(se1.name, se1.salary,se1.alias);
se2 = SoftEng('John', '22', 'senior', '15000');
print(se2.name, se2.salary, se2.alias);

#create a class (blueprint)
#create a instance (object)
#class vs instance
#instance attributes: defined in __init__(self)
#class attribute