__author__ = "RituRaj"

#python imports 
import subprocess
import tempfile
import os

# rest framework imports
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser, FileUploadParser

# local imports
from .constants import (
    COMMANDS, 
    EXTENSION_MAP,
)
from .utils import handle_uploaded_file


def get_extension(filename) :
    """
        returns the extension (text after last period), or 'no_extension' if no period is
        found (or is last char).

        @param file: uploaded file     
    """
    index = filename.rfind('.')
    if index == -1 :
        return None
    elif index == len(filename) - 1:
        # if last char
        return None
    else :
        extension = filename[index:]
        return extension


class CodeAnalyzeApi(APIView):
    """Source code analyzer based on plain text and uploaded file 
    """

    def post(self, request, *args, **kwargs):
        try:
            payload = request.data
            print ("payload",payload)
            if payload['language'] == "undefined":
                if payload['analysis_of'] == "file":
                    f = request.FILES.getlist('file')[0]
                    uploaded_files = []
                    handle_uploaded_file(f)
                    file_path = "private/" + f.name
                    filename = os.path.basename(file_path)
                    extension = get_extension(filename)
                    if extension in EXTENSION_MAP:
                        language = EXTENSION_MAP[extension]
            else:
                language = payload['language']

            with tempfile.NamedTemporaryFile(suffix="."+language) as fp:
                if payload['analysis_of'] == 'file':
                    text = f.read()
                else:
                    text = payload['text'].encode()
                fp.write(text)
                fp.flush()
                if language in COMMANDS.keys():
                    cmd = COMMANDS[language] + " " + fp.name
                else:
                    cmd = "echo 'Language is not supported!'"
                out, error = subprocess.Popen(
                    cmd,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    shell=True
                ).communicate()
                try:
                    file_name = f.name
                except NameError:
                    file_name = "test." + language
                
                out = out.decode() + "\n" + error.decode()
                out = out.replace(fp.name, file_name)

            return Response({"output": out},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error": e}, status=status.HTTP_400_BAD_REQUEST)

