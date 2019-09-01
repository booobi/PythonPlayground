# import wx

# app = wx.App()

# frame = wx.Frame(None,-1, 'inclass.py')
# frame.Show()

# app.MainLoop()
class Dog(object):
    def __init__(self):
        self.name = "initDog"
        self.age = 13

myDog = Dog()
print myDog.name