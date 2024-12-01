# Track Coach the Game!! by Oliver Graham ograham
# imports
from cmu_graphics import *
import random
import math
import copy


# character
class athlete:
    def __init__(self, name, power, technique, endurance, year=1):
        self.name = name
        self.power = power
        self.tec = technique
        self.endure = (
            endurance  # for events but also slows degredation throughout a meet
        )
        self.baseStates = [power, technique, endurance]
        self.trainged = [0, 0, 0]
        self.year = year
        self.injured = False
        self.highlighted = False
        self.selected = False

    def __repr__(self):
        return (
            "athlete: "
            + self.name
            + " power: "
            + str(self.power)
            + " technique: "
            + str(self.tec)
            + " endurance: "
            + str(self.endure)
            + " year: "
            + str(self.year)
        )


class team:
    def __init__(self):
        self.team = []
        self.size = 10

    def makeRoster(self):
        temp = []
        for i in range(self.size):
            temp.append(makeAthlete())
        self.team = temp

    def __repr__(self):
        temp = ""
        for i in self.team:
            temp += str(i) + "\n"
        return "your team: \n" + temp

    def newyear(self):
        for athlete in self.team:
            if athlete.year == 4:
                self.team.remove(athlete)
        if len(self.team) < 8:
            for i in range(random.randint(8 - len(self.team), 12 - len(self.team))):
                self.team.append(makeAthlete(0))
        elif len(self.team) < 12:
            for i in range(random.randint(0, 12 - len(self.team))):
                self.team.append(makeAthlete(0))


#  generate a athlete
def makeAthlete(year=-1):
    # list of names is generated by bingAI thanks bing I didn't want to have to make a really long list of names this would've taken forever
    popular_first_names = [
        "Liam",
        "Noah",
        "Oliver",
        "Elijah",
        "James",
        "William",
        "Benjamin",
        "Lucas",
        "Henry",
        "Alexander",
        "Olivia",
        "Emma",
        "Ava",
        "Sophia",
        "Isabella",
        "Mia",
        "Charlotte",
        "Amelia",
        "Harper",
        "Evelyn",
        "John",
        "Michael",
        "David",
        "Chris",
        "Sarah",
        "Ashley",
        "Emily",
        "Jessica",
        "Madison",
        "Aiden",
        "Ethan",
        "Logan",
        "Mason",
        "Sebastian",
        "Jack",
        "Daniel",
        "Matthew",
        "Samuel",
        "Joseph",
        "Jackson",
        "Aria",
        "Grace",
        "Chloe",
        "Ella",
        "Abigail",
        "Scarlett",
        "Zoey",
        "Lily",
        "Hannah",
        "Addison",
        "Samantha",
        "Luna",
        "Layla",
        "Ellie",
        "Riley",
        "Levi",
        "Owen",
        "Wyatt",
        "Gabriel",
        "Carter",
        "Julian",
        "Dylan",
        "Lincoln",
        "Leo",
        "Isaac",
        "Victoria",
        "Nora",
        "Hazel",
        "Mila",
        "Penelope",
        "Lillian",
        "Aubrey",
        "Eleanor",
        "Bella",
        "Savannah",
        "Christian",
        "Hunter",
        "Jameson",
        "Isaiah",
        "Grayson",
        "Nathan",
        "Aaron",
        "Adrian",
        "Eli",
        "Jonathan",
        "Lucy",
        "Paisley",
        "Brooklyn",
        "Aurora",
        "Skylar",
        "Genesis",
        "Naomi",
        "Elena",
        "Caroline",
        "Violet",
        "Mackenzie",
        "Autumn",
        "Kennedy",
        "Natalie",
        "Isabelle",
    ]
    if year == -1:
        return athlete(
            random.choice(popular_first_names),
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 4),
        )
    else:
        return athlete(
            random.choice(popular_first_names),
            random.randint(1, 10),
            random.randint(1, 10),
            random.randint(1, 10),
            random.choice([1, 1, 1, 1, 2, 2, 2, 3, 3, 4]),
        )


# events


def m100(athlete):
    return athlete.power


def m200(athlete):
    return athlete.power * 0.8 + athlete.endure * 0.2


def m400(athlete):
    return athlete.power * 0.4 + athlete.endure * 0.6


def m800(athlete):
    return athlete.power * 0.3 + athlete.endure * 0.7


def m1600(athlete):
    return athlete.power * 0.2 + athlete.endure * 0.8


def m3200(athlete):
    return athlete.power * 0.1 + athlete.endure * 0.9


def discus(athlete):
    return athlete.power * 0.4 + athlete.tec * 0.6


def shotput(athlete):
    return athlete.power * 0.7 + athlete.tec * 0.3


def jav(athlete):
    return athlete.power * 0.3 + athlete.tec * 0.7


def long(athlete):
    return athlete.power * 0.7 + athlete.tec * 0.3


def high(athlete):
    return athlete.power * 0.6 + athlete.tec * 0.4


def polevault(athlete):
    return athlete.power * 0.3 + athlete.tec * 0.7


def h110(athlete):
    return athlete.power * 0.5 + athlete.tec * 0.5


def h400(athlete):
    return athlete.power * 0.2 + athlete.endure * 0.3 + athlete.tec * 0.5


eventList = [
    m100,
    m200,
    m400,
    m800,
    m1600,
    m3200,
    discus,
    shotput,
    jav,
    long,
    high,
    polevault,
    h110,
    h400,
]


# trainings:
def enduranceTraining():
    for athlete in myteam.team:
        if athlete.selected:
            athlete.endure += random.choice(
                [
                    -1,
                    0,
                    1,
                    1,
                    1,
                    1,
                    2,
                ]
            )
            if athlete.endure > 10:
                athlete.endure = 10
            if athlete.endure <= 1:
                athlete.endure = 1


def powerTraining():
    for athlete in myteam.team:
        if athlete.selected:
            athlete.power += random.choice(
                [
                    -1,
                    0,
                    1,
                    1,
                    1,
                    1,
                    2,
                ]
            )
            if athlete.power > 10:
                athlete.power = 10
            if athlete.power <= 1:
                athlete.power = 1


def tecTraining():
    for athlete in myteam.team:
        if athlete.selected:
            athlete.tec += random.choice(
                [
                    -1,
                    0,
                    1,
                    1,
                    1,
                    1,
                    2,
                ]
            )
            if athlete.tec > 10:
                athlete.tec = 10
            if athlete.tec <= 1:
                athlete.tec = 1


# output
def onAppStart(app):
    app.width = 1500
    app.height = 700
    app.game = False
    app.background = "darkGreen"
    app.help = False
    app.meet = False
    app.endureTrain = False
    app.tecTrain = False
    app.powerTrain = False
    app.eventsList = [
        "100M dash",
        "200M dash",
        "400m dash",
        "800m dash",
        "1600m",
        "3200m",
        "discus",
        "shotput",
        "javolin",
        "long Jump",
        "high Jump",
        "polevault",
        "110m hurdles",
        "400m hurdles",
    ]
    app.currentEvent = 0
    app.playerScore = 0
    app.opponentScore = 0
    app.cardSelected = False
    app.selected = None
    pass


def redrawAll(app):
    if app.game:
        drawTrack(app)
        for i in range(len(myteam.team)):
            makeCard(
                i * 1500 / len(myteam.team) + ((0.5 * 1500 / len(myteam.team)) - 55),
                app.height - 210,
                myteam.team[i],
            )
        if app.meet:
            drawMeet(app)
        else:
            drawPractice(app)
    elif app.help:
        drawHelp(app)
    else:
        drawHome(app)


def drawMeet(app):  # need to do
    drawRect(app.width - 340, app.height / 2 + 30, 300, 50, fill="gray")
    drawLabel(
        "Your Score: " + str(app.playerScore),
        app.width - 190,
        app.height / 2 + 50,
        size=42,
        fill="blue",
    )
    drawRect(app.width - 340, app.height / 2 - 80, 300, 50, fill="gray")
    drawLabel(
        "computer's Score: " + str(app.opponentScore),
        app.width - 190,
        app.height / 2 - 50,
        size=32,
        fill="red",
    )
    for i in range(len(otherTeam.team)):
        makeCard(
            i * 1500 / len(otherTeam.team) + ((0.5 * 1500 / len(otherTeam.team)) - 55),
            20,
            otherTeam.team[i],
            True,
        )
    drawRect(app.width / 2 - 400, app.height / 2 - 100, 800, 200, fill="gray")
    drawLabel(
        app.eventsList[app.currentEvent], app.width / 2 - 100, app.height / 2, size=100
    )
    makeCard(
        app.width / 2 + 200,
        app.height / 2 - 100,
        computerPick()[app.currentEvent],
        True,
    )


def drawPractice(app):
    drawLabel(
        "pick one athlete for each type of training:",
        app.width / 2,
        150,
        size=50,
        fill="white",
    )
    # tec
    if not app.tecTrain:
        drawRect(app.width / 2 - 400, app.height / 2 - 100, 200, 200, fill="red")
        drawLabel("Train Technique", app.width / 2 - 300, app.height / 2 - 80, size=20)
        drawLabel(
            "useful in events that require form:",
            app.width / 2 - 300,
            app.height / 2 - 40,
        )
        drawLabel("like hurdles and throws", app.width / 2 - 300, app.height / 2 - 30)

    # power
    if not app.powerTrain:
        drawRect(app.width / 2 - 100, app.height / 2 - 100, 200, 200, fill="green")
        drawLabel("Train Power", app.width / 2, app.height / 2 - 80, size=20)
        drawLabel(
            "useful in events that require strength:",
            app.width / 2,
            app.height / 2 - 40,
        )
        drawLabel("like shot put or sprinting", app.width / 2, app.height / 2 - 30)

    # endure
    if not app.endureTrain:
        drawRect(app.width / 2 + 200, app.height / 2 - 100, 200, 200, fill="blue")
        drawLabel("Train Endurance", app.width / 2 + 300, app.height / 2 - 80, size=20)
        drawLabel("useful in longer events", app.width / 2 + 300, app.height / 2 - 40)
        drawLabel("like long running events", app.width / 2 + 300, app.height / 2 - 30)
        drawLabel("or doing multiple events", app.width / 2 + 300, app.height / 2 - 20)

    pass


def drawHome(app):

    drawTrack(app)
    drawLabel(
        "Track and Field the Card game",
        app.width / 2,
        app.height / 4,
        size=50,
        bold=True,
    )
    drawRect(app.width / 2 - 200, app.height / 2 - 100, 400, 200, fill="lightGray")
    drawLabel("PLAY!", app.width / 2, app.height / 2, size=120)
    drawRect(app.width / 2 - 100, app.height / 2 + 150, 200, 50, fill="lightGray")
    drawLabel("Help!", app.width / 2, app.height / 2 + 175, size=30)


def drawHelp(app):  # needs to be done
    drawRect(0, 0, app.width, app.height, fill="white")
    drawLabel(
        "instructions on how to play, click anywhere to exit back to home", 20, 20
    )


def startGame(app):
    pass


def drawTrack(app):
    for i in range(10):
        drawArc(
            app.height / 2,
            app.height / 2,
            app.height - 25 * i,
            app.height - 25 * i,
            90,
            180,
            border="white",
        )
        drawArc(
            app.width - app.height / 2,
            app.height / 2,
            app.height - 25 * i,
            app.height - 25 * i,
            -90,
            180,
            border="white",
        )
        if i == 9:
            drawRect(
                app.height / 2 - 2.5,
                0 + 12.5 * i,
                app.width - app.height + 5,
                app.height - 25 * i,
                fill="darkGreen",
            )
            drawCircle(app.width / 2, app.height / 2, 75)
            drawLine(
                app.height / 2,
                9 * 12.5,
                app.height / 2 + app.width - app.height,
                9 * 12.5,
                fill="white",
                lineWidth=2,
            )
            drawLine(
                app.height / 2,
                app.height - 9 * 12.5,
                app.height / 2 + app.width - app.height,
                app.height - 9 * 12.5,
                fill="white",
                lineWidth=2,
            )
        else:
            drawRect(
                app.height / 2,
                0 + 12.5 * i,
                app.width - app.height,
                app.height - 25 * i,
                border="white",
            )


def makeCard(x, y, athlete, AI=False):
    color = "black"
    cardColor = RGB(athlete.tec * 25.5, athlete.power * 25.5, athlete.endure * 25.5)
    if athlete.selected:
        drawRect(x, y, 110, 200, fill=cardColor, borderWidth=20, border="gold")
    elif athlete.highlighted:
        drawRect(x, y, 110, 200, fill=cardColor, borderWidth=10, border="gold")
    else:
        drawRect(x, y, 110, 200, fill=cardColor)
    if (athlete.tec * 25.5 + athlete.power * 25.5 + athlete.endure * 25.5) / 3 <= 150:
        color = "white"
    if not AI:
        drawLabel(athlete.name, x + 55, y + 5, align="top", fill=color, size=20)
        drawLabel(
            "Year: " + str(athlete.year),
            x + 100,
            y + 30,
            align="top",
            fill=color,
            size=20,
            rotateAngle=90,
        )
        drawRect(x + 20, y + 25, 70, 70, fill="white")
        drawCircle(x + 55, y + 60, 30, fill="yellow")
        drawCircle(x + 55, y + 65, 20, fill="pink")
        drawRect(x + 35, y + 45, 40, 20, fill="yellow")
        drawCircle(x + 47, y + 52, 10, fill="white")
        drawCircle(x + 63, y + 52, 10, fill="white")
        drawCircle(x + 63, y + 52, 5)
        drawCircle(x + 47, y + 52, 5)
        drawLabel(
            "technique: " + str(athlete.tec), x + 55, y + 100, align="top", fill=color
        )
        drawRect(x + 5, y + 120, athlete.tec * 10, 10, fill="red", border=color)
        drawLabel(
            "power: " + str(athlete.power), x + 55, y + 133, align="top", fill=color
        )
        drawRect(x + 5, y + 150, athlete.power * 10, 10, fill="green", border=color)
        drawLabel(
            "endurance: " + str(athlete.endure),
            x + 55,
            y + 166,
            align="top",
            fill=color,
        )
        drawRect(x + 5, y + 180, athlete.endure * 10, 10, fill="blue", border=color)
    if AI:
        drawRect(x + 20, y + 25, 70, 70, fill="white")
        drawCircle(x + 55, y + 60, 30, fill="yellow")
        drawRect(x + 35, y + 75, 40, 5, fill="red")
        drawCircle(x + 47, y + 52, 10, fill="white")
        drawCircle(x + 63, y + 52, 10, fill="white")
        drawCircle(x + 63, y + 52, 5)
        drawCircle(x + 47, y + 52, 5)
        drawLabel("technique: ", x + 55, y + 100, align="top", fill=color)
        drawRect(
            x + 5,
            y + 120,
            athlete.tec * 10 + (random.random() - 0.5) * 2,
            10,
            fill=gradient("red", cardColor, start="left"),
        )
        drawLabel("power: ", x + 55, y + 133, align="top", fill=color)
        drawRect(
            x + 5,
            y + 150,
            athlete.power * 10 + (random.random() - 0 / 5) * 2,
            10,
            fill=gradient("green", cardColor, start="left"),
        )
        drawLabel("endurance: ", x + 55, y + 166, align="top", fill=color)
        drawRect(
            x + 5,
            y + 180,
            athlete.endure * 10 + (random.random() - 0 / 5) * 2,
            10,
            fill=gradient("blue", cardColor, start="left"),
        )


def main():
    runApp()


# AI

""" code recieved from my brother

func_list = [ a, b, c ]

cur_max = 0

for func in func_list:
    cur_max = max(func(10), cur_max)

"""


def computerPick():  # terrible returns list in order of events no wearing out yet
    bestList = []
    bestScore = 0
    best = None
    for event in eventList:
        for athlete in otherTeam.team:
            if best == None:
                best = athlete
            elif event(athlete) > event(best):
                best = athlete
        bestList.append(best)
        best = None
        bestScore = 0
    return bestList


    """bestList = []
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if m100(athlete) > bestScore:
                best = athlete
                bestScore = m100(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if m200(athlete) > bestScore:
                best = athlete
                bestScore = m200(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if m400(athlete) > bestScore:
                best = athlete
                bestScore = m400(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if m800(athlete) > bestScore:
                best = athlete
                bestScore = m800(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if m1600(athlete) > bestScore:
                best = athlete
                bestScore = m1600(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if m3200(athlete) > bestScore:
                best = athlete
                bestScore = m3200(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if discus(athlete) > bestScore:
                best = athlete
                bestScore = discus(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if shotput(athlete) > bestScore:
                best = athlete
                bestScore = shotput(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if jav(athlete) > bestScore:
                best = athlete
                bestScore = jav(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if long(athlete) > bestScore:
                best = athlete
                bestScore = long(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if high(athlete) > bestScore:
                best = athlete
                bestScore = high(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if polevault(athlete) > bestScore:
                best = athlete
                bestScore = polevault(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if h110(athlete) > bestScore:
                best = athlete
                bestScore = h110(athlete)
    bestList.append(best)
    best = None
    bestScore = 0
    for athlete in otherTeam.team:
        if best == None:
            best = athlete
        else:
            if h400(athlete) > bestScore:
                best = athlete
                bestScore = h400(athlete)
    return bestList"""


# meet


# input
def onMousePress(app, mouseX, mouseY):
    if app.help:
        app.help = not app.help
    if not app.game:
        if (
            app.width / 2 - 200 < mouseX < app.width / 2 + 200
            and app.height / 2 - 100 < mouseY < app.height / 2 + 100
        ):
            app.game = True
        if (
            app.width / 2 - 100 < mouseX < app.width / 2 + 100
            and app.height / 2 + 150 < mouseY < app.height / 2 + 200
        ):
            app.help = True
    else:
        if not app.meet:
            if (
                app.width / 2 - 400 < mouseX < app.width / 2 - 200
                and app.height / 2 + 120 > mouseY > app.height / 2 - 80
                and not app.tecTrain
                and app.cardSelected
            ):
                tecTraining()
                app.tecTrain = True
            elif (
                app.width / 2 - 100 < mouseX < app.width / 2 + 100
                and app.height / 2 + 120 > mouseY > app.height / 2 - 80
                and not app.powerTrain
                and app.cardSelected
            ):
                powerTraining()
                app.powerTrain = True
            elif (
                app.width / 2 + 200 < mouseX < app.width / 2 + 400
                and app.height / 2 + 120 > mouseY > app.height / 2 - 80
                and not app.endureTrain
                and app.cardSelected
            ):
                enduranceTraining()
                app.endureTrain = True
            if app.tecTrain and app.powerTrain and app.endureTrain:
                app.meet = True
        else:

            if (
                (app.width / 2) - 400 < mouseX < (app.width / 2) + 400
                and (app.height / 2) - 100 < mouseY < (app.height / 2) + 100
                and app.cardSelected
            ):
                if app.selected != None:
                    if (eventList[app.currentEvent](app.selected)) > eventList[app.currentEvent](computerPick()[app.currentEvent]):
                        print('you: '+ str(eventList[app.currentEvent](app.selected)))
                        print('them: '+ str(eventList[app.currentEvent](computerPick()[app.currentEvent])))
                        app.playerScore +=1
                        print('you win')
                    elif (eventList[app.currentEvent](app.selected)) == eventList[app.currentEvent](computerPick()[app.currentEvent]):
                        print('you: '+ str(eventList[app.currentEvent](app.selected)))
                        print('them: '+ str(eventList[app.currentEvent](computerPick()[app.currentEvent])))
                        print('you tied')
                    else:
                        print('you: '+ str(eventList[app.currentEvent](app.selected)))
                        print('them: '+ str(eventList[app.currentEvent](computerPick()[app.currentEvent])))
                        app.opponentScore +=1
                        print('you lose')
                    app.currentEvent +=1

        for i in range(len(myteam.team)):
            if (
                i * 1500 / len(myteam.team) + ((0.5 * 1500 / len(myteam.team)) - 55)
                < mouseX
                < i * 1500 / len(myteam.team)
                + ((0.5 * 1500 / len(myteam.team)) - 55)
                + 110
                and mouseY > 480
            ):
                if myteam.team[i].selected == True:
                    app.cardSelected = False
                    myteam.team[i].selected = False
                    app.selected = None
                else:
                    app.cardSelected = True
                    for athlete in myteam.team:
                        athlete.selected = False
                    myteam.team[i].selected = True
                    app.selected = myteam.team[i]

                    break
            else:
                app.selected = None
                app.cardSelected = False
                myteam.team[i].selected = False


def onMouseMove(app, mouseX, mouseY):
    for i in range(len(myteam.team)):
        if (
            i * 1500 / len(myteam.team) + ((0.5 * 1500 / len(myteam.team)) - 55)
            < mouseX
            < i * 1500 / len(myteam.team) + ((0.5 * 1500 / len(myteam.team)) - 55) + 110
            and mouseY > 480
        ):
            myteam.team[i].highlighted = True
        else:
            myteam.team[i].highlighted = False


def onKeyPress(app, key):  # only escape to home works
    if key == "escape":
        app.game = False


# running
myteam = team()
myteam.makeRoster()
otherTeam = team()
otherTeam.makeRoster()
myteam.newyear()
main()
