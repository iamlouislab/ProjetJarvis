import flask
import signal
import getopt
import time
from pathlib import Path
import sys
import ingescape as igs

from VoiceHandling import *

app = flask.Flask(__name__)

port = 9182
agent_name = "VoiceHandling"
device = None
verbose = False
is_interrupted = False

short_flag = "hvip:d:n:"
long_flag = ["help", "verbose", "interactive_loop", "port=", "device=", "name="]

ingescape_path = Path("~/Documents/Ingescape").expanduser()


@app.route("/", methods=["GET"])
def index():
    return "Hello, World!"


@app.route("/voice_path_input_callback", methods=["POST"])
def voice_data():
    # get voice data from request
    voice_data = flask.request.get_data()

    # save voice data to file
    with open("voice.mp3", "wb") as f:
        f.write(voice_data)

    # send file path to output
    agent.voice_file_pathO = "voice.mp3"

    return "OK"


if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], short_flag, long_flag)
    except getopt.GetoptError as err:
        igs.error(err)
        sys.exit(2)
    for o, a in opts:
        if o == "-h" or o == "--help":
            exit(0)
        elif o == "-v" or o == "--verbose":
            verbose = True
        elif o == "-i" or o == "--interactive_loop":
            interactive_loop = True
        elif o == "-p" or o == "--port":
            port = int(a)
        elif o == "-d" or o == "--device":
            device = a
        elif o == "-n" or o == "--name":
            agent_name = a
        else:
            assert False, "unhandled option"

    igs.agent_set_name(agent_name)
    igs.definition_set_version("1.0")
    igs.log_set_console(verbose)
    igs.log_set_file(True, None)
    igs.log_set_stream(verbose)
    igs.set_command_line(sys.executable + " " + " ".join(sys.argv))

    agent = VoiceHandling()

    igs.start_with_device(device, port)

    # start flask server
    app.run()

    while (not is_interrupted) and igs.is_started():
        time.sleep(2)

    if igs.is_started():
        igs.stop()
