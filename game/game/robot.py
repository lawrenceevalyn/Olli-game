import config

def updaterobot(status):
    config.robot_status = status

def checkending():
    if config.robot_status == "sad":
        print "The robot is sad. This is a Bad End."
        
    elif config.robot_status == "wantsstory":
        print "The robot is glad to have its companion back, but is still restless. This is a mediocre end."
        
    else:
        print "You got a Good End!"