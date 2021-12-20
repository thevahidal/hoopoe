import datetime

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class Timestamp(ViewSet):
    def retrieve(self, request, *args, **kwargs):
        return Response(
            {"timestamp": datetime.datetime.now(), "version": request.version}
        )


class Echo(ViewSet):
    def retrieve(self, request, *args, **kwargs):
        return Response(
            {
                "timestamp": datetime.datetime.now(),
                "version": request.version,
                "method": request.method,
                "data": request.data,
                "headers": request.headers,
                "path": request.path,
                "query_params": request.query_params,
            }
        )
