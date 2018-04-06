from django.shortcuts import render
from rest_framework.views import APIView
from models import Workouts, Settings, Sequences, Metric_Info, Exercises, Exercise_Metrics, EM_Containers
from serializers import WorkoutsSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User



# Create your views here.

class All_Workout_Data(APIView):
    def post(self, request):
        data = request.data

        #retutns user that corresponds to settings sent from the app
        user = Settings.createOrUpdate(data["Settings"])

        Workouts.createOrUpdate(data['Workouts'], user)
        Sequences.createOrUpdate(data['Sequences'], user)
        Exercises.createOrUpdate(data['Exercises'], user)
        EM_Containers.createOrUpdate(data["EM_Containers"], user)
        Exercise_Metrics.createOrUpdate(data["Exercise_Metrics"], user)
        Metric_Info.createOrUpdate(data["Metric_Info"], user)
        return Response()
    

class Workout_Data(APIView):

    def get(self, request, userID):
        print(userID)
        user = User.objects.get(id=userID)
        workouts = Workouts.objects.filter(user=user).order_by('date')
        serializer = WorkoutsSerializer(workouts, many=True)
        print(serializer.data)
        return Response(serializer.data)

class Exercise_Data(APIView):

    def get(self, request, userID):
        user = User.objects.get(id=userID)
        exercises = Exercises.objects.filter(exercise_metrics__isNull=False)
