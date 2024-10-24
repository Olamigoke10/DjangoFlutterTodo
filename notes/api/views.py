from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerailizer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/notes/",
            "method": "/GET/",
            "body": None,
            "description": "Returns an array of notes"
        },
        {
            "Endpoint": "/notes/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single note object"
        },
        {
            "Endpoint": "/notes/",
            "method": "GET",
            "body": None,
            "description": "Returns an array of notes"
        },
        
        {
            "Endpoint": "/notes/create/",
            "method": "POST",
            "body": {"body": ""},
            "description": "Creates new notes sent in post request"
        }, 
        
        {
            "Endpoint": "/notes/update/",
            "method": "PUT",
            "body": {"body": ""},
            "description": "Creates an existing note with data sent in"
        }, 
        
        {
            "Endpoint": "/notes/id/delete",
            "method": "DELETE",
            "body": None,
            "description": "Deletes and exiting note"
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerailizer(notes, many=True)
    return Response(serializer.data)