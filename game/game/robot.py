import config

def updaterobot(status):
    config.robot_status = status

def checkending():
    if config.robot_status == "sad":
        print "The robot is sad. This is a Bad End."
    else:
        print "You got a Good End!"