#position, name, age, level, salary

se1 = ['Software Engineer', 'Ravan', '22', 'junior', '5000'];
se2 = ['Software Engineer', 'John', '22', 'senior', '15000'];
d1 = ['Designer', 'Trish'];
#function
# def code(se):
#     print(f"{se[1]} is writing a code...");

# code(se1);
# code(d1);

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

    #instance method
    def code(self):
        print(f"{self.name} is writing a code...");

    def code_lang(self, language):
        print(f"{self.name} is writing a code in {language}...");

    # def info(self):
    #     info = f"name = {self.name}, age = {self.age} level = {self.level}";
    #     return info;

    #special methods
    #dunder method
    def __str__(self): #string method
        info = f"name = {self.name}, age = {self.age} level = {self.level}";
        return info;

    def __eq__(self, other): #this result true or false
        return self.name == other.name and self.age == other.age;

    @staticmethod # -> decorator using this you can use this function inside the instance but you cannot access the sefl attributes
    def entry_salary(age): #you can only use this function only in the class but not in an instance because it did'nt use self parameter
        if age < 25:
            return 5000;
        if age < 30:
            return 7000;
        return 7000;
#instance
se1 = SoftEng('Ravan', '22', 'junior', '5000');
se2 = SoftEng('John', '22', 'senior', '15000');
se3 = SoftEng('John', '23', 'senior', '15000');

se1.code();
se2.code();

se1.code_lang("Python");
se1.code_lang("Java");

print(se1.info());
print(se1);
print(se2 == se3);

print(SoftEng.entry_salary(24))

#recap:
# instance method(self)
# can take arguments and can return values
# special "dunder" method (__str__ adn __eq__)
# @staticmethod