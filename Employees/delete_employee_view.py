from django.contrib.auth.models import User
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from RevenueCosts.models import Member

@permission_classes((permissions.AllowAny,))
class EmployeeDeleteView(APIView):
    queryset = User.objects.all() 

    def delete(self, request, id, format=None):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            raise Http404
        
        Member.objects.filter(user_id=user.id).delete()
        
        try:
            profile = user.profile
            profile.obrisan = True
            profile.save()
        except user.profile.DoesNotExist:
            pass
       
        #user.delete()
        
        return Response({'success': 'Employee deleted!'}, status=status.HTTP_204_NO_CONTENT)
