# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2019-05-28 10:03

from capnpy import ptr as _ptr
from capnpy.struct_ import Struct as _Struct
from capnpy.struct_ import check_tag as _check_tag
from capnpy.struct_ import undefined as _undefined
from capnpy.enum import enum as _enum, fill_enum as _fill_enum
from capnpy.enum import BaseEnum as _BaseEnum
from capnpy.type import Types as _Types
from capnpy.segment.builder import SegmentBuilder as _SegmentBuilder
from capnpy.list import List as _List
from capnpy.list import PrimitiveItemType as _PrimitiveItemType
from capnpy.list import BoolItemType as _BoolItemType
from capnpy.list import TextItemType as _TextItemType
from capnpy.list import StructItemType as _StructItemType
from capnpy.list import EnumItemType as _EnumItemType
from capnpy.list import VoidItemType as _VoidItemType
from capnpy.list import ListItemType as _ListItemType
from capnpy.anypointer import AnyPointer as _AnyPointer
from capnpy.util import text_repr as _text_repr
from capnpy.util import float32_repr as _float32_repr
from capnpy.util import float64_repr as _float64_repr
from capnpy.util import extend_module_maybe as _extend_module_maybe
from capnpy.util import check_version as _check_version
__capnpy_version__ = '0.5.4.dev12+ngbc554c5.d20190405'
# schema compiled with --no-version-check, skipping the call to _check_version

#### FORWARD DECLARATIONS ####

class options(object):
    __id__ = 13670177934128632979
    targets_file = True
    targets_const = False
    targets_enum = False
    targets_enumerant = False
    targets_struct = True
    targets_field = False
    targets_union = False
    targets_group = False
    targets_interface = False
    targets_method = False
    targets_param = False
    targets_annotation = False
class key(object):
    __id__ = 14658097673689429382
    targets_file = False
    targets_const = False
    targets_enum = False
    targets_enumerant = False
    targets_struct = True
    targets_field = True
    targets_union = False
    targets_group = True
    targets_interface = False
    targets_method = False
    targets_param = False
    targets_annotation = False
class nullable(object):
    __id__ = 11296117080722892765
    targets_file = False
    targets_const = False
    targets_enum = False
    targets_enumerant = False
    targets_struct = False
    targets_field = False
    targets_union = False
    targets_group = True
    targets_interface = False
    targets_method = False
    targets_param = False
    targets_annotation = False
class BoolOption(_BaseEnum):
    __members__ = ('false', 'true', 'notset',)
    @staticmethod
    def _new(x):
        return BoolOption(x)
_fill_enum(BoolOption)
_BoolOption_list_item_type = _EnumItemType(BoolOption)

class Options(_Struct): pass
Options.__name__ = 'Options'

class group(object):
    __id__ = 12694526166034528397
    targets_file = False
    targets_const = False
    targets_enum = False
    targets_enumerant = False
    targets_struct = False
    targets_field = True
    targets_union = False
    targets_group = False
    targets_interface = False
    targets_method = False
    targets_param = False
    targets_annotation = False

#### DEFINITIONS ####

@Options.__extend__
class Options(_Struct):
    __static_data_size__ = 1
    __static_ptrs_size__ = 0
    
    
    @property
    def convert_case(self):
        # no union check
        value = self._read_data_int16(0)
        if 2 != 0:
            value = (value ^ 2)
        return BoolOption._new(value)
    
    @staticmethod
    def __new(convert_case=2):
        builder = _SegmentBuilder()
        pos = builder.allocate(8)
        convert_case ^= 2
        builder.write_int16(pos + 0, convert_case)
        return builder.as_string()
    
    def __init__(self, convert_case=2):
        _buf = Options.__new(convert_case)
        self._init_from_buffer(_buf, 0, 1, 0)
    
    def shortrepr(self):
        parts = []
        parts.append("convert_case = %s" % self.convert_case)
        return "(%s)" % ", ".join(parts)

_Options_list_item_type = _StructItemType(Options)


_extend_module_maybe(globals(), modname=__name__)