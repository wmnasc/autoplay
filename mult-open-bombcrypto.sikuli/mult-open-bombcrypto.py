import random
import base64
import datetime
import java.lang.System as JSYS

ciclo = 0
status = "waiting"
message = "waiting"

### ALERT MESSAGE ###
inicio = "Starting"
fim = "Success"
off = "Bot - offline"
error1 = "Error - General failure, restarting"
error2 = "Error - Wallet error, restarting"
error3 = "Error - MetaMask error, restarting"
done = "done"
reloadPage = "Reloading page"
connectMeta = "Conecting Metamask"
loadHeromsg = "Loading heros"
meta1 = "Wallet (1)"
meta2 = "Wallet (2)"
meta3 = "Wallet (3)"
meta4 = "Wallet (4)"

### IMPORT PASSWORD ###
with open ('pass.txt','r') as f:
    metamask = f.read()
    f.close()
    pw = base64.b64decode(metamask).decode('utf-8')

### SAVE LOG ###
def logfile():
    global message
    time = datetime.datetime.now()
    time = time.strftime("%d/%m/%Y %H:%M:%S")
    f=open("log.txt", "a")
    f.write("\n" + time + " - " + message)
    f.close()

### BOT STATUS ###
def runbot():
    global status
    with open ('botStatus.txt','r') as a:
        status = a.read()
        a.close()

### PAGE RELOAD ###
def forceReload():
    keyDown(Key.CTRL + Key.F5)

def simpleReload():
    sleep(2)
    type('r',Key.CTRL)

def waitConnect():
    global message
    global ciclo
    sleep(10)
    connectload = 0
    while not exists ("1641697213577.png"):
        sleep(5)
        connectload += 1
        if connectload > 12:
            connectload = 0
            message = error2
            logfile()
            sleep(random.randrange(1,600))
            forceReload()

def rload1():
    sleep(5)
    click(Location(322, 201)) #Tela 1
    simpleReload()
    waitConnect()
    click(Location(322, 347)) #Connect wallet
    
def rload2():
    sleep(5)
    click(Location(318, 666)) #Tela 2
    simpleReload()
    waitConnect()
    click(Location(329, 821)) #Connect wallet

def rload3():
    sleep(5)
    click(Location(970, 194)) #Tela 3
    simpleReload()
    waitConnect()
    click(Location(969, 352)) #Connect wallet

def rload4():
    sleep(5)
    click(Location(922, 717)) #Tela 4
    simpleReload()
    waitConnect()
    click(Location(970, 814)) #Connect wallet

def metamask():
    global message
    sleep(2)
    if exists ("1638061307171.png"):
        type(pw)
        click("1638061307171.png")
        while not exists ("1635776519047.png"):
            sleep(2)
        click("1635776519047.png")
        message = done
        logfile()
    else:
        if exists ("1635776519047.png"):
            click("1635776519047.png")
            message = done
            logfile()

def connect():
    global ciclo
    global message
    message = connectMeta
    logfile()
    load = 1
    while not exists("1641422420564.png"):
        metamask()
        load += 1
        if load > 30:
            load = 1
            message = error3
            logfile()
            sleep(random.randrange(1,300))
            if ciclo == 1:
                forceReload()
                rload1()
            elif ciclo == 2:
                forceReload()
                rload2()
            elif ciclo == 3:
                forceReload()
                rload3()
            elif ciclo == 4:
                forceReload()
                rload4()

def loadhero():
    global ciclo
    global message
    message = loadHeromsg
    logfile()
    click("1641422420564.png")
    sleep(8)
    if exists ("1641422541417.png", 2):
        click("1641422541417.png")
    sleep(5)
    click("1641422576755.png")
    sleep(3)
    click("1641422610010.png") #Comeca o jogo
    message = done
    logfile()
    ciclo += 1

def game1():
    global message
    message = meta1
    logfile()
    rload1()
    connect()
    loadhero()

def game2():
    global message
    message = meta2
    logfile()
    rload2()
    connect()
    loadhero()

def game3():
    global message
    message = meta3
    logfile()
    rload3()
    connect()
    loadhero()

def game4():
    global message
    message = meta4
    logfile()
    rload4()
    connect()
    loadhero()
    
while True:
    try:
        global status
        global message
        global ciclo
        runbot()
        if status == "online":
            message = inicio
            logfile()
            ciclo = 1
            game1()
            game2()
            game3()
            game4()
            message = fim
            logfile()
            JSYS.gc()
            sleep(random.randrange(5400,7200)) #Espera entre 1:30 e 2 horas para iniciar um novo jogo.
        elif status == "offline":
            message = off
            logfile()
            sleep(60)
    except FindFailed:
        message = error1
        logfile()
        sleep(random.randrange(1,600)) #Caso nao encontre os botoes, espera ate 10 min para uma proxima tentativa
        #popError("Did not work, try to restart")
