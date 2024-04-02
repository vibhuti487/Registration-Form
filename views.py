from django.shortcuts import render, redirect, get_object_or_404
# from .forms import RegistrationForm
from .models import User
#from rest_framework import status
#from rest_framework.response import Response
#from rest_framework.views import APIView
#from .serializers import UserSerializer
#from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse

# def register(request):
  #  if request.method == 'POST':
 #       form = RegistrationForm(request.POST)
  #      if form.is_valid():
   #         form.save()
    #        return redirect('registration_success')
     #   else:
      #      return render(request,'register_page.html',{'form':form})
    #else:
     #   form= RegistrationForm()
    #return render(request,'register_page.html',{'form':form})
        
#def registration_success(request):
 #   return render(request, 'registration_success.html')

#class UserRegistration(APIView):
 #   def post(self,request):
  #      serializer = UserSerializer(data=request.data)
   #     if serializer.is_valid():
    #        serializer.save()
     #       return Response(serializer.data, status=status.HTTP_201_CREATED)
      #  return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
#class UserViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.all()
    #serializer_class=UserSerializer

def registration(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        birthdate = request.POST.get('birthdate')
        address = request.POST.get('address')

        user= User(first_name=first_name,last_name=last_name,email=email,phone=phone,password=password,birthdate=birthdate, address= address)
        user.save()

        return redirect('user_page')
    
    elif request.method == 'GET':
        return render(request,'register_page.html')
    
def user_page(request):
    users = User.objects.all()
    return render(request, 'user_page.html',{'users':users})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id) 
    if request.method =='POST':
        user.delete()
        return redirect('user_page')
    return render(request,'delete_user.html',{'user':user})
    
