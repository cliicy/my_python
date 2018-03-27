import wx
import fileinput


class A:

    def add(self,a,b):
        'Try to caculate numbers'
        return a+b

    def init(self,data):
        'Initialize the account information'
        data['first']={}
        data['middle']={}
        data['last']={}

    def lookup(self, data,label, name):
        'look for account information'
        return data[label].get(name)

    def store(self, data, *full_names):
        'Save account information to store'
        for full_name in full_names:
            names=full_name.split()
            if len(names) == 2:
                names.insert(1, '')
            labels='first', 'middle', 'last'
            for label, name in zip(labels, names):
                people = self.lookup(data, label, name)
                if people:
                    people.append(full_name)
                else:
                    data[label][name]=[full_name]

"""

def load(event):
    print("Button will do something")
    file=open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file=open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()

"""

if __name__== '__main__':
    print('aaa')


"""
for line in fileinput.input(inplace=True):
        line=line.rstrip()
        num=fileinput.lineno()
        print('%-40s # %2i' %(line, num))
    

    app = wx.App()
    win = wx.Frame(None,title="Simple Editor",size=(410,335))
#    loadButton=wx.Button(win,label='open',pos=(225,1),size=(80,25))
#    saveButton=wx.Button(win,label='Save',pos=(315,5),size=(80,25))

#    filename=wx.TextCtrl(win,pos=(5,5),size=(210,25))
#    contents=wx.TextCtrl(win,pos=(5,35),size=(390,260),style=wx.TE_MULTILINE|wx.HSCROLL)
#    btn=wx.Button(win)

    bkg=wx.Panel(win)
    loadButton=wx.Button(bkg,label='Open')
    saveButton=wx.Button(bkg,label='Save')
    filename=wx.TextCtrl(bkg)
    contents=wx.TextCtrl(bkg,style=wx.TE_MULTILINE|wx.HSCROLL)

    hbox=wx.BoxSizer()
    hbox.Add(filename,proportion=1,flag=wx.EXPAND)
    hbox.Add(loadButton,proportion=0,flag=wx.LEFT,border=5)
    hbox.Add(saveButton,proportion=0,flag=wx.LEFT,border=5)

    vbox = wx.BoxSizer(wx.VERTICAL)
    vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.ALL,border=5)
    vbox.Add(contents, proportion=1, flag=wx.LEFT, border=5)
    vbox.Add(saveButton, proportion=0, flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT, border=5)

    bkg.SetSizer(vbox)

    loadButton.Bind(wx.EVT_BUTTON,load)

    win.Show()
    app.MainLoop()
"""