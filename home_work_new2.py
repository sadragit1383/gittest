class Address:
    def __init__(self,name_city,name_street,code_post):
        self.name_city=name_city
        self.name_street=name_street
        self.code_post=code_post
        self.addrees={'city':name_city,'street':name_street,'code post':code_post}
    
    def show(self):
        print(f'Name:{self.name_city}\tName_street:{self.name_street}\tcode post:{self.code_post}')

    def show_dict(self):
        for item in self.addrees.items():
            print(item)
#=======================================================================================

class Person:
    def __init__(self,name,family,code_custmer,phone_number,Email):
        self.name=name
        self.family=family
        self.code_custmer=code_custmer
        self.phone_number=phone_number
        self.Email=Email
        self.person={'name':name,'family':family,'code custmer':code_custmer,'phone_number':phone_number,'Email':Email}
    def show(self):
        print(f'Name:{self.name}\tfamily:{self.family}\tcode custmer:{self.code_custmer}\tphone number:{self.phone_number}\tEmail:{self.Email}')

    def show_dict(self):
        for item in self.person.items():
            print(item)
#===========================================the contact class has show func and member that merge with dict============================================

class Contact(Address,Person):
    def __init__(self, name_city, name_street, code_post,name,family,code_custmer,phone_number,Email):
       Address.__init__(self,name_city, name_street, code_post)
       Person.__init__(self,name,family,code_custmer,phone_number,Email)
       self.contact={'city':name_city,'street':name_street,'code post':code_post,'name':name,'family':family,'code custmer':code_custmer,'phone_number':phone_number,'Email':Email}
       return Person.show(self)
            
    def show(self):
        print(f'Name:{self.name_city}\tName_street:{self.name_street}\tcode post:{self.code_post}\tName:{self.name}\tfamily:{self.family}\tcode custmer:{self.code_custmer}\tphone number:{self.phone_number}\tEmail:{self.Email}')

    def __str__(self):
        return f'Name:{self.name_city}\tName_street:{self.name_street}\tcode post:{self.code_post}\tName:{self.name}\tfamily:{self.family}\tcode custmer:{self.code_custmer}\tphone number:{self.phone_number}\tEmail:{self.Email}'

    def show_dict(self):
        for item in self.contact.items():
            print(item)

#=======================================================================================

class Phone_book():
    def __init__(self,name_phoneBook):
        self.name_phone_book=name_phoneBook
        self.list_contact=[]
        
    
    def add_contact(self,Contact_new):
       if Contact_new in [person for person in self.list_contact]:
            print('This contact is already has in system....')

       else:
           self.list_contact.append(Contact_new)
           print('Succefuly added....')
# this func for chacking las name for show information.....
    def search_contact(self,last_family):
        found=False
        
        for person in self.list_contact:
            if person.family==last_family:
                found=True
                print('Your information is...')
                print(f'Name:{person.name}')
                print(f'Family:{person.family}')
                print(f'code custmer:{person.code_custmer}')
                print(f'phone number:{person.phone_number}')
                print(f'Email"{person.Email}')
                print(f'your address:  name city{person.name_city}\tname street:{person.name_street}\tcode custmer:{person.code_post}')
            else:
                print(f'cant found this family:{last_family}')
# for show all info usr args ruls
    def show_ALL_contanc(self,*contacts):
        for contact in contacts:
            print(contact)
            print(100*'-')
    
#=======================================================================================

Phone_book1=Phone_book('My phonr book')       

Contact1=Contact('losangles','azadi','33','sadra','rostami','444','09339087909','sadraabadkar1383@gmail.com')
Contact2=Contact('seyatel','azadi','33','sadra','rohi','444','09339087909','sadraabadkar1383@gmail.com')
Contact3=Contact('losangles','azadi','33','sadra','mamadof','444','09339087909','sadraabadkar1383@gmail.com')
# super(Contact,Contact1).show()
Phone_book1.add_contact(Contact1)
Phone_book1.add_contact(Contact2)
Phone_book1.add_contact(Contact3)
Phone_book1.show_ALL_contanc(Contact1,Contact2,Contact3)
Phone_book1.search_contact('mamadof')
# Contact1.show_dict()

#     .........................برای اثبات انجام تکالیف توسظ خودم...............
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt

# ایجاد تصویر با اندازه و رنگ پس زمینه و رنگ متن دلخواه
image = Image.new('RGB', (500, 300), color = 'black')

# اضافه کردن متن "write by abadkar" به تصویر
draw = ImageDraw.Draw(image)
text = 'write by abadkar'
font = ImageFont.truetype('arial.ttf', 60)
textwidth, textheight = draw.textsize(text, font)
x = (image.width - textwidth) / 2
y = (image.height- textheight) / 2
draw.text((x, y), text, font=font, fill=(255, 20, 147))

# ذخیره تصویر
image.save('write_by_abadkar.png')

# نمایش تصویر با استفاده از کتابخانه matplotlib
img = plt.imread('write_by_abadkar.png')
plt.imshow(img)
plt.axis('off')
plt.show()