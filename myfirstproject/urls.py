from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.utils import IntegrityError
from django.shortcuts import render
from django.db import connection
from django.urls import path

cursor = connection.cursor()

create_table_query ="""
CREATE TABLE IF NOT EXISTS "user" ( 
    "first_name" varchar(30) NOT NULL, 
    "last_name" varchar(30) NOT NULL, 
    "mobile_number" varchar(15) NOT NULL, 
    "email" varchar(254) PRIMARY KEY, 
    "password" varchar(30) NOT NULL, 
    "dob" text NOT NULL, 
    "address" text NOT NULL 
);"""
cursor.execute(create_table_query)

@api_view(['GET'])
def get_user(request):
	try:
		cursor.execute("select *from user")
		data = cursor.fetchall()
		users = [
			{
				"first_name":user[0],
				"last_name":user[1],
				"mobile_number":user[2],
				"email":user[3],
				"password":user[4],
				"dob":user[5],
				"address":user[6]
			}
			for user in data
		]
		print(users)
		return Response({'error':False, "message":"Get user working","payload":users})
	except Exception as e:
		print(e)
		return Response({'error':True, "message":"Internal server error"})

@api_view(['POST'])
def save_user(request):
    try:
        data = request.data
        query = """insert into user (first_name, last_name, mobile_number, email, password, dob, address) values(%s, %s, %s, %s, %s, %s, %s)"""

        values = [
            data['first_name'],
            data['last_name'],
            data['mobile_number'],
            data['email'],
            data['password'],
            data['dob'],
            data['address']
            ]
        cursor.execute(query,values)
        return Response({'error':False, "message":"User saved successfully"})
    except IntegrityError as e:
        return Response({'error':True, "message":"Email already exists"})
    except Exception as e:
        print(e)
        return Response({'error':True, "message":"Internal server error"})

@api_view(['DELETE'])
def delete_user(request):
	try:
		data = request.data
		email = data['email']
		password = data['password']
		cursor.execute("select *from user where email =%s",[email])
		user = cursor.fetchone()
		if user:
			stored_password = user[4]
			if password == stored_password:
				cursor.execute("delete from user where email=%s",[email])
				return Response({'error':False, "message":"User deleted"})
			else:
				return Response({'error':True, "message":"Incorrect password"})
		else:
			return Response({'error':True, "message":"User does not exist"})
		 
	except Exception as e:
		return Response({'error':True, "message":"Internal server error"})



@api_view(['GET'])
def get_registration_page(request):
	return render(request,"registration.html")


@api_view(['GET'])
def get_data_page(request):
	return render(request,"data.html")

urlpatterns = [
    path('', get_registration_page),
	path("data", get_data_page),
	path("getUser", get_user),
	path("saveUser", save_user),
	path("deleteUser", delete_user),
]
