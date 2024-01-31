#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  VoiceHandling.py
#  VoiceHandling version 1.0
#  Created by Ingenuity i/o on 2024/01/31
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


class VoiceHandling(metaclass=Singleton):
    def __init__(self):
        pass
        # outputs
        self._voice_file_pathO = None

    # outputs
    @property
    def voice_file_pathO(self):
        return self._voice_file_pathO

    @voice_file_pathO.setter
    def voice_file_pathO(self, value):
        self._voice_file_pathO = value
        if self._voice_file_pathO is not None:
            igs.output_set_string("voice_file_path", self._voice_file_pathO)


