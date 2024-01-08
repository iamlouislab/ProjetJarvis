#!/usr/bin/env -P /usr/bin:/usr/local/bin python3 -B
# coding: utf-8

#
#  LLMAgent.py
#  LLMAgent version 1.0
#  Created by Ingenuity i/o on 2024/01/08
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


class LLMAgent(metaclass=Singleton):
    def __init__(self):
        # inputs
        self.promptI = None
        self.currentLLMI = None

        # outputs
        self._responseO = None

    # outputs
    @property
    def responseO(self):
        return self._responseO

    @responseO.setter
    def responseO(self, value):
        self._responseO = value
        if self._responseO is not None:
            igs.output_set_string("response", self._responseO)


