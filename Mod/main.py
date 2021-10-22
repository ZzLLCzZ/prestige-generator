import BigNumber
import SeededRand
import GameController

class Data:
    def __init__(self, id):
        self.id = id
        self.level = 0
        self.current = BigNumber(0)
        self.goal = 1000.0
        self.progress = BigNumber(0)
        self.p_currency = 0
        self.upgrade_points = 0

    def updateProgress(self):
        self.progress = self.current / BigNumber(self.goal)
        if self.level >= 15.0:
            self.progress = BigNumber(1)
        self.prestige_currency = str(BigNumber(self.p_currency))
        self.up_points = "UP:" + str(BigNumber(self.upgrade_points))


def onLoad():
    return  "Success Loading"

def onUnload():
    return "Success Unloading"

def createModule(id):
    data = Data(id)
    data.result = "Created Template"

    return data

def tick(data):
    data.current += BigNumber(1)
    data.updateProgress()

    return data

def bulkTick(data, amount):
    data.current += amount
    while data.current > BigNumber(data.goal):
        data.p_currency += data.level
        data.current -= BigNumber(data.goal)
    data.updateProgress()

    return data

def destroyModule(data):
    return data

def onPrestige(data):
    data.upgrade_points += 1

    return data

def loadSave(save, id):
    data = createModule(id)
    data.level = int(save.split(",")[0])
    data.goal = float(save.split(",")[1])
    data.p_currency = int(save.split(",")[2])

    return data

def saveData(data):
    result = ""
    result += str(data.level) + ","
    result += str(data.goal) + ","
    result += str(data.p_currency)

    return result

"""
END special functions
"""

def upgradeClick(data):
    data.goal /= 1.024
    if data.goal <= 1:
        data.goal = 1
    data.level += 1

    return data

def upgradeAvail(data):
    return data.upgrade_points >= 1
