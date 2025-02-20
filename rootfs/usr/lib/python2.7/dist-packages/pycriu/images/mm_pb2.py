# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mm.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import opts_pb2 as opts__pb2
import vma_pb2 as vma__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mm.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x08mm.proto\x1a\nopts.proto\x1a\tvma.proto\">\n\x0e\x61io_ring_entry\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x0e\n\x06nr_req\x18\x02 \x02(\r\x12\x10\n\x08ring_len\x18\x03 \x02(\r\"\xb8\x03\n\x08mm_entry\x12\x1c\n\rmm_start_code\x18\x01 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1a\n\x0bmm_end_code\x18\x02 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1c\n\rmm_start_data\x18\x03 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1a\n\x0bmm_end_data\x18\x04 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1d\n\x0emm_start_stack\x18\x05 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1b\n\x0cmm_start_brk\x18\x06 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x15\n\x06mm_brk\x18\x07 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1b\n\x0cmm_arg_start\x18\x08 \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x19\n\nmm_arg_end\x18\t \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x1b\n\x0cmm_env_start\x18\n \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x19\n\nmm_env_end\x18\x0b \x02(\x04\x42\x05\xd2?\x02\x08\x01\x12\x13\n\x0b\x65xe_file_id\x18\x0c \x02(\r\x12\x15\n\rmm_saved_auxv\x18\r \x03(\x04\x12\x18\n\x04vmas\x18\x0e \x03(\x0b\x32\n.vma_entry\x12\x10\n\x08\x64umpable\x18\x0f \x01(\x05\x12\x1d\n\x04\x61ios\x18\x10 \x03(\x0b\x32\x0f.aio_ring_entry')
  ,
  dependencies=[opts__pb2.DESCRIPTOR,vma__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AIO_RING_ENTRY = _descriptor.Descriptor(
  name='aio_ring_entry',
  full_name='aio_ring_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='aio_ring_entry.id', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nr_req', full_name='aio_ring_entry.nr_req', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ring_len', full_name='aio_ring_entry.ring_len', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=97,
)


_MM_ENTRY = _descriptor.Descriptor(
  name='mm_entry',
  full_name='mm_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mm_start_code', full_name='mm_entry.mm_start_code', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_end_code', full_name='mm_entry.mm_end_code', index=1,
      number=2, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_start_data', full_name='mm_entry.mm_start_data', index=2,
      number=3, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_end_data', full_name='mm_entry.mm_end_data', index=3,
      number=4, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_start_stack', full_name='mm_entry.mm_start_stack', index=4,
      number=5, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_start_brk', full_name='mm_entry.mm_start_brk', index=5,
      number=6, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_brk', full_name='mm_entry.mm_brk', index=6,
      number=7, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_arg_start', full_name='mm_entry.mm_arg_start', index=7,
      number=8, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_arg_end', full_name='mm_entry.mm_arg_end', index=8,
      number=9, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_env_start', full_name='mm_entry.mm_env_start', index=9,
      number=10, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='mm_env_end', full_name='mm_entry.mm_env_end', index=10,
      number=11, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='exe_file_id', full_name='mm_entry.exe_file_id', index=11,
      number=12, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mm_saved_auxv', full_name='mm_entry.mm_saved_auxv', index=12,
      number=13, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vmas', full_name='mm_entry.vmas', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dumpable', full_name='mm_entry.dumpable', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aios', full_name='mm_entry.aios', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=540,
)

_MM_ENTRY.fields_by_name['vmas'].message_type = vma__pb2._VMA_ENTRY
_MM_ENTRY.fields_by_name['aios'].message_type = _AIO_RING_ENTRY
DESCRIPTOR.message_types_by_name['aio_ring_entry'] = _AIO_RING_ENTRY
DESCRIPTOR.message_types_by_name['mm_entry'] = _MM_ENTRY

aio_ring_entry = _reflection.GeneratedProtocolMessageType('aio_ring_entry', (_message.Message,), dict(
  DESCRIPTOR = _AIO_RING_ENTRY,
  __module__ = 'mm_pb2'
  # @@protoc_insertion_point(class_scope:aio_ring_entry)
  ))
_sym_db.RegisterMessage(aio_ring_entry)

mm_entry = _reflection.GeneratedProtocolMessageType('mm_entry', (_message.Message,), dict(
  DESCRIPTOR = _MM_ENTRY,
  __module__ = 'mm_pb2'
  # @@protoc_insertion_point(class_scope:mm_entry)
  ))
_sym_db.RegisterMessage(mm_entry)


_MM_ENTRY.fields_by_name['mm_start_code'].has_options = True
_MM_ENTRY.fields_by_name['mm_start_code']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_end_code'].has_options = True
_MM_ENTRY.fields_by_name['mm_end_code']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_start_data'].has_options = True
_MM_ENTRY.fields_by_name['mm_start_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_end_data'].has_options = True
_MM_ENTRY.fields_by_name['mm_end_data']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_start_stack'].has_options = True
_MM_ENTRY.fields_by_name['mm_start_stack']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_start_brk'].has_options = True
_MM_ENTRY.fields_by_name['mm_start_brk']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_brk'].has_options = True
_MM_ENTRY.fields_by_name['mm_brk']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_arg_start'].has_options = True
_MM_ENTRY.fields_by_name['mm_arg_start']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_arg_end'].has_options = True
_MM_ENTRY.fields_by_name['mm_arg_end']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_env_start'].has_options = True
_MM_ENTRY.fields_by_name['mm_env_start']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_MM_ENTRY.fields_by_name['mm_env_end'].has_options = True
_MM_ENTRY.fields_by_name['mm_env_end']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
# @@protoc_insertion_point(module_scope)
