__author__ = "RituRaj"


# This can be included in database to be directly edited in django admin
import subprocess
import tempfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser

from .constants import COMMANDS


class CodeAnalyzeApi(APIView):
    """Source code analyzer based on plain text and uploaded file 
    """

    def post(self, request, *args, **kwargs):
        try:
            payload = request.data
            print ("payload",payload)
            if payload['analysis_of'] == "file":
                f = request.FILES['file']
            language = payload['language']
            with tempfile.NamedTemporaryFile(suffix="."+language) as fp:
                if payload['analysis_of'] == 'file':
                    fp.write(f.read())
                else:
                    fp.write(payload['text'].encode())
                fp.flush()
                if language in COMMANDS.keys():
                    cmd = COMMANDS[language] + " " + fp.name
                    print("command", cmd)
                else:
                    cmd = "echo 'Language is not supported!'"
                output, error = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                ).communicate()
                try:
                    file_name = f.name
                except NameError:
                    file_name = "test." + language
                output, error = (output.decode().replace(fp.name, file_name),
                                 error.decode().replace(fp.name, file_name)
                                 )
            return Response({"output": output, "Error": error}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": e}, status=status.HTTP_400_BAD_REQUEST)
