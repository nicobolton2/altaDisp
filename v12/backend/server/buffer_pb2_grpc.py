# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import buffer_pb2 as buffer__pb2


class ServicerStub(object):
    """Servicio
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTemperature = channel.unary_unary(
                '/mypackage.Servicer/GetTemperature',
                request_serializer=buffer__pb2.Empty.SerializeToString,
                response_deserializer=buffer__pb2.Temperature.FromString,
                )
        self.GetUF = channel.unary_unary(
                '/mypackage.Servicer/GetUF',
                request_serializer=buffer__pb2.Empty.SerializeToString,
                response_deserializer=buffer__pb2.UF.FromString,
                )
        self.GetDollar = channel.unary_unary(
                '/mypackage.Servicer/GetDollar',
                request_serializer=buffer__pb2.Empty.SerializeToString,
                response_deserializer=buffer__pb2.Dollar.FromString,
                )


class ServicerServicer(object):
    """Servicio
    """

    def GetTemperature(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUF(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDollar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServicerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTemperature': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTemperature,
                    request_deserializer=buffer__pb2.Empty.FromString,
                    response_serializer=buffer__pb2.Temperature.SerializeToString,
            ),
            'GetUF': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUF,
                    request_deserializer=buffer__pb2.Empty.FromString,
                    response_serializer=buffer__pb2.UF.SerializeToString,
            ),
            'GetDollar': grpc.unary_unary_rpc_method_handler(
                    servicer.GetDollar,
                    request_deserializer=buffer__pb2.Empty.FromString,
                    response_serializer=buffer__pb2.Dollar.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mypackage.Servicer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Servicer(object):
    """Servicio
    """

    @staticmethod
    def GetTemperature(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Servicer/GetTemperature',
            buffer__pb2.Empty.SerializeToString,
            buffer__pb2.Temperature.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUF(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Servicer/GetUF',
            buffer__pb2.Empty.SerializeToString,
            buffer__pb2.UF.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetDollar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Servicer/GetDollar',
            buffer__pb2.Empty.SerializeToString,
            buffer__pb2.Dollar.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)