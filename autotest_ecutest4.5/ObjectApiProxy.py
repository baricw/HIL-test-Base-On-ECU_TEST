# -*- coding: utf-8 -*-

import sys

if sys.version_info < (3,):
    from xmlrpclib import Server, Marshaller, Unmarshaller, MAXINT, MININT
else:
    from xmlrpc.client import Server, Marshaller, Unmarshaller, MAXINT, MININT

def dump_long(_unused_self, value, write):
    if MININT <= value <= MAXINT:
        typecode = "int"
    else:
        typecode = "ex:i8"
    write('<value xmlns:ex="http://ws.apache.org/xmlrpc/namespaces/extensions"><%s>' % typecode)
    write("%d" % value)
    write("</%s></value>" % typecode)

if sys.version_info < (3,):
    Marshaller.dispatch[long] = dump_long
else:
    Marshaller.dispatch[int] = dump_long
Unmarshaller.dispatch.setdefault("i8", Unmarshaller.dispatch["int"])
Unmarshaller.dispatch.setdefault("ex:i8", Unmarshaller.dispatch["i8"])


class ObjectApiProxy(object):
    """
    Base functions to connect with the ECU-TEST Api.

    Each API call returns an object of this type.
    An instance of this class is representing a proxy for an API object.
    """

    PORTNUMBER = 8000
    def __init__(self, xmlRpc=None, objId=0):
        """
        Creates a new client connection to ECU-TEST.
        """
        if xmlRpc is None:
            # läuft extern, muss XMLRPC verwenden
            self._xmlRpc = Server('http://127.0.0.1:%s' % ObjectApiProxy.PORTNUMBER,
                                  allow_none=True)
        else:
            self._xmlRpc = xmlRpc
        self._objId = objId

    @staticmethod
    def SetPortNumber(portNumber):
        ObjectApiProxy.PORTNUMBER = portNumber

    def __str__(self):
        """
        Returns the name of the wrapped object

        :return: type name
        :rtype: unicode
        """
        return self._xmlRpc.ObjectApi.Str(self._objId)

    def __dir__(self):
        return self._xmlRpc.ObjectApi.Dir(self._objId)

    def _Call(self, methodName, *args, **kwargs):
        """
        For internal use only - do not call!
        """
        argList = [self._ConvertComplexTypeToProxyId(arg) for arg in args]
        argDict = dict((self._ConvertComplexTypeToProxyId(k),
                        self._ConvertComplexTypeToProxyId(v))
                        for k, v in kwargs.items())

        return self._xmlRpc.ObjectApi.Call(self._objId, methodName, argList, argDict)

    def __repr__(self):
        return "<Proxy for: {}>".format(self._xmlRpc.ObjectApi.Repr(self._objId))

    def __del__(self):
        self._xmlRpc.ObjectApi.Del(self._objId)

    def _ConvertComplexTypeToProxyId(self, value):
        """
        For internal use only - do not call!
        """
        if isinstance(value, (list, tuple)):
            return [self._ConvertComplexTypeToProxyId(v) for v in value]
        elif isinstance(value, dict):
            convertedDict = {}
            for k, v in value.items():
                convertedKey = self._ConvertComplexTypeToProxyId(k)
                convertedValue = self._ConvertComplexTypeToProxyId(v)
                convertedDict[convertedKey] = convertedValue
            return convertedDict
        elif isinstance(value, ObjectApiProxy):
            return value._objId #pylint: disable-msg=W0212
        return value
