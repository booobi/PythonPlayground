import wx


class HangmanGame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(HangmanGame, self).__init__(*args, **kwargs)
        self.initUI()

    def initUI(self):
        self.mainPanel = wx.Panel(self)
        self.SetSize(wx.Size(400, 500))
        self.Show(True)
        self.initializeInput('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.guessButton = wx.Button(self.mainPanel, label="Guess", pos=(450, 400))

    def initializeInput(self, inputLetters):

        self.letterInputList = []

        startX = 90
        startY = 150
        offsetX = 0
        offsetY = 0

        for letter in inputLetters:
            self.letterInputList.append(
                wx.ToggleButton(self.mainPanel, label=letter, pos=(startX + offsetX, startY + offsetY), size=(20, 20)))
            offsetX += 20
            if offsetX >= 220:
                offsetY += 20
                offsetX = 0


app = wx.App()

HangmanGame(None)

app.MainLoop()
