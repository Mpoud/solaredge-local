# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: maintenance.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='maintenance.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11maintenance.proto\"\xe9\x07\n\x0bMaintenance\x12-\n\x0b\x64iagnostics\x18\x06 \x01(\x0b\x32\x18.Maintenance.Diagnostics\x1ax\n\x0bTemperature\x12\r\n\x05value\x18\x01 \x01(\x05\x12-\n\x05units\x18\x02 \x01(\x0b\x32\x1e.Maintenance.Temperature.Units\x1a+\n\x05Units\x12\x0f\n\x07\x63\x65lsius\x18\x01 \x01(\x08\x12\x11\n\tfarenheit\x18\x02 \x01(\x08\x1a\xb0\x06\n\x0b\x44iagnostics\x12\x35\n\tinverters\x18\x01 \x01(\x0b\x32\".Maintenance.Diagnostics.Inverters\x1a\xe9\x05\n\tInverters\x12\x35\n\x04left\x18\x01 \x01(\x0b\x32\'.Maintenance.Diagnostics.Inverters.Unit\x12\x38\n\x07primary\x18\x02 \x01(\x0b\x32\'.Maintenance.Diagnostics.Inverters.Unit\x12\x36\n\x05right\x18\x03 \x01(\x0b\x32\'.Maintenance.Diagnostics.Inverters.Unit\x1a\xb2\x04\n\x04Unit\x12\r\n\x05invSn\x18\x01 \x01(\t\x12\x44\n\toptimizer\x18\x02 \x03(\x0b\x32\x31.Maintenance.Diagnostics.Inverters.Unit.Optimizer\x12R\n\x10optimizersStatus\x18\x04 \x01(\x0b\x32\x38.Maintenance.Diagnostics.Inverters.Unit.OptimizersStatus\x1a\x31\n\x10OptimizersStatus\x12\r\n\x05total\x18\x01 \x01(\x05\x12\x0e\n\x06online\x18\x02 \x01(\x05\x1a\xcd\x02\n\tOptimizer\x12\x14\n\x0cserialNumber\x18\x01 \x01(\t\x12\x0e\n\x06online\x18\x02 \x01(\x08\x12J\n\nlastReport\x18\x03 \x01(\x0b\x32\x36.Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date\x12\x0e\n\x06\x65nergy\x18\x04 \x01(\x02\x12\x0f\n\x07outputV\x18\x05 \x01(\x05\x12\x0e\n\x06inputV\x18\x06 \x01(\x05\x12\x0e\n\x06inputC\x18\x07 \x01(\x05\x12-\n\x0btemperature\x18\x08 \x01(\x0b\x32\x18.Maintenance.Temperature\x1a^\n\x04\x44\x61te\x12\x0c\n\x04year\x18\x01 \x01(\x05\x12\r\n\x05month\x18\x02 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\x05\x12\x0c\n\x04hour\x18\x04 \x01(\x05\x12\x0e\n\x06minute\x18\x05 \x01(\x05\x12\x0e\n\x06second\x18\x06 \x01(\x05\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAINTENANCE_TEMPERATURE_UNITS = _descriptor.Descriptor(
  name='Units',
  full_name='Maintenance.Temperature.Units',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='celsius', full_name='Maintenance.Temperature.Units.celsius', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='farenheit', full_name='Maintenance.Temperature.Units.farenheit', index=1,
      number=2, type=8, cpp_type=7, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=204,
)

_MAINTENANCE_TEMPERATURE = _descriptor.Descriptor(
  name='Temperature',
  full_name='Maintenance.Temperature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Maintenance.Temperature.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='units', full_name='Maintenance.Temperature.units', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCE_TEMPERATURE_UNITS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=84,
  serialized_end=204,
)

_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZERSSTATUS = _descriptor.Descriptor(
  name='OptimizersStatus',
  full_name='Maintenance.Diagnostics.Inverters.Unit.OptimizersStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='Maintenance.Diagnostics.Inverters.Unit.OptimizersStatus.total', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online', full_name='Maintenance.Diagnostics.Inverters.Unit.OptimizersStatus.online', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=638,
  serialized_end=687,
)

_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date.year', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='month', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date.month', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date.day', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hour', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date.hour', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minute', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date.minute', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='second', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date.second', index=5,
      number=6, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=929,
  serialized_end=1023,
)

_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER = _descriptor.Descriptor(
  name='Optimizer',
  full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='serialNumber', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.serialNumber', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='online', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.online', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastReport', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.lastReport', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='energy', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.energy', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputV', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.outputV', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputV', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.inputV', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inputC', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.inputC', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='temperature', full_name='Maintenance.Diagnostics.Inverters.Unit.Optimizer.temperature', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER_DATE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=690,
  serialized_end=1023,
)

_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT = _descriptor.Descriptor(
  name='Unit',
  full_name='Maintenance.Diagnostics.Inverters.Unit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invSn', full_name='Maintenance.Diagnostics.Inverters.Unit.invSn', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='Maintenance.Diagnostics.Inverters.Unit.optimizer', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='optimizersStatus', full_name='Maintenance.Diagnostics.Inverters.Unit.optimizersStatus', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZERSSTATUS, _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=1023,
)

_MAINTENANCE_DIAGNOSTICS_INVERTERS = _descriptor.Descriptor(
  name='Inverters',
  full_name='Maintenance.Diagnostics.Inverters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='left', full_name='Maintenance.Diagnostics.Inverters.left', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primary', full_name='Maintenance.Diagnostics.Inverters.primary', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='right', full_name='Maintenance.Diagnostics.Inverters.right', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=1023,
)

_MAINTENANCE_DIAGNOSTICS = _descriptor.Descriptor(
  name='Diagnostics',
  full_name='Maintenance.Diagnostics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='inverters', full_name='Maintenance.Diagnostics.inverters', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCE_DIAGNOSTICS_INVERTERS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=207,
  serialized_end=1023,
)

_MAINTENANCE = _descriptor.Descriptor(
  name='Maintenance',
  full_name='Maintenance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='diagnostics', full_name='Maintenance.diagnostics', index=0,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_MAINTENANCE_TEMPERATURE, _MAINTENANCE_DIAGNOSTICS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=1023,
)

_MAINTENANCE_TEMPERATURE_UNITS.containing_type = _MAINTENANCE_TEMPERATURE
_MAINTENANCE_TEMPERATURE.fields_by_name['units'].message_type = _MAINTENANCE_TEMPERATURE_UNITS
_MAINTENANCE_TEMPERATURE.containing_type = _MAINTENANCE
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZERSSTATUS.containing_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER_DATE.containing_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER.fields_by_name['lastReport'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER_DATE
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER.fields_by_name['temperature'].message_type = _MAINTENANCE_TEMPERATURE
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER.containing_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT.fields_by_name['optimizer'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT.fields_by_name['optimizersStatus'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZERSSTATUS
_MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT.containing_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS
_MAINTENANCE_DIAGNOSTICS_INVERTERS.fields_by_name['left'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT
_MAINTENANCE_DIAGNOSTICS_INVERTERS.fields_by_name['primary'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT
_MAINTENANCE_DIAGNOSTICS_INVERTERS.fields_by_name['right'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT
_MAINTENANCE_DIAGNOSTICS_INVERTERS.containing_type = _MAINTENANCE_DIAGNOSTICS
_MAINTENANCE_DIAGNOSTICS.fields_by_name['inverters'].message_type = _MAINTENANCE_DIAGNOSTICS_INVERTERS
_MAINTENANCE_DIAGNOSTICS.containing_type = _MAINTENANCE
_MAINTENANCE.fields_by_name['diagnostics'].message_type = _MAINTENANCE_DIAGNOSTICS
DESCRIPTOR.message_types_by_name['Maintenance'] = _MAINTENANCE

Maintenance = _reflection.GeneratedProtocolMessageType('Maintenance', (_message.Message,), dict(

  Temperature = _reflection.GeneratedProtocolMessageType('Temperature', (_message.Message,), dict(

    Units = _reflection.GeneratedProtocolMessageType('Units', (_message.Message,), dict(
      DESCRIPTOR = _MAINTENANCE_TEMPERATURE_UNITS,
      __module__ = 'maintenance_pb2'
      # @@protoc_insertion_point(class_scope:Maintenance.Temperature.Units)
      ))
    ,
    DESCRIPTOR = _MAINTENANCE_TEMPERATURE,
    __module__ = 'maintenance_pb2'
    # @@protoc_insertion_point(class_scope:Maintenance.Temperature)
    ))
  ,

  Diagnostics = _reflection.GeneratedProtocolMessageType('Diagnostics', (_message.Message,), dict(

    Inverters = _reflection.GeneratedProtocolMessageType('Inverters', (_message.Message,), dict(

      Unit = _reflection.GeneratedProtocolMessageType('Unit', (_message.Message,), dict(

        OptimizersStatus = _reflection.GeneratedProtocolMessageType('OptimizersStatus', (_message.Message,), dict(
          DESCRIPTOR = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZERSSTATUS,
          __module__ = 'maintenance_pb2'
          # @@protoc_insertion_point(class_scope:Maintenance.Diagnostics.Inverters.Unit.OptimizersStatus)
          ))
        ,

        Optimizer = _reflection.GeneratedProtocolMessageType('Optimizer', (_message.Message,), dict(

          Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), dict(
            DESCRIPTOR = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER_DATE,
            __module__ = 'maintenance_pb2'
            # @@protoc_insertion_point(class_scope:Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date)
            ))
          ,
          DESCRIPTOR = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT_OPTIMIZER,
          __module__ = 'maintenance_pb2'
          # @@protoc_insertion_point(class_scope:Maintenance.Diagnostics.Inverters.Unit.Optimizer)
          ))
        ,
        DESCRIPTOR = _MAINTENANCE_DIAGNOSTICS_INVERTERS_UNIT,
        __module__ = 'maintenance_pb2'
        # @@protoc_insertion_point(class_scope:Maintenance.Diagnostics.Inverters.Unit)
        ))
      ,
      DESCRIPTOR = _MAINTENANCE_DIAGNOSTICS_INVERTERS,
      __module__ = 'maintenance_pb2'
      # @@protoc_insertion_point(class_scope:Maintenance.Diagnostics.Inverters)
      ))
    ,
    DESCRIPTOR = _MAINTENANCE_DIAGNOSTICS,
    __module__ = 'maintenance_pb2'
    # @@protoc_insertion_point(class_scope:Maintenance.Diagnostics)
    ))
  ,
  DESCRIPTOR = _MAINTENANCE,
  __module__ = 'maintenance_pb2'
  # @@protoc_insertion_point(class_scope:Maintenance)
  ))
_sym_db.RegisterMessage(Maintenance)
_sym_db.RegisterMessage(Maintenance.Temperature)
_sym_db.RegisterMessage(Maintenance.Temperature.Units)
_sym_db.RegisterMessage(Maintenance.Diagnostics)
_sym_db.RegisterMessage(Maintenance.Diagnostics.Inverters)
_sym_db.RegisterMessage(Maintenance.Diagnostics.Inverters.Unit)
_sym_db.RegisterMessage(Maintenance.Diagnostics.Inverters.Unit.OptimizersStatus)
_sym_db.RegisterMessage(Maintenance.Diagnostics.Inverters.Unit.Optimizer)
_sym_db.RegisterMessage(Maintenance.Diagnostics.Inverters.Unit.Optimizer.Date)


# @@protoc_insertion_point(module_scope)
