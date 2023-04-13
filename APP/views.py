from rest_framework.views import APIView
from rest_framework.response import Response
from APP.serializers import *
from APP.models import *

# Create your views here.

# CLASS BAES VIEW --- APIVIEW
# FUNCTION BASED VIEW --- @apiview

# Views For Parent Model ('Family')
class familylist(APIView):
    def get(self,request):
        family_datas=FamilySerializer(family.objects.all(),many=True)
        return Response(family_datas.data)
    
    def post(self,request):
        family_datas=FamilySerializer(data=request.data)
        if family_datas.is_valid():
            family_datas.save()
            return Response({"Message":"New FAMILY added!!"})
        else:
            return Response(family_datas.errors)
        
    def put(self,request):
        data=request.data
        update_farmer=data['Farmer']
        family_datas=FamilySerializer(data=data)
        if family_datas.is_valid():
            family_datas.save()
            return Response({"Message":f"FAMILY {update_farmer} IN WHOLE UPDATED!!!!"})
        else:
            return Response(family_datas.errors)
        
    def patch(self,request):
        data=request.data
        update_farmer=data['Farmer']
        family_datas=FamilySerializer(data=data,partial=True)
        if family_datas.is_valid():
            family_datas.save()
            return Response({"Message":f"FAMILY {update_farmer} UPDATED!!!!"})
        else:
            return Response(family_datas.errors)
    
    def delete(self,request):
        data=request.data
        delete_farmer=data['Farmer']
        if delete_farmer!="*":
            obj=family.objects.get(Farmer=delete_farmer)
            obj.delete()
            return Response({"Message":f"FAMILY {delete_farmer} DELETED!!!!"})
        else:
            obj=family.objects.all()
            obj.delete()
            return Response({"Message":f"ALL FAMILIES ARE DELETED!!!!"})


# Views For Parent Model ('Family')

class childlist(APIView):
    def get(self,request):
        child_datas=ChildSerializer(child.objects.all(),many=True)
        return Response(child_datas.data)
    
    def post(self,request):
        child_datas=ChildSerializer(data=request.data)
        if child_datas.is_valid():
            child_datas.save()
            return Response({"Message":"New CHILD added!!"})
        else:
            return Response(child_datas.errors)
        
    def put(self,request):
        data=request.data
        update_child=data['child_name']
        child_datas=ChildSerializer(data=data)
        if child_datas.is_valid():
            child_datas.save()
            return Response({"Message":f"CHILD {update_child} IN WHOLE UPDATED!!!!"})
        else:
            return Response(child_datas.errors)
        
    def patch(self,request):
        data=request.data
        update_child=data['child_name']
        child_datas=ChildSerializer(data=data,partial=True)
        if child_datas.is_valid():
            child_datas.save()
            return Response({"Message":f"CHILD {update_child} UPDATED!!!!"})
        else:
            return Response(child_datas.errors)
        
    def delete(self,request):
        data=request.data
        delete_child=data['child_name']
        if delete_child!="*":
            obj=child.objects.get(Farmer=delete_child)
            obj.delete()
            return Response({"Message":f"CHILD {delete_child} DELETED!!!!"})
        else:
            obj=child.objects.all()
            obj.delete()
            return Response({"Message":f"ALL CHILDS ARE DELETED!!!!"})