var React = require('react')


export default class WorkoutsViewController {
  constructor(workouts) {
    this.workouts = workouts
    this.viewControllers = workouts.map(=>workout(
      WorkoutViewController(workout)
    ))
  }

}



export default class WorkoutViewController extends React.Component {
  constructor(workout) {
    this.workout = workout
    this.model = WorkoutModel(workout)
  }

  render() {
    return (<WorkoutView workout=workout>)
  }

}

class WorkoutModel {
  constructor(workout) {
    this.workout = workout
  }

  sequences() {

    const sequences = this.workout.sequences

    return sequences.sort(function(a,b) {
      return a.workout_order > b.workout_order
    })

  }

  emContainers() {

    const containers = sequences.map(sequence=>(
      sequence.em_containers
    ))

    return containers.sort(function(a,b) {
        return a.order > b.order
    })

  }

}


class SequenceModel {
  constructor(sequence){
    this.sequence = sequence
  }
}

class EM_ContainerModel {
  constructor(container) {
    this.container = container
  }

  exerciseMetrics() {
    return em.container.exercise_metrics.sort(function(a,b) {
      return a.set_number > b.set_number
    })
  }

}



class WorkoutView extends React.Component {



}
