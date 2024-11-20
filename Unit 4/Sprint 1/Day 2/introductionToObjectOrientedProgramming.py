#Note: Python supports various kind of programming paradigm(the way/style of writing code).

#There are following types of programming paradigm:
#1. Procedural programming [Done]
#2. Functional Programming [Done]
#3. Object Oriented Programming [Pending]

#Why Object Oriented Programming?
#Note: in object oriented programming everything is object or you can say object is first citizen.

#Reason: In real world, everything is object, and in each object two things are common.
#1. how they look/state/property
#2. how they act/behavior/functionality

"""
Examples:
Mobile: Object
1. how they look/state/property
    brandName
    model
    backCamera
    frontCamera
    bettery
    color
2. how they act/behavior/functionality
    playMusic
    pauseMusic
    playVideo
    doVideoCall
    audioCall
    doMsg
Bike: Object
1. how they look/state/property
    model
    brand
    wheels
2. how they act/behavior/functionality
    move
    brake
    increase speed

Technically - how they look/state/property - state/variable/property
Technically - how they act/behave/functionality - functionality/method/behavior

Before object Oriented programming, we're having to write these two(state and behavior)things sepereatly

"""


#Before Object Oriented Programming Example:

#Account: Object

#Functions/behaviors/acts

def depositMoney(accountNumber, availBalance, amount):
    pass

def withdrawalMoney(accountNumber, availBalance, amount):
    pass 
    
def checkBalance(accountNumber, availBalance, amount):
    pass


#States/Properties/looks
accountNumber = "123456789"
availableBalance = 5000


#According to above example, in this case your code follows following things:
#redudancy/duplicay
#less secure data
#there is no modelarity


#With the help object oriented programming, we bind these two important things about object as single entity.