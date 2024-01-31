import ingescape as igs


def printMessage(message):
    igs.service_call("Whiteboard", "chat", (message), "")


def printGif():
    print("NOT DONE YET")
    # igs.service_call("Whiteboard", "gif", (message), "")
