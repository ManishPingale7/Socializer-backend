from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny


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
        profiles = Profile.objects.all()

        serializer = ProfileSerializer(profiles, many=True)

        return Response(serializer.data)

    # Create single profile
    def post(self, request):

        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        print("YOUR DATA IS NOT VALID")
        return Response(serializer.errors, status=400)


class ProfileDetail(APIView):
    permission_classes = [IsAuthenticated]

    # Get single profile
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # Update single profile
    def put(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=404)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Reponse(serializer.error, status=400)
    # Delete single profile

    def delete(self, request, pk):
        try:
            profile = Profile.objects.get(pk=pk)
            profile.delete()
            return Response(status=204)
        except Profile.DoesNotExist:
            return Response({'error': 'Profile not found'}, status=404)
