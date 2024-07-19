from rest_framework.views import APIView
from rest_framework.response import Response
from APP.serializers import *
from APP.models import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics


# CLASS BAES VIEW --- APIVIEW (APIViewset , ModelViewset (along with Listviewset for nested search))
# FUNCTION BASED VIEW --- @apiview

# Writing Listview for Normal view

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
            obj=child.objects.get(child_name=delete_child)
            obj.delete()
            return Response({"Message":f"CHILD {delete_child} DELETED!!!!"})
        else:
            obj=child.objects.all()
            obj.delete()
            return Response({"Message":f"ALL CHILDS ARE DELETED!!!!"})
        

class cowlist(APIView):
    def get(self,request):
        cow_datas=CowSerializer(cow.objects.all(),many=True)
        return Response(cow_datas.data)
    
    def post(self,request):
        cow_datas=CowSerializer(data=request.data)
        if cow_datas.is_valid():
            cow_datas.save()
            return Response({"Message":"New COW added!!"})
        else:
            return Response(cow_datas.errors)
        
    def put(self,request):
        data=request.data
        update_cow=data['cow_name']
        cow_datas=CowSerializer(data=data)
        if cow_datas.is_valid():
            cow_datas.save()
            return Response({"Message":f"CHILD {update_cow} IN WHOLE UPDATED!!!!"})
        else:
            return Response(cow_datas.errors)
        
    def patch(self,request):
        data=request.data
        update_cow=data['cow_name']
        cow_datas=CowSerializer(data=data,partial=True)
        if cow_datas.is_valid():
            cow_datas.save()
            return Response({"Message":f"CHILD {update_cow} UPDATED!!!!"})
        else:
            return Response(cow_datas.errors)
        
    def delete(self,request):
        data=request.data
        delete_cow=data['cow_name']
        if delete_cow!="*":
            obj=cow.objects.get(cow_name=delete_cow)
            obj.delete()
            return Response({"Message":f"COW {delete_cow} DELETED!!!!"})
        else:
            obj=cow.objects.all()
            obj.delete()
            return Response({"Message":f"ALL COWS ARE DELETED!!!!"})
        

class sheaplist(APIView):
    def get(self,request):
        sheap_datas=SheapSerializer(sheap.objects.all(),many=True)
        return Response(sheap_datas.data)
    
    def post(self,request):
        sheap_datas=SheapSerializer(data=request.data)
        if sheap_datas.is_valid():
            sheap_datas.save()
            return Response({"Message":"New SHEAP added!!"})
        else:
            return Response(sheap_datas.errors)
        
    def put(self,request):
        data=request.data
        update_sheap=data['cow_name']
        sheap_datas=SheapSerializer(data=data)
        if sheap_datas.is_valid():
            sheap_datas.save()
            return Response({"Message":f"SHEAP {update_sheap} IN WHOLE UPDATED!!!!"})
        else:
            return Response(sheap_datas.errors)
        
    def patch(self,request):
        data=request.data
        update_sheap=data['sheap_name']
        sheap_datas=SheapSerializer(data=data,partial=True)
        if sheap_datas.is_valid():
            sheap_datas.save()
            return Response({"Message":f"SHEAP {update_sheap} UPDATED!!!!"})
        else:
            return Response(sheap_datas.errors)
        
    def delete(self,request):
        data=request.data
        delete_sheap=data['sheap_name']
        if delete_sheap!="*":
            obj=sheap.objects.get(sheap_name=delete_sheap)
            obj.delete()
            return Response({"Message":f"SHEAPS {delete_sheap} DELETED!!!!"})
        else:
            obj=sheap.objects.all()
            obj.delete()
            return Response({"Message":f"ALL SHEAPSS ARE DELETED!!!!"})
        

class goatlist(APIView):
    def get(self,request):
        goat_datas=GoatSerializer(goat.objects.all(),many=True)
        return Response(goat_datas.data)
    
    def post(self,request):
        goat_datas=GoatSerializer(data=request.data)
        if goat_datas.is_valid():
            goat_datas.save()
            return Response({"Message":"New GOAT added!!"})
        else:
            return Response(goat_datas.errors)
        
    def put(self,request):
        data=request.data
        update_goat=data['goat_name']
        goat_datas=GoatSerializer(data=data)
        if goat_datas.is_valid():
            goat_datas.save()
            return Response({"Message":f"GOAT {update_goat} IN WHOLE UPDATED!!!!"})
        else:
            return Response(goat_datas.errors)
        
    def patch(self,request):
        data=request.data
        update_goat=data['goat_name']
        goat_datas=GoatSerializer(data=data,partial=True)
        if goat_datas.is_valid():
            goat_datas.save()
            return Response({"Message":f"GOAT {update_goat} UPDATED!!!!"})
        else:
            return Response(goat_datas.errors)
        
    def delete(self,request):
        data=request.data
        delete_goat=data['goat_name']
        if delete_goat!="*":
            obj=goat.objects.get(goat_name=delete_goat)
            obj.delete()
            return Response({"Message":f"GOATS {delete_goat} DELETED!!!!"})
        else:
            obj=goat.objects.all()
            obj.delete()
            return Response({"Message":f"ALL GOATS ARE DELETED!!!!"})


# Classes for Nested queryset generation (help for searching child objects under parent objects)
 
class childlistset(generics.ListAPIView):
    serializer_class=ChildSerializer
    
    def get_queryset(self):
        queryset=child.objects.all()
        child_names = self.request.query_params['search']
        if child_names is not None:
            queryset=queryset.filter(child_name__startswith=child_names)
        return queryset

class cowlistset(generics.ListAPIView):
    serializer_class=CowSerializer
    
    def get_queryset(self):
        queryset=cow.objects.all()
        cow_names = self.request.query_params['search']
        if cow_names is not None:
            queryset=queryset.filter(cow_name__startswith=cow_names)
        return queryset

class sheaplistset(generics.ListAPIView):
    serializer_class=SheapSerializer
    
    def get_queryset(self):
        queryset=sheap.objects.all()
        sheap_names = self.request.query_params['search']
        if sheap_names is not None:
            queryset=queryset.filter(sheap_name__startswith=sheap_names)
        return queryset

class goatlistset(generics.ListAPIView):
    serializer_class=GoatSerializer
    
    def get_queryset(self):
        queryset=goat.objects.all()
        goat_names = self.request.query_params['search']
        if goat_names is not None:
            queryset=queryset.filter(goat_name__startswith=goat_names)
        return queryset   

# Writing ModelViewsets for all views only ( including ROUTER )

class familyviewset(ModelViewSet):
    serializer_class=FamilySerializer
    queryset=family.objects.all()
        
class childviewset(ModelViewSet):
    serializer_class=ChildSerializer
    queryset=child.objects.all()

class cowviewset(ModelViewSet):
    serializer_class=CowSerializer
    queryset=cow.objects.all()

class sheapviewset(ModelViewSet):
    serializer_class=SheapSerializer
    queryset=sheap.objects.all()

class goatviewset(ModelViewSet):
    serializer_class=GoatSerializer
    queryset=goat.objects.all()
