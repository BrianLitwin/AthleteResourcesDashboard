from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User

#Todo: don't re-add the same exercises over and over again
#have to have a way of deleting thing
#figure out how to do complexes

class Workouts(models.Model):

    coreDataID = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    @classmethod
    def createOrUpdate(cls, workouts, user):

        for data in workouts:

            coreDataID = data['coreDataID']
            date = datetime.strptime(data["date"], "%m-%d-%Y %H:%M")

            try:
                workout = Workouts.objects.get(coreDataID=coreDataID, user=user)

            except:
                workout = Workouts()
                workout.coreDataID = coreDataID
                workout.user = user

            data = data['name']
            workout.date = date
            workout.save()

class Sequences(models.Model):

    coreDataID = models.IntegerField()
    workout = models.ForeignKey(Workouts, on_delete=models.CASCADE, related_name='sequences')
    workout_order = models.IntegerField()
    user = models.ForeignKey(User)

    @classmethod
    def createOrUpdate(cls, sequences, user):

        for data in sequences:

            print(data)

            try:
                print(data['workout'])
                workout = Workouts.objects.get(coreDataID=data['workout'], user=user)

            except:
                print("Could not find workout for sequence!!")
                break

            coreDataID = data['coreDataID']


            try:
                sequence = Sequences.objects.get(coreDataID=coreDataID, workout=workout)

            except:
                sequence = Sequences()
                sequence.user = user

            sequence.coreDataID = coreDataID
            sequence.workout = workout
            sequence.workout_order = data['workout_order']
            sequence.save()



class Exercises(models.Model):

    coreDataID = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    variation = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    oneRepMax = models.IntegerField(default=0)

    @classmethod
    def createOrUpdate(cls, exercises, user):
        for data in exercises:
            coreDataID = data["coreDataID"]

            try:
                exercise = Exercises.objects.get(coreDataID=coreDataID, user=user)
            except:
                exercise = Exercises()
                exercise.coreDataID = coreDataID
                exercise.user = user

            exercise.name = data["name"]
            exercise.variation = data["variation"]
            exercise.oneRepMax = data["oneRepMax"]
            print(exercise.oneRepMax)
            exercise.save()

class Metric_Info(models.Model):

    coreDataID = models.IntegerField()
    metric = models.CharField(max_length=50)
    output_label = models.CharField(max_length=100)
    sort_in_ascending_order = models.BooleanField(default=False)
    unit_of_measurement = models.CharField(max_length=25)
    exercise = models.ForeignKey(Exercises, on_delete=models.CASCADE, related_name='metric_info')

    def __str__(self):
        return self.metric

    @classmethod
    def createOrUpdate(cls, metricInfos, user):
        for data in metricInfos:
            coreDataID = data["coreDataID"]

            try:
                exercise = Exercises.objects.get(coreDataID=data["exercise"], user=user)

            except:
                print("could not find exercise for metric_info!")

            try:
                metric_info = Metric_Info.objects.get(coreDataID=data["exercises"], user=user)

            except:
                metric_info = Metric_Info()
                metric_info.coreDataID = data["coreDataID"]

            metric_info.exercise = exercise
            metric_info.metric = data["metric"]
            metric_info.sort_in_ascending_order = data["sort_in_ascending_order"]
            metric_info.unit_of_measurement = data["unit_of_measurement"]
            metric_info.save()


class EM_Containers(models.Model):

    coreDataID = models.IntegerField()
    order = models.IntegerField()
    sequence = models.ForeignKey(Sequences, on_delete=models.CASCADE, related_name='em_containers')
    exercise = models.ForeignKey(Exercises, related_name='exercise')
    user = models.ForeignKey(User)

    def __str__(self):
        return "order %d sequence %d" % (self.order, self.sequence.workout_order)

    @classmethod
    def createOrUpdate(cls, em_containers, user):

        for data in em_containers:
            coreDataID = data["coreDataID"]

            try:
                parentSequence = Sequences.objects.get(coreDataID=data["sequence"],user=user)

            except:
                print("could not get em_containers sequence!!")

            try:
                exercise = Exercises.objects.get(coreDataID=data["exercise"], user=user)

            except:
                print("could not find em_containers exercise!")

            try:
                em_container = EM_Containers.objects.get(coreDataID=coreDataID, sequence=parentSequence, user=user)

            except:
                em_container = EM_Containers()
                em_container.coreDataID = coreDataID
                em_container.sequence = parentSequence
                em_container.user = user
                em_container.exercise = exercise

            em_container.order = data["order"]
            em_container.save()



class Exercise_Metrics(models.Model):

    coreDataID = models.IntegerField()
    display_string = models.CharField(max_length=50)
    container = models.ForeignKey(EM_Containers, on_delete=models.CASCADE, related_name="exercise_metrics")
    user = models.ForeignKey(User)
    set_number = models.IntegerField()
    weight = models.IntegerField(default=0)
    reps = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    length = models.IntegerField(default=0)
    velocity = models.IntegerField(default=0)
    personalRecord = models.ForeignKey(Exercises, null=True)

    def __str__(self):
        return "coredataID %d order %d container %d sequence %d" % (self.coreDataID, self.set_number, self.container.order, self.container.sequence.workout_order)

    @classmethod
    def createOrUpdate(cls, exerciseMetrics, user):

        for data in exerciseMetrics:

            coreDataID = data["coreDataID"]
            set_number = data["set_number"]

            try:
                container = EM_Containers.objects.get(coreDataID=data["em_container"], user=user)

            except:
                print("couldn't get exercise_metrics em_container")
                print(coreDataID)

            try:
                exercise_metric = Exercise_Metrics.objects.get(coreDataID=coreDataID, container=container, set_number=set_number)

            except:
                exercise_metric = Exercise_Metrics()
                exercise_metric.coreDataID = coreDataID
                exercise_metric.user = user
                exercise_metric.set_number = set_number

            exercise_metric.container = container
            exercise_metric.display_string = data["display_string"]
            exercise_metric.weight = data['weight']
            exercise_metric.reps = data['reps']
            exercise_metric.sets = data['sets']
            exercise_metric.time = data['time']
            exercise_metric.length = data['length']
            exercise_metric.velocity = data['velocity']
            exercise_metric.save()


class Settings(models.Model):

    unique_id = models.CharField(max_length=90)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=90)

    @classmethod
    def createOrUpdate(cls, settings):

        try:
            data = settings[0]
            unique_id = data["coreDataID"]
            print(unique_id)

        except:
            print("settings not uploaded  ")

        try:
            userSettings = Settings.objects.get(unique_id=unique_id)
            print("Previous User Fetched")
            return userSettings.user

        except:
            userSettings = Settings()
            userSettings.unique_id = unique_id
            password = "homerun24"
            email = "noMail@noMail.com"

            newUser = User.objects.create_user(unique_id, email, password)
            newUser.username = unique_id
            print(password)
            newUser.save()
            userSettings.email = email
            userSettings.password = password
            userSettings.user = newUser
            userSettings.save()
            print("new user created")
            return newUser
