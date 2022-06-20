#Q1: Follow the steps:

class triangle:
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
    number_sides=3
    def check_angle(self):
        sum=self.angle1+self.angle2+self.angle3
        if sum<=180:
            return True
        else:
            return False
a=int(input("enter angle1:"))
b=int(input("enter angle2:"))
c=int(input("enter angle3:"))
my_triangles=triangle(a,b,c)
p=my_triangles.check_angle()
print("check angles:",p)
print("triangle sides=",my_triangles.number_sides)
#Q2: Define a class called Songs,
class song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
happy_bday=song(["May god bless you;","Have a sunshine on you;","Happy Birthday to you !"])
happy_bday.sing_me_a_song()

#Q 3: Define a class called Lunch.Its __init__() method should have two arguments:selfanf menu.Where
class lunch:
    
    def __init__(self,menu):
        self.menu=menu
        
    def menu_price(self):
        if self.menu=="menu1":
            print("your choice")
            print("menu price 12.00")
        elif self.menu=="menu2":
            print("your choice")
            print("menu price 13.00")
        else:
            print("error in menu")
a=input("enter input (menu1/menu2):")
b=str(a)
paul=lunch(b)
paul.menu_price()


#Q4: Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case.
class word:
    def get_string(self,str1):
        self.str1=str1
        self.str2=self.str1.upper()
    def print_string(self):
        print(self.str2)
s1=word()
a=input("enter your string(lowercase):")
s1.get_string(a)
s1.print_string()
#Q5: Write a program to find the area and perimeter of a rectangle using classes and objects.
Program output should be like this:
class sum:
    def area(self,length,width):
        print("area:",length*width)
    def peri(self,length,width):
        print("perimeter:",2*(length+width))

b=int(input("enter length of rectangle:"))
c=int(input("enter width of rectangle:"))
print("""1.area
2.perimeter
3.exit""")
s1=sum()
while True:
    print("enter your choice")
    a=int(input())
    if a==1:
        s1.area(b,c)
    if a==2:
        s1.peri(b,c)
    if a==3:
        break 
    
    


        
                  
                  
        
        
