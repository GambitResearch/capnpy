# THIS FILE HAS BEEN GENERATED AUTOMATICALLY BY capnpy
# do not edit by hand
# generated on 2019-04-04 17:53

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
__capnpy_version__ = '0.5.4.dev7+ng2ca514d.d20190404'
# schema compiled with --no-version-check, skipping the call to _check_version

#### FORWARD DECLARATIONS ####

class group(object):
    __capnpy_id__ = 0xb02c044a1e63b88d
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
class nullable(object):
    __capnpy_id__ = 0x9cc3dea2b1b5e7dd
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
class key(object):
    __capnpy_id__ = 0xcb6c062c1b3cf586
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

#### DEFINITIONS ####


_extend_module_maybe(globals(), modname=__name__)