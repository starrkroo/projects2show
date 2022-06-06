#!/usr/bin/env python3


def attr(e,n,v): #will work for any object you feed it, but only that object
    class tmp(type(e)):
        def attr(self,n,v):
            setattr(self,n,v)
            return self
    return tmp(e).attr(n,v)


def reversing():

