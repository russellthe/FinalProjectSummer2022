class Moves:
    def __init__(self, name, type, category, moveType, PP, power, accuracy, effect, secondary_effect=None, secondary_power=None):
        self.name = name
        self.type = type
        self.category = category
        self.moveType = moveType
        self.PP = PP
        self.power = power
        self.accuracy = accuracy
        self.effect = effect
        self.secondary_effect = secondary_effect
        self.secondary_power = secondary_power

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getCategory(self):
        return self.category

    def getMoveType(self):
        return self.moveType

    def getPP(self):
        return self.PP

    def getPower(self):
        return self.power

    def getAccuracy(self):
        return self.accuracy

    def getEffect(self):
        return self.effect

    def getSecondary_effect(self):
        return self.secondary_effect

    def getSecondary_power(self):
        return self.secondary_power

    def changePP(self, change):
        self.PP = self.PP + change
