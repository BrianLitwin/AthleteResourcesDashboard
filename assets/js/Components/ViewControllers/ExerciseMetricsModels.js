


class WorkoutModel {

  constructor(props) {

  }

  get Sequences() {
    var s = sequences.sort(function(a,b) {
      return a.workout_order > b.workout_order
    })
    return s
  }


}

class SequenceModel {



}



class ExerciseMetricModel {

  constructor(props){
    this.em = props.em
  }

  get volume() {
    return this.em.weight * this.em.reps * this.em.sets
  }

  get totalReps() {
    return this.reps * this.sets
  }

}
