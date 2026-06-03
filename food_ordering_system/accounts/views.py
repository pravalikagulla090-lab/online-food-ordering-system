from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .serializers import UserRegisterSerializer, UserSerializer

def frontend_login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            user_role = getattr(request.user, 'role', 'customer')
            if request.user.is_superuser or request.user.is_staff or user_role == 'admin':
                return redirect(request.GET.get('next') or '/manage/')
            return redirect(request.GET.get('next') or '/')

        next_url = request.GET.get('next', '/')
        response = render(request, 'login.html', {'next_url': next_url})
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        return response

    try:
        payload = json.loads(request.body.decode('utf-8'))
    except (ValueError, json.JSONDecodeError):
        payload = request.POST

    username = payload.get('username')
    password = payload.get('password')
    portal_type = payload.get('portal') or request.POST.get('portal') or 'customer'
    next_url = payload.get('next') or request.POST.get('next') or '/'

    user = authenticate(username=username, password=password)
    if user:
        auth_login(request, user)
        request.session.save()
        token, _ = Token.objects.get_or_create(user=user)
        user_role = getattr(user, 'role', 'customer')
        if user.is_superuser or user.is_staff:
            user_role = 'admin'

        if portal_type == 'admin' and user_role != 'admin':
            if request.content_type == 'application/json':
                return JsonResponse({'error': 'Admin access required'}, status=403)
            return render(request, 'login.html', {'error': 'Admin access required'})

        if portal_type == 'admin':
            next_url = '/manage/'
        elif user_role == 'admin' and next_url == '/cart/':
            next_url = '/manage/'

        response_data = {
            'token': str(token.key),
            'access': str(token.key),
            'role': user_role,
            'user': UserSerializer(user).data,
            'redirect': next_url
        }
        # Always return JSON for POST requests
        return JsonResponse(response_data, status=200)

    # Return JSON for POST requests (form now sends JSON)
    return JsonResponse({'error': 'Invalid Credentials'}, status=401)

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = [] # [cite: 5]

class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = [] # [cite: 6]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password) # [cite: 6]
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            user_role = getattr(user, 'role', 'customer') # [cite: 7]
            if user.is_superuser or user.is_staff:
                user_role = 'admin' # [cite: 8]

            return Response({
                'token': str(token.key),
                'access': str(token.key), # Token duplication pattern avoids JavaScript parsing errors [cite: 313]
                'role': user_role, # [cite: 8]
                'user': UserSerializer(user).data # [cite: 9]
            }, status=status.HTTP_200_OK)
            
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED) # [cite: 9]