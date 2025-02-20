# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sk-unix.proto

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
import fown_pb2 as fown__pb2
import sk_opts_pb2 as sk__opts__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sk-unix.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rsk-unix.proto\x1a\nopts.proto\x1a\nfown.proto\x1a\rsk-opts.proto\":\n\x10\x66ile_perms_entry\x12\x0c\n\x04mode\x18\x01 \x02(\r\x12\x0b\n\x03uid\x18\x02 \x02(\r\x12\x0b\n\x03gid\x18\x03 \x02(\r\"\xc2\x02\n\runix_sk_entry\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0b\n\x03ino\x18\x02 \x02(\r\x12\x0c\n\x04type\x18\x03 \x02(\r\x12\r\n\x05state\x18\x04 \x02(\r\x12\x14\n\x05\x66lags\x18\x05 \x02(\rB\x05\xd2?\x02\x08\x01\x12\x15\n\x06uflags\x18\x06 \x02(\rB\x05\xd2?\x02\x08\x01\x12\x0f\n\x07\x62\x61\x63klog\x18\x07 \x02(\r\x12\x0c\n\x04peer\x18\x08 \x02(\r\x12\x19\n\x04\x66own\x18\t \x02(\x0b\x32\x0b.fown_entry\x12\x1c\n\x04opts\x18\n \x02(\x0b\x32\x0e.sk_opts_entry\x12\x0c\n\x04name\x18\x0b \x02(\x0c\x12\x1e\n\x08shutdown\x18\x0c \x01(\x0e\x32\x0c.sk_shutdown\x12%\n\nfile_perms\x18\r \x01(\x0b\x32\x11.file_perms_entry\x12\x10\n\x08name_dir\x18\x0e \x01(\t\x12\x0f\n\x07\x64\x65leted\x18\x0f \x01(\x08')
  ,
  dependencies=[opts__pb2.DESCRIPTOR,fown__pb2.DESCRIPTOR,sk__opts__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_FILE_PERMS_ENTRY = _descriptor.Descriptor(
  name='file_perms_entry',
  full_name='file_perms_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='file_perms_entry.mode', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid', full_name='file_perms_entry.uid', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='file_perms_entry.gid', index=2,
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
  serialized_start=56,
  serialized_end=114,
)


_UNIX_SK_ENTRY = _descriptor.Descriptor(
  name='unix_sk_entry',
  full_name='unix_sk_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='unix_sk_entry.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ino', full_name='unix_sk_entry.ino', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='unix_sk_entry.type', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='unix_sk_entry.state', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='unix_sk_entry.flags', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='uflags', full_name='unix_sk_entry.uflags', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='backlog', full_name='unix_sk_entry.backlog', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='peer', full_name='unix_sk_entry.peer', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fown', full_name='unix_sk_entry.fown', index=8,
      number=9, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opts', full_name='unix_sk_entry.opts', index=9,
      number=10, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='unix_sk_entry.name', index=10,
      number=11, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shutdown', full_name='unix_sk_entry.shutdown', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_perms', full_name='unix_sk_entry.file_perms', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name_dir', full_name='unix_sk_entry.name_dir', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='unix_sk_entry.deleted', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=117,
  serialized_end=439,
)

_UNIX_SK_ENTRY.fields_by_name['fown'].message_type = fown__pb2._FOWN_ENTRY
_UNIX_SK_ENTRY.fields_by_name['opts'].message_type = sk__opts__pb2._SK_OPTS_ENTRY
_UNIX_SK_ENTRY.fields_by_name['shutdown'].enum_type = sk__opts__pb2._SK_SHUTDOWN
_UNIX_SK_ENTRY.fields_by_name['file_perms'].message_type = _FILE_PERMS_ENTRY
DESCRIPTOR.message_types_by_name['file_perms_entry'] = _FILE_PERMS_ENTRY
DESCRIPTOR.message_types_by_name['unix_sk_entry'] = _UNIX_SK_ENTRY

file_perms_entry = _reflection.GeneratedProtocolMessageType('file_perms_entry', (_message.Message,), dict(
  DESCRIPTOR = _FILE_PERMS_ENTRY,
  __module__ = 'sk_unix_pb2'
  # @@protoc_insertion_point(class_scope:file_perms_entry)
  ))
_sym_db.RegisterMessage(file_perms_entry)

unix_sk_entry = _reflection.GeneratedProtocolMessageType('unix_sk_entry', (_message.Message,), dict(
  DESCRIPTOR = _UNIX_SK_ENTRY,
  __module__ = 'sk_unix_pb2'
  # @@protoc_insertion_point(class_scope:unix_sk_entry)
  ))
_sym_db.RegisterMessage(unix_sk_entry)


_UNIX_SK_ENTRY.fields_by_name['flags'].has_options = True
_UNIX_SK_ENTRY.fields_by_name['flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_UNIX_SK_ENTRY.fields_by_name['uflags'].has_options = True
_UNIX_SK_ENTRY.fields_by_name['uflags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
# @@protoc_insertion_point(module_scope)
