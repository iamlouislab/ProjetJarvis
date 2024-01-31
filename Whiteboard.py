import ingescape as igs

def printMessage(message) : 
    igs.service_call("Whiteboard", "chat", (message),"")

def printWaitingGif() :
    igs.service_call("Whiteboard", "addImageFromUrl", ("https://cdn.pixabay.com/animation/2023/11/30/10/11/10-11-02-622_256.gif", 250, 100), "")

def unprintWaitingGif(id) :
    igs.service_call("Whiteboard", "remove", (id), "")

def clear(): 
    igs.service_call("Whiteboard", "clear", (), "")

def printSpeakingGif() :
    igs.service_call("Whiteboard", "addImageFromUrl", ("https://cdn.pixabay.com/animation/2023/11/30/10/11/10-11-02-622_256.gif", 250, 100), "")

def unprintSpeakingGif() :
    igs.service_call("Whiteboard", "remove", (1), "")