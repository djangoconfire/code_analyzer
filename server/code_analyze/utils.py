__author__ = "RituRaj"

""" Utility function """

def handle_uploaded_file(f):
    destination = open('private/%s'%f.name, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()