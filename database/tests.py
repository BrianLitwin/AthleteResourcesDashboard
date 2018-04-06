from django.test import TestCase
from models import Workouts, Sequences
# Create your tests here.



class Sequences_Tests(TestCase):

    def test_duplicate_sequences_created(self):

        workout = Workouts()
        workout.coreDataID = 2
        workout.save()

        sequence = Sequences()
        sequence.coreDataID = 1
        sequence.workout = workout
        sequence.workout_order = 0
        sequence.save()

        sequenceJSON = [{'workout': 2, 'coreDataID': 1, 'workout_order': 1}]

        #test that two sequences aren't created w/ the same coreDataID
        #only want to update the sequence if it already exists

        Sequences.createOrUpdate(sequenceJSON)

        sequenceCount = workout.sequences.all().count()

        self.assertEqual(sequenceCount, 1)
