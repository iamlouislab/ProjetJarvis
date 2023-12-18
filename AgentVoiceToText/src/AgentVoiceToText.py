#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  AgentVoiceToText.py
#  AgentVoiceToText version 1.0
#  Created by Ingenuity i/o on 2023/12/18
#
# "no description"
#
import ingescape as igs


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class AgentVoiceToText(metaclass=Singleton):
    def __init__(self):
        # inputs
        self.voiceI = None

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


