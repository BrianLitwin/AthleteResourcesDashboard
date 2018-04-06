var React = require('react')
var ReactDOM = require('react-dom')

import SidebarView from './ViewControllers/SideBar.js'

class TopViewController extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      workouts: [],
      finishedLoading: false
    }

    this.sideBarMenuOptions = ["Workouts"]
    this.loadWorkoutsFromServer = this.loadWorkoutsFromServer.bind(this)
  }

  componentDidMount() {
    this.loadWorkoutsFromServer()
  }

  loadWorkoutsFromServer() {

    const getUserID = () => {
      var path = window.location.pathname
      var substrings = path.split('/');
      var length = substrings.length
      return substrings[length - 2]
    }


    var url = '/data/workout_data/' + getUserID()
    console.log(url)

      $.ajax({
          url: url,
          datatype: 'json',
          cache: false,
          success: function(workouts) {
            this.setState({ workouts: workouts, finishedLoading: true })
            console.log(this.state.workouts)
          }.bind(this)
      })
    }


    render() {

      const mainContainer = {
        marginLeft: 280
      }

      switch (this.state.finishedLoading) {
        case true:
          return(
            <div>
              <SidebarView sideBarOptions={this.sideBarMenuOptions}/>
              <div style={mainContainer}>
                <WorkoutsViewController workouts={this.state.workouts}/>
              </div>

            </div>
          )

        case false:
          return(<div> loading </div> )

      }
    }
  }


  class WorkoutsViewController extends React.Component {

    render() {
      return (
        this.props.workouts.map(workout=>(
          <WorkoutView workout={workout}/>
      )))
    }
  }


  class WorkoutView extends React.Component {
  	constructor(props){
    super(props)
    this.workout = new Workout(props.workout)
    }

    render() {

      const headerStyle = {
      backgroundColor: 'rgba(16,113,255,0.1)',
      color: '#0073e6',
      padding: '3px 3px'

      }

    	return (
      <div>
      <p style={headerStyle}> {this.workout.workout.date} </p>
      {this.workout.sequences.map(sequence=>(
      	<div style={{
        display: 'inline-block',
        marginBottom: 20,
        width: '100%',
        padding: "5px 5px 5px 5px"
        }}>
          <SequenceView sequence={sequence}/>
        </div>
      ))}
      </div>

      )
      }
  }

  class SequenceView extends React.Component {
  constructor(props) {
  super(props)
  this.sequence = props.sequence
  const exerciseMetrics = props.sequence.exerciseMetrics()
  this.emsModel = new ExerciseMetricsModel(exerciseMetrics)
  }

  render() {


  const leftColumn = {
    width: '50%',
    float: 'left',
  	clear: 'both'
  }

  const statsContainer = {
  	width: '50%',
    float: 'left',
  }

  return(

      this.sequence.containers.map(container=>(
      	<div>
          <div style={leftColumn}>
            <EM_ContainerView container={container}/>
          </div>
          <div style={statsContainer}>
            <EMStatsView stats={ this.emsModel.stats() } />
          </div>
         </div>
      ))

  )
  }

  }

  class EM_ContainerView extends React.Component {
  constructor(props) {
  super(props)
  this.container = props.container
  }

  render() {

  const headerStyle = {
  	display: 'inline-block',
  	paddingBottom: 5
  }

  return(
  <div>
  <label style={headerStyle}> {this.container.exercise.fullName() }</label>
  {this.container.exerciseMetrics.map(em=>(
  	<ExerciseMetricView exerciseMetric={em} />
  ))}
  </div>
  )
  }

  }

  class ExerciseMetricView extends React.Component {
  constructor(props) {
  super(props)
  this.em = props.exerciseMetric
  }

  render() {

  const displayString = {
  width: '50%',
  display: 'inline-block',
  paddingBottom: 5
  }

  const oneRmPercentage = {
  color: '#0073e6',
  width: '45px',
  display: 'inline-block',
  paddingRight: '5px',
  textAlign: 'right'
  }

  return(
  <div>
  <label style={displayString}> {this.em.em.display_string} </label>
  <label style={oneRmPercentage}> {this.em.percentageOfOneRM()}%</label>
  <label> {this.em.calculateRepRM()}% </label>
  </div>
   )
  }

  }



  class Workout  {
  constructor(workout){
  this.workout = workout
  this.sequences = workout.sequences.map(sequence=>(new Sequence(sequence)))
  }

  }

  class Sequence {
  constructor(sequence){
  this.sequence = sequence
  this.containers = sequence.em_containers.map(container=>(
  	new EM_Container(container)
  ))
  }

  exerciseMetrics() {
  	return this.containers.reduce((ems, container)=>
   	ems.concat(container.exerciseMetrics), []
    )
  }

  }

  class EM_Container {
  constructor(container) {
  this.container = container
  const exercise = new Exercise(container.exercise)
  this.exercise = exercise
  this.exerciseMetrics = container.exercise_metrics.map(exerciseMetric=>(
  	new ExerciseMetric(exerciseMetric, exercise)
  ))
  }

  }

  class Exercise {
    constructor(exercise) {
      console.log("exercise created")
      this.exercise = exercise
      this.metricInfos = exercise.metric_info.map(metricInfo=>(
        new Metric_Info(metricInfo)
      ))
    }

    fullName() {
      return this.exercise.name + " " + this.exercise.variation
    }

    weightUnitOfMeasurement() {
      const weightUnit = this.metricInfos.find(metricInfo=>(
        metricInfo.meitricInfo.metric === "Weight"
      ))
      return weightUnit ? weightUnit.metricInfo.unit_of_measurement : ""

    }

  }

  class Metric_Info {
    constructor(metricInfo){
      this.metricInfo = metricInfo
    }
  }

  class ExerciseMetric {
    constructor(exerciseMetric, exercise) {
    this.em = exerciseMetric
    this.exercise = exercise
  }

  percentageOfOneRM() {
  	const value = this.em.weight / this.exercise.exercise.oneRepMax
    return (value* 100).toFixed(0)
  }

  calculateRepRM() {
  	const weight = this.em.weight
    const reps = this.em.reps
    const oneRM = this.exercise.exercise.oneRepMax
    const rm = reps === 1 ? oneRM : oneRM / (1 + (reps / 30))
    return ((weight/rm)*100).toFixed(0)
   }

   volume() {
   	return this.em.weight * this.em.reps * this.em.sets
   }

   totalReps() {
   	return this.em.reps * this.em.sets
   }

  }

  class ExerciseMetricsModel {
  constructor(exerciseMetrics) {
  this.exerciseMetrics = exerciseMetrics
  }

  stats() {
  	var stats = new EMStats()
    this.exerciseMetrics.forEach(em=>(
      stats.increment(em)
    ))
  	return stats
  }

  }

  class EMStats {
  constructor() {
  this.volume = 0
  this.totalReps = 0
  this.totalSets = 0
  }

  increment(exerciseMetric) {
  	this.volume += exerciseMetric.volume()
    this.totalReps += exerciseMetric.totalReps()
    this.totalSets += exerciseMetric.em.sets
  }

  }


  class EMStatsView extends React.Component {
    render() {

      const unitOfMeasurement = ""

    	const listItems = [
        {label: "Volume", value: this.props.stats.volume.toString() + " " + unitOfMeasurement},
        {label: "Total Reps", value: this.props.stats.totalReps},
        {label: "Total Sets", value: this.props.stats.totalSets},
      ]

    	const list = {
      	listStyle: 'none'
      }

      const label={
      	display: 'inline-block',
        width: 75,
        paddingRight: 5,
        paddingBottom: 2,
      }

      const container = {
      	borderRight: '#0073e6 solid',
        backgroundColor: 'rgba(16,113,255,0.1)',
        width: '50%',
        marginTop: 20
      }

      const innerBox = {
      	padding: "5px 5px 5px 5px"
      }

      return(

      <div style={container}>
        <div style={innerBox}>
  			{listItems.map(item=>(
        	<li style={list}>
          <label style={label}> {item.label}: </label>
          <label > {item.value} </label>
          </li>
        ))}
        </div>
      </div>
      )
    }
  }



ReactDOM.render(<TopViewController />, document.getElementById('container'))
