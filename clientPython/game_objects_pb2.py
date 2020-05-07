# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game_objects.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game_objects.proto',
  package='endpoints.flunky.simulator',
  syntax='proto3',
  serialized_options=b'\n*de.flunkyteam.endpoints.projects.simulatorB\013GameObjectsP\001',
  serialized_pb=b'\n\x12game_objects.proto\x12\x1a\x65ndpoints.flunky.simulator\"\xd0\x02\n\tGameState\x12\x37\n\x0bplayerTeamA\x18\x01 \x03(\x0b\x32\".endpoints.flunky.simulator.Player\x12\x37\n\x0bplayerTeamB\x18\x02 \x03(\x0b\x32\".endpoints.flunky.simulator.Player\x12\x36\n\nspectators\x18\x03 \x03(\x0b\x32\".endpoints.flunky.simulator.Player\x12:\n\nruleConfig\x18\x08 \x01(\x0b\x32&.endpoints.flunky.simulator.RuleConfig\x12\x15\n\rrestingPeriod\x18\t \x01(\x08\x12\x16\n\x0ethrowingPlayer\x18\n \x01(\t\x12\x16\n\x0estrafbierTeamA\x18\x0b \x01(\x03\x12\x16\n\x0estrafbierTeamB\x18\x0c \x01(\x03\")\n\nRuleConfig\x12\x1b\n\x13restingPeriodLength\x18\x01 \x01(\x03\")\n\x06Player\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tabgegeben\x18\x02 \x01(\x08*|\n\x11\x45numThrowStrength\x12\x1a\n\x16UNKNOWN_THROW_STRENGTH\x10\x00\x12\x17\n\x13SOFT_THROW_STRENGTH\x10\x01\x12\x19\n\x15MEDIUM_THROW_STRENGTH\x10\x02\x12\x17\n\x13HARD_THROW_STRENGTH\x10\x03*W\n\tEnumTeams\x12\x11\n\rUNKNOWN_TEAMS\x10\x00\x12\x13\n\x0fSPECTATOR_TEAMS\x10\x01\x12\x10\n\x0cTEAM_A_TEAMS\x10\x02\x12\x10\n\x0cTEAM_B_TEAMS\x10\x03\x42;\n*de.flunkyteam.endpoints.projects.simulatorB\x0bGameObjectsP\x01\x62\x06proto3'
)

_ENUMTHROWSTRENGTH = _descriptor.EnumDescriptor(
  name='EnumThrowStrength',
  full_name='endpoints.flunky.simulator.EnumThrowStrength',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_THROW_STRENGTH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOFT_THROW_STRENGTH', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM_THROW_STRENGTH', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HARD_THROW_STRENGTH', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=475,
  serialized_end=599,
)
_sym_db.RegisterEnumDescriptor(_ENUMTHROWSTRENGTH)

EnumThrowStrength = enum_type_wrapper.EnumTypeWrapper(_ENUMTHROWSTRENGTH)
_ENUMTEAMS = _descriptor.EnumDescriptor(
  name='EnumTeams',
  full_name='endpoints.flunky.simulator.EnumTeams',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_TEAMS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SPECTATOR_TEAMS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEAM_A_TEAMS', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEAM_B_TEAMS', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=601,
  serialized_end=688,
)
_sym_db.RegisterEnumDescriptor(_ENUMTEAMS)

EnumTeams = enum_type_wrapper.EnumTypeWrapper(_ENUMTEAMS)
UNKNOWN_THROW_STRENGTH = 0
SOFT_THROW_STRENGTH = 1
MEDIUM_THROW_STRENGTH = 2
HARD_THROW_STRENGTH = 3
UNKNOWN_TEAMS = 0
SPECTATOR_TEAMS = 1
TEAM_A_TEAMS = 2
TEAM_B_TEAMS = 3



_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='endpoints.flunky.simulator.GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerTeamA', full_name='endpoints.flunky.simulator.GameState.playerTeamA', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='playerTeamB', full_name='endpoints.flunky.simulator.GameState.playerTeamB', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spectators', full_name='endpoints.flunky.simulator.GameState.spectators', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ruleConfig', full_name='endpoints.flunky.simulator.GameState.ruleConfig', index=3,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restingPeriod', full_name='endpoints.flunky.simulator.GameState.restingPeriod', index=4,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='throwingPlayer', full_name='endpoints.flunky.simulator.GameState.throwingPlayer', index=5,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strafbierTeamA', full_name='endpoints.flunky.simulator.GameState.strafbierTeamA', index=6,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strafbierTeamB', full_name='endpoints.flunky.simulator.GameState.strafbierTeamB', index=7,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=387,
)


_RULECONFIG = _descriptor.Descriptor(
  name='RuleConfig',
  full_name='endpoints.flunky.simulator.RuleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='restingPeriodLength', full_name='endpoints.flunky.simulator.RuleConfig.restingPeriodLength', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=389,
  serialized_end=430,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='endpoints.flunky.simulator.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='endpoints.flunky.simulator.Player.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abgegeben', full_name='endpoints.flunky.simulator.Player.abgegeben', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=432,
  serialized_end=473,
)

_GAMESTATE.fields_by_name['playerTeamA'].message_type = _PLAYER
_GAMESTATE.fields_by_name['playerTeamB'].message_type = _PLAYER
_GAMESTATE.fields_by_name['spectators'].message_type = _PLAYER
_GAMESTATE.fields_by_name['ruleConfig'].message_type = _RULECONFIG
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
DESCRIPTOR.message_types_by_name['RuleConfig'] = _RULECONFIG
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.enum_types_by_name['EnumThrowStrength'] = _ENUMTHROWSTRENGTH
DESCRIPTOR.enum_types_by_name['EnumTeams'] = _ENUMTEAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'game_objects_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.GameState)
  })
_sym_db.RegisterMessage(GameState)

RuleConfig = _reflection.GeneratedProtocolMessageType('RuleConfig', (_message.Message,), {
  'DESCRIPTOR' : _RULECONFIG,
  '__module__' : 'game_objects_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.RuleConfig)
  })
_sym_db.RegisterMessage(RuleConfig)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'game_objects_pb2'
  # @@protoc_insertion_point(class_scope:endpoints.flunky.simulator.Player)
  })
_sym_db.RegisterMessage(Player)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
