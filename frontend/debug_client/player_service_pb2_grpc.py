# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import player_service_pb2 as player__service__pb2


class PlayerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterPlayer = channel.unary_unary(
        '/endpoints.flunky.simulator.PlayerService/RegisterPlayer',
        request_serializer=player__service__pb2.RegisterPlayerReq.SerializeToString,
        response_deserializer=player__service__pb2.RegisterPlayerResp.FromString,
        )
    self.KickPlayer = channel.unary_unary(
        '/endpoints.flunky.simulator.PlayerService/KickPlayer',
        request_serializer=player__service__pb2.KickPlayerReq.SerializeToString,
        response_deserializer=player__service__pb2.KickPlayerResp.FromString,
        )
    self.SwitchTeam = channel.unary_unary(
        '/endpoints.flunky.simulator.PlayerService/SwitchTeam',
        request_serializer=player__service__pb2.SwitchTeamReq.SerializeToString,
        response_deserializer=player__service__pb2.SwitchTeamResp.FromString,
        )
    self.ShuffleTeams = channel.unary_unary(
        '/endpoints.flunky.simulator.PlayerService/ShuffleTeams',
        request_serializer=player__service__pb2.ShuffleTeamsReq.SerializeToString,
        response_deserializer=player__service__pb2.ShuffleTeamsResp.FromString,
        )
    self.StreamAllPlayers = channel.unary_stream(
        '/endpoints.flunky.simulator.PlayerService/StreamAllPlayers',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=player__service__pb2.PlayerListResp.FromString,
        )
    self.StreamTeamAPlayers = channel.unary_stream(
        '/endpoints.flunky.simulator.PlayerService/StreamTeamAPlayers',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=player__service__pb2.PlayerListResp.FromString,
        )
    self.StreamTeamBPlayers = channel.unary_stream(
        '/endpoints.flunky.simulator.PlayerService/StreamTeamBPlayers',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=player__service__pb2.PlayerListResp.FromString,
        )
    self.StreamSpectators = channel.unary_stream(
        '/endpoints.flunky.simulator.PlayerService/StreamSpectators',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=player__service__pb2.PlayerListResp.FromString,
        )


class PlayerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def RegisterPlayer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def KickPlayer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SwitchTeam(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ShuffleTeams(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamAllPlayers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamTeamAPlayers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamTeamBPlayers(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StreamSpectators(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_PlayerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterPlayer': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterPlayer,
          request_deserializer=player__service__pb2.RegisterPlayerReq.FromString,
          response_serializer=player__service__pb2.RegisterPlayerResp.SerializeToString,
      ),
      'KickPlayer': grpc.unary_unary_rpc_method_handler(
          servicer.KickPlayer,
          request_deserializer=player__service__pb2.KickPlayerReq.FromString,
          response_serializer=player__service__pb2.KickPlayerResp.SerializeToString,
      ),
      'SwitchTeam': grpc.unary_unary_rpc_method_handler(
          servicer.SwitchTeam,
          request_deserializer=player__service__pb2.SwitchTeamReq.FromString,
          response_serializer=player__service__pb2.SwitchTeamResp.SerializeToString,
      ),
      'ShuffleTeams': grpc.unary_unary_rpc_method_handler(
          servicer.ShuffleTeams,
          request_deserializer=player__service__pb2.ShuffleTeamsReq.FromString,
          response_serializer=player__service__pb2.ShuffleTeamsResp.SerializeToString,
      ),
      'StreamAllPlayers': grpc.unary_stream_rpc_method_handler(
          servicer.StreamAllPlayers,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=player__service__pb2.PlayerListResp.SerializeToString,
      ),
      'StreamTeamAPlayers': grpc.unary_stream_rpc_method_handler(
          servicer.StreamTeamAPlayers,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=player__service__pb2.PlayerListResp.SerializeToString,
      ),
      'StreamTeamBPlayers': grpc.unary_stream_rpc_method_handler(
          servicer.StreamTeamBPlayers,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=player__service__pb2.PlayerListResp.SerializeToString,
      ),
      'StreamSpectators': grpc.unary_stream_rpc_method_handler(
          servicer.StreamSpectators,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=player__service__pb2.PlayerListResp.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'endpoints.flunky.simulator.PlayerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
