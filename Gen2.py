import wx

class windowClass(wx.Frame):
    
    def __init__(self, parent, title):
        super(windowClass, self)._init_(parent, title=title, size =(800,600))

        self.Show()
       
    
app = wx.App()
windowClass(None, title='Genesis')
app.MainLoop()
