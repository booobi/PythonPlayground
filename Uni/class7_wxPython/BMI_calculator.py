import wx

class BMICalculator(wx.Frame):
    def __init__(self, *args, **kw):
        super(BMICalculator, self).__init__(*args, **kw)
        self.initUI()
# CHECK NAME OF FILE
# CHECK NAME OF FILE
# CHECK NAME OF FILE
# CHECK NAME OF FILE

    def initUI(self):
        self.mainPanel = wx.Panel(self)
        self.SetTitle("BMI Calculator")
        self.Show(True)
        
        self.bmiCalcMainLabel = wx.StaticText(self.mainPanel, label = "Body Mass Index Calculator", pos = (80,10))
        self.bmiResultText = wx.StaticText(self.mainPanel, pos = (200,75))
        self.bmiResultText.Hide()

        self.weightLbl = wx.StaticText(self.mainPanel, label = "weight(kg):", pos = (20,50))
        self.weightCtrl = wx.SpinCtrl(self.mainPanel, size = (60,20), pos = (120,50), min = 1, max = 999)
        
        self.hightLbl = wx.StaticText(self.mainPanel, label = "hight(cm):", pos = (20,100))
        self.hightCtrl = wx.SpinCtrl(self.mainPanel, size = (60,20), pos = (120,100), min = 1, max = 999)

        self.computeButton = wx.Button(self.mainPanel, pos = (60, 150), label = "Compute")
        self.computeButton.Bind(wx.EVT_BUTTON, self.OnCompute)


        self.closeButton = wx.Button(self.mainPanel, pos = (170, 150), label = "Close")
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
    

    def OnCompute(self, e):

        self.bmiResultText.Show()
        
        inputWeight = self.weightCtrl.GetValue()
        inputhight = self.hightCtrl.GetValue()
        result = self.calculateBMI(inputWeight, inputhight)

        self.bmiResultText.SetLabel("Your Body Mass Index is %.2f" % result)
    
    def calculateBMI(self, weight, hight):
        hight = hight/100.0
        return weight / (hight * hight)

    def OnClose(self, e):
        self.Close()
        
app = wx.App()

BMICalculator(None)
app.MainLoop()