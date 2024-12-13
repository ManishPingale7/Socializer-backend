from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from django.db.models import Q


class RegisterView(APIView):

    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]

    # Register a single user
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            print(serializer.data)

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):

    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        print(username, password)
        user = authenticate(username=username, password=password)

        if user is not None:
            return Response({"message": "Login successful"}, status=200)
        else:
            return Response({"message": "Invalid credentials"}, status=401)


class ProfileListCreate(APIView):
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]

    # Get all profiles
    def get(self, request):
        search_query = request.query_params.get('query', None)
        if not search_query:
            profiles = Profile.objects.all()
            serializer = ProfileSerializer(profiles, many=True)
            return Response(serializer.data)
        else:
            filter_conditions = Q(username__icontains=search_query) |\
                Q(interests__icontains=search_query) | \
                Q(description__icontains=search_query) | \
                Q(address__icontains=search_query)
            profiles = Profile.objects.filter(filter_conditions)
            serializer = ProfileSerializer(profiles, many=True)
            print(serializer.data)
            return Response(serializer.data, 200)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print("YOUR DATA IS NOT VALID")
        return Response(serializer.errors, status=400)


class ProfileDetail(APIView):
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]

    # Get single profile
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        username = kwargs.get('username')

        try:
            if pk:
                profile = Profile.objects.get(pk=pk)
            elif username:
                profile = Profile.objects.get(username=username)
            else:
                return Response({'error': 'Invalid request'}, status=400)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            print("found profile", profile)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            print("valid")
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            print("Not valid", serializer.data)
            return Response("Error", status=400)
    # Delete single profile

    def delete(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            profile.delete()
            return Response(status=204)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)
