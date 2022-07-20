class CreatePokemon:
    party = {}

    def __init__(self, name, hp, atk, defense, sp_atk, sp_def, speed, moveSet, type1, type2):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.defense = defense
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.moveSet = moveSet
        self.type1 = type1
        self.type2 = type2
        self.atkStage = 0
        self.defenseStage = 0
        self.sp_atkStage = 0
        self.sp_defStage = 0
        self.speedStage = 0
        self.accuracyStage = 0
        self.evasionStage = 0
        self.status = "" # "" or "(Fainted)"

    def getName(self):
        return self.name

    def getHP(self):
        return self.hp

    def getAtk(self):
        return self.atk

    def getDefense(self):
        return self.defense

    def getSp_atk(self):
        return self.sp_atk

    def getSp_def(self):
        return self.sp_def

    def getSpeed(self):
        return self.speed

    def getMoveSet(self):
        return self.moveSet

    def getType1(self):
        return self.type1

    def getType2(self):
        return self.type2

    def getAtkStage(self):
        return self.atkStage

    def getDefenseStage(self):
        return self.defenseStage

    def getSp_atkStage(self):
        return self.sp_atkStage

    def getSp_defStage(self):
        return self.sp_defStage

    def getSpeedStage(self):
        return self.speedStage

    def getAccuracyStage(self):
        return self.accuracyStage

    def getEvasionStage(self):
        return self.evasionStage

    def getStatus(self):
        return self.status

    def getMax_HP(self):
        return self.max_hp

    def getHP_percentage(self):
        return int(self.hp/self.max_hp * 100)

    def setHP(self, change):
        self.hp = change

    def setMoveSet(self, moveSet):
        self.moveSet = moveSet

    def changeHP(self, change):
        self.hp += change

    def changeAtkStage(self, change):
        self.atkStage += change

    def changeDefenseStage(self, change):
        self.defenseStage += change

    def changeSp_atkStage(self, change):
        self.sp_atkStage += change

    def changeSp_defStage(self, change):
        self.sp_defStage += change

    def changeSpeedStage(self, change):
        self.speedStage += change

    def changeAccuracyStage(self, change):
        self.accuracyStage += change

    def changeEvasionStage(self, change):
        self.evasionStage += change

    def setStatus(self, change):
        self.status = change

    def resetStages(self):
        self.atkStage = 0
        self.defenseStage = 0
        self.sp_atkStage = 0
        self.sp_defStage = 0
        self.speedStage = 0
        self.accuracyStage = 0
        self.evasionStage = 0
