# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModKYnDKRZg", version="0.0.1")
class Script_NeteaseModKYnDKRZg(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModKYnDKRZgServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModKYnDKRZgServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModKYnDKRZgClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModKYnDKRZgClientDestroy(self):
        pass
