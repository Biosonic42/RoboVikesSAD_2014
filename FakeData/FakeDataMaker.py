import random

teams = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

TrueFalse = [0,1]
MatchesFull = []

totalData = []

def FullCheck(List, x, y):
    occurences = 0
    for element in List:
        if element == x: occurences += 1

    return occurences >= y
  
for team in teams:
    i = 0
    MatchNums = []
    teamData = []
    MatchNum = 0
    HadAuto = 0
    while i < 12: # give each team 12 matches
        matchData = []
        while MatchNum in MatchesFull or MatchNum == 0 or FullCheck(MatchNums, MatchNum, 1):
            MatchNum = random.randrange(1,81)

        MatchNums.append(MatchNum)
        if FullCheck(MatchNums, MatchNum, 6): MatchesFull.append(MatchNum)
        
        TeamNum = team

        AllianceColor = 1 if FullCheck(MatchNums, MatchNum, 3) else 0

        if HadAuto != 1: HadAuto = random.randrange(0,10)
        HadAuto = 1 if HadAuto<4 and HadAuto>0 else 0
        GoalieZone = random.choice(TrueFalse) if HadAuto == 1 else 0
        MobilityBonus = random.choice(TrueFalse) if HadAuto == 1 and GoalieZone == 0 else 0
        autoHighScore = random.randrange(0,4) if HadAuto == 1 and GoalieZone == 0 else 0
        autoLowScore = random.randrange(0,4-autoHighScore) if HadAuto == 1 and GoalieZone == 0 and 4-autoHighScore>0 else 0
        autoScores = autoHighScore+autoLowScore
        autoHotScore = random.randrange(0,autoScores) if HadAuto == 1 and GoalieZone == 0 and autoScores>0 else 0

        Disabled = random.randrange(0,25)
        Disabed = 1 if Disabled == 24 else 0
        Broken = random.randrange(0,50)
        Broken = 1 if Broken == 49 else 0

        NumberOfCycles = random.randrange(1,15)

        teleHighScore = random.randrange(0,NumberOfCycles) if Disabled == 0 and Broken == 0 else 0
        teleHighAttempt = random.randrange(teleHighScore, NumberOfCycles*3) if Disabled == 0 and Broken == 0 else 0
        teleLowScore = random.randrange(0,NumberOfCycles) if Disabled == 0 and Broken == 0 else 0
        teleLowAttempt = random.randrange(teleLowScore, NumberOfCycles*3) if Disabled == 0 and Broken == 0 else 0
        teleTrussScore = random.randrange(0,NumberOfCycles) if Disabled == 0 and Broken == 0 else 0
        teleCatchScore = random.randrange(0,NumberOfCycles-teleTrussScore) if Disabled == 0 and Broken == 0 and (NumberOfCycles-teleTrussScore)>0 else 0
        teleAssistScore = random.randrange(0,NumberOfCycles*2) if Disabled == 0 and Broken == 0 else 0            

        Defensive = random.randrange(0,20)
        Defensive = 1 if Defensive == 19 else 0
        Technical = random.randrange(0,25) if Disabled == 0 and Broken == 0 else 0
        if Technical >= 4:
            Technical = 0
        Regular = random.randrange(0,20) if Disabled == 0 and Broken == 0 else 0
        if Regular >= 6:
            Regular = 0
        YellowPenalty = random.randrange(0,50)
        YellowPenalty = 1 if YellowPenalty == 49 and Disabled == 0 and Broken == 0 else 0
        RedPenalty = random.randrange(0,100)
        RedPenalty = 1 if RedPenalty == 99 and Disabled == 0 and Broken == 0 else 0

        matchData.append(MatchNum)
        matchData.append(TeamNum)
        matchData.append(AllianceColor)

        matchData.append(HadAuto)
        matchData.append(MobilityBonus)
        matchData.append(GoalieZone)
        matchData.append(autoHighScore)
        matchData.append(autoLowScore)
        matchData.append(autoHotScore)

        matchData.append(teleHighScore)
        matchData.append(teleHighAttempt)
        matchData.append(teleLowScore)
        matchData.append(teleLowAttempt)
        matchData.append(teleTrussScore)
        matchData.append(teleCatchScore)
        matchData.append(teleAssistScore)
        
        matchData.append(Regular)
        matchData.append(Technical)
        matchData.append(Disabled)
        matchData.append(Broken)
        matchData.append(YellowPenalty)
        matchData.append(RedPenalty)
        matchData.append(Defensive)
        
        teamData.append(matchData)

        i+=1

    totalData.append(teamData)

dataFile = open("data.txt", "w")
dataFile.writelines(["%s\n" % item for item in totalData])
