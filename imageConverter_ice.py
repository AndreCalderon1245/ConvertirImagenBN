# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `imageConverter.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module ImageConverter
_M_ImageConverter = Ice.openModule('ImageConverter')
__name__ = 'ImageConverter'

_M_ImageConverter._t_Converter = IcePy.defineValue('::ImageConverter::Converter', Ice.Value, -1, (), False, True, None, ())

if 'ConverterPrx' not in _M_ImageConverter.__dict__:
    _M_ImageConverter.ConverterPrx = Ice.createTempClass()
    class ConverterPrx(Ice.ObjectPrx):

        def convertToBlackAndWhite(self, inputFile, outputFile, context=None):
            return _M_ImageConverter.Converter._op_convertToBlackAndWhite.invoke(self, ((inputFile, outputFile), context))

        def convertToBlackAndWhiteAsync(self, inputFile, outputFile, context=None):
            return _M_ImageConverter.Converter._op_convertToBlackAndWhite.invokeAsync(self, ((inputFile, outputFile), context))

        def begin_convertToBlackAndWhite(self, inputFile, outputFile, _response=None, _ex=None, _sent=None, context=None):
            return _M_ImageConverter.Converter._op_convertToBlackAndWhite.begin(self, ((inputFile, outputFile), _response, _ex, _sent, context))

        def end_convertToBlackAndWhite(self, _r):
            return _M_ImageConverter.Converter._op_convertToBlackAndWhite.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_ImageConverter.ConverterPrx.ice_checkedCast(proxy, '::ImageConverter::Converter', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_ImageConverter.ConverterPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::ImageConverter::Converter'
    _M_ImageConverter._t_ConverterPrx = IcePy.defineProxy('::ImageConverter::Converter', ConverterPrx)

    _M_ImageConverter.ConverterPrx = ConverterPrx
    del ConverterPrx

    _M_ImageConverter.Converter = Ice.createTempClass()
    class Converter(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::ImageConverter::Converter')

        def ice_id(self, current=None):
            return '::ImageConverter::Converter'

        @staticmethod
        def ice_staticId():
            return '::ImageConverter::Converter'

        def convertToBlackAndWhite(self, inputFile, outputFile, current=None):
            raise NotImplementedError("servant method 'convertToBlackAndWhite' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_ImageConverter._t_ConverterDisp)

        __repr__ = __str__

    _M_ImageConverter._t_ConverterDisp = IcePy.defineClass('::ImageConverter::Converter', Converter, (), None, ())
    Converter._ice_type = _M_ImageConverter._t_ConverterDisp

    Converter._op_convertToBlackAndWhite = IcePy.Operation('convertToBlackAndWhite', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0), ((), IcePy._t_string, False, 0)), (), None, ())

    _M_ImageConverter.Converter = Converter
    del Converter

# End of module ImageConverter