# uncompyle6 version 2.9.10
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.10 (default, Feb  6 2017, 23:53:20) 
# [GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.34)]
# Embedded file name: type_Result.py
from types import *
import mcl.object.MclTime

class Result:

    def __init__(self):
        self.__dict__['hopNum'] = 0
        self.__dict__['tripTime'] = mcl.object.MclTime.MclTime()
        self.__dict__['host'] = ''

    def __getattr__(self, name):
        if name == 'hopNum':
            return self.__dict__['hopNum']
        if name == 'tripTime':
            return self.__dict__['tripTime']
        if name == 'host':
            return self.__dict__['host']
        raise AttributeError("Attribute '%s' not found" % name)

    def __setattr__(self, name, value):
        if name == 'hopNum':
            self.__dict__['hopNum'] = value
        elif name == 'tripTime':
            self.__dict__['tripTime'] = value
        elif name == 'host':
            self.__dict__['host'] = value
        else:
            raise AttributeError("Attribute '%s' not found" % name)

    def Marshal(self, mmsg):
        from mcl.object.Message import MarshalMessage
        submsg = MarshalMessage()
        submsg.AddU16(MSG_KEY_RESULT_HOP_NUMBER, self.__dict__['hopNum'])
        submsg.AddTime(MSG_KEY_RESULT_TRIP_TIME, self.__dict__['tripTime'])
        submsg.AddStringUtf8(MSG_KEY_RESULT_HOST, self.__dict__['host'])
        mmsg.AddMessage(MSG_KEY_RESULT, submsg)

    def Demarshal(self, dmsg, instance=-1):
        import mcl.object.Message
        msgData = dmsg.FindData(MSG_KEY_RESULT, mcl.object.Message.MSG_TYPE_MSG, instance)
        submsg = mcl.object.Message.DemarshalMessage(msgData)
        self.__dict__['hopNum'] = submsg.FindU16(MSG_KEY_RESULT_HOP_NUMBER)
        self.__dict__['tripTime'] = submsg.FindTime(MSG_KEY_RESULT_TRIP_TIME)
        self.__dict__['host'] = submsg.FindString(MSG_KEY_RESULT_HOST)