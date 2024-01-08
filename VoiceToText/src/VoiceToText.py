#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  VoiceToText.py
#  VoiceToText version 1.0
#  Created by Ingenuity i/o on 2024/01/08
#
# "no description"
#
import ingescape as igs
import speech_recognition as sr
from pydub import AudioSegment


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class VoiceToText(metaclass=Singleton):
    def __init__(self):
        # inputs
        self.voice_pathI = None

        # outputs
        self._textO = None

    # outputs
    @property
    def textO(self):
        return self._textO

    @textO.setter
    def textO(self, value):
        self._textO = value
        if self._textO is not None:
            igs.output_set_string("text", self._textO)


def mp3_to_wav(mp3_file):
    """
    Convert mp3 file to wav format.
    """
    sound = AudioSegment.from_mp3(mp3_file)
    wav_file = mp3_file.replace(".mp3", ".wav")
    sound.export(wav_file, format="wav")
    return wav_file


def speech_to_text(audio_file):
    """
    Convert speech in an audio file to text.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio"
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service"


def path_to_text(path):
    wav_file = mp3_to_wav(path)
    text = speech_to_text(wav_file)
    return text
