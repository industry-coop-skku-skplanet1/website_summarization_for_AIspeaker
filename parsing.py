#-*- coding:utf-8 -*-

from bs4 import BeautifulSoup



def recursiveChildren(x):
    if "childGenerator" in dir(x):
      for child in x.childGenerator():
          name = getattr(child, "name", None)
          if name is not None:
             print ("[Container Node]",child.name)
          recursiveChildren(child)
    else:
       if not x.isspace(): #Just to avoid printing "\n" parsed from document.
          print ("[Terminal Node]",str(x))

your_data ='''<div class="btn_area">
                <a href="#" class="btn_type1" onclick="addReservationGameCafe(); return false;"><strong>하이하</strong></a>
            </div>'''
soup = BeautifulSoup(your_data,'html.parser')
for child in soup.childGenerator():
    recursiveChildren(child)