# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sk-inet.proto

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
  name='sk-inet.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\rsk-inet.proto\x1a\nopts.proto\x1a\nfown.proto\x1a\rsk-opts.proto\"!\n\rip_opts_entry\x12\x10\n\x08\x66reebind\x18\x01 \x01(\x08\"\xdb\x02\n\rinet_sk_entry\x12\n\n\x02id\x18\x01 \x02(\r\x12\x0b\n\x03ino\x18\x02 \x02(\r\x12\x0e\n\x06\x66\x61mily\x18\x03 \x02(\r\x12\x0c\n\x04type\x18\x04 \x02(\r\x12\r\n\x05proto\x18\x05 \x02(\r\x12\r\n\x05state\x18\x06 \x02(\r\x12\x10\n\x08src_port\x18\x07 \x02(\r\x12\x10\n\x08\x64st_port\x18\x08 \x02(\r\x12\x14\n\x05\x66lags\x18\t \x02(\rB\x05\xd2?\x02\x08\x01\x12\x0f\n\x07\x62\x61\x63klog\x18\n \x02(\r\x12\x17\n\x08src_addr\x18\x0b \x03(\rB\x05\xd2?\x02\x10\x01\x12\x17\n\x08\x64st_addr\x18\x0c \x03(\rB\x05\xd2?\x02\x10\x01\x12\x19\n\x04\x66own\x18\r \x02(\x0b\x32\x0b.fown_entry\x12\x1c\n\x04opts\x18\x0e \x02(\x0b\x32\x0e.sk_opts_entry\x12\x0e\n\x06v6only\x18\x0f \x01(\x08\x12\x1f\n\x07ip_opts\x18\x10 \x01(\x0b\x32\x0e.ip_opts_entry\x12\x0e\n\x06ifname\x18\x11 \x01(\t')
  ,
  dependencies=[opts__pb2.DESCRIPTOR,fown__pb2.DESCRIPTOR,sk__opts__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_IP_OPTS_ENTRY = _descriptor.Descriptor(
  name='ip_opts_entry',
  full_name='ip_opts_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='freebind', full_name='ip_opts_entry.freebind', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=56,
  serialized_end=89,
)


_INET_SK_ENTRY = _descriptor.Descriptor(
  name='inet_sk_entry',
  full_name='inet_sk_entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='inet_sk_entry.id', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ino', full_name='inet_sk_entry.ino', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family', full_name='inet_sk_entry.family', index=2,
      number=3, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='inet_sk_entry.type', index=3,
      number=4, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='proto', full_name='inet_sk_entry.proto', index=4,
      number=5, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='state', full_name='inet_sk_entry.state', index=5,
      number=6, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='src_port', full_name='inet_sk_entry.src_port', index=6,
      number=7, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dst_port', full_name='inet_sk_entry.dst_port', index=7,
      number=8, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flags', full_name='inet_sk_entry.flags', index=8,
      number=9, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))),
    _descriptor.FieldDescriptor(
      name='backlog', full_name='inet_sk_entry.backlog', index=9,
      number=10, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='src_addr', full_name='inet_sk_entry.src_addr', index=10,
      number=11, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='dst_addr', full_name='inet_sk_entry.dst_addr', index=11,
      number=12, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\020\001'))),
    _descriptor.FieldDescriptor(
      name='fown', full_name='inet_sk_entry.fown', index=12,
      number=13, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opts', full_name='inet_sk_entry.opts', index=13,
      number=14, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v6only', full_name='inet_sk_entry.v6only', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip_opts', full_name='inet_sk_entry.ip_opts', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ifname', full_name='inet_sk_entry.ifname', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=92,
  serialized_end=439,
)

_INET_SK_ENTRY.fields_by_name['fown'].message_type = fown__pb2._FOWN_ENTRY
_INET_SK_ENTRY.fields_by_name['opts'].message_type = sk__opts__pb2._SK_OPTS_ENTRY
_INET_SK_ENTRY.fields_by_name['ip_opts'].message_type = _IP_OPTS_ENTRY
DESCRIPTOR.message_types_by_name['ip_opts_entry'] = _IP_OPTS_ENTRY
DESCRIPTOR.message_types_by_name['inet_sk_entry'] = _INET_SK_ENTRY

ip_opts_entry = _reflection.GeneratedProtocolMessageType('ip_opts_entry', (_message.Message,), dict(
  DESCRIPTOR = _IP_OPTS_ENTRY,
  __module__ = 'sk_inet_pb2'
  # @@protoc_insertion_point(class_scope:ip_opts_entry)
  ))
_sym_db.RegisterMessage(ip_opts_entry)

inet_sk_entry = _reflection.GeneratedProtocolMessageType('inet_sk_entry', (_message.Message,), dict(
  DESCRIPTOR = _INET_SK_ENTRY,
  __module__ = 'sk_inet_pb2'
  # @@protoc_insertion_point(class_scope:inet_sk_entry)
  ))
_sym_db.RegisterMessage(inet_sk_entry)


_INET_SK_ENTRY.fields_by_name['flags'].has_options = True
_INET_SK_ENTRY.fields_by_name['flags']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\010\001'))
_INET_SK_ENTRY.fields_by_name['src_addr'].has_options = True
_INET_SK_ENTRY.fields_by_name['src_addr']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\020\001'))
_INET_SK_ENTRY.fields_by_name['dst_addr'].has_options = True
_INET_SK_ENTRY.fields_by_name['dst_addr']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\322?\002\020\001'))
# @@protoc_insertion_point(module_scope)
