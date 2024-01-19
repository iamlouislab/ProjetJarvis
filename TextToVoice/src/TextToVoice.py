#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  TextToVoice.py
#  TextToVoice version 1.0
#  Created by Ingenuity i/o on 2024/01/08
#
# "no description"
#
import ingescape as igs
from gtts import gTTS
import pygame


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TextToVoice(metaclass=Singleton):
    def __init__(self):
        # inputs
        self.textI = None

        # outputs
        self._voiceO = None

    # outputs
    @property
    def voiceO(self):
        return self._voiceO

    @voiceO.setter
    def voiceO(self, value):
        self._voiceO = value
        if self._voiceO is not None:
            igs.output_set_data("voice", value)


def text_to_speech(text, lang="en"):
    """
    Convert text to speech and save it as an MP3 file.

    Args:
    text (str): The text to be converted to speech.
    lang (str, optional): The language of the text. Defaults to 'en' (English).
    """
    tts = gTTS(text=text, lang=lang)
    filename = "speech.mp3"
    tts.save(filename)
    print(f"Saved as {filename}")

    with open(filename, "rb") as f:
        data = f.read()

    print("reading sound file...")
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    return data
