from rest_framework import serializers

from models import Workouts, Sequences, Metric_Info, Exercises, EM_Containers, Exercise_Metrics

class Metric_InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metric_Info
        fields = '__all__'

class ExercisesSerializer(serializers.ModelSerializer):

    metric_info = Metric_InfoSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Exercises
        fields = ['name', 'variation', 'oneRepMax', 'id', 'metric_info']

class Exercise_MetricsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise_Metrics
        fields = '__all__'

class EM_ContainersSerializer(serializers.ModelSerializer):

    exercise = ExercisesSerializer(read_only=True)
    exercise_metrics = Exercise_MetricsSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = EM_Containers
        fields = ['exercise', 'exercise_metrics', 'order']

class SequencesSerializer(serializers.ModelSerializer):

    em_containers = EM_ContainersSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Sequences
        fields = ['workout_order', 'em_containers']

class WorkoutsSerializer(serializers.ModelSerializer):

    ##setup eager loading

    sequences = SequencesSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = Workouts
        fields = ('date', 'sequences')
