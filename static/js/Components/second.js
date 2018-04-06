var React = require('react')
var ReactDOM = require('react-dom')


class WorkoutList extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      selectedWorkoutIndex: 0,
      data: []
    };
    this.loadWorkoutsFromServer = this.loadWorkoutsFromServer.bind(this),
    this.renderWorkout = this.renderWorkout.bind(this)
    this.getUserID = this.getUserID.bind(this)
  }

  componentDidMount() {
    this.loadWorkoutsFromServer()
  }

  getUserID() {
    var path = window.location.pathname
    var substrings = path.split('/');
    var length = substrings.length
    console.log(length)
    return substrings[length - 2]

  }

  loadWorkoutsFromServer() {

    var url = '/data/workout_data/' + this.getUserID()
    console.log(url)

      $.ajax({
          url: url,
          datatype: 'json',
          cache: false,
          success: function(data) {
              this.setState({data: data})
          }.bind(this)
      })
    }

    renderWorkout(workout) {
      let index = this.state.data.indexOf(workout)
      this.setState({
        selectedWorkoutIndex: index
      })
      workout = this.state.data[this.state.selectedWorkoutIndex]
    }

    render() {

      return (
        <div>
          <div style={sideNav}>
            <WorkoutItems data={this.state.data} renderWorkout={this.renderWorkout} />
          </div>
          <div style={main}>
            <Workout workout={this.state.data[this.state.selectedWorkoutIndex]}/>
          </div>
        </div>
      )
    }
  }

  class Workout extends React.Component {

    renderSequences() {

      const sequences = this.props.workout.sequences

      sequences.sort(function(a,b) {
        return a.workout_order > b.workout_order
      })

      return(
        sequences.map(sequence=>(
          <Sequence sequence={sequence} />
        ))
      )
    }

    render() {
      return (
        this.props.workout ?
        <div>
        <div> {this.props.workout.date} </div>
        {this.renderSequences()}
        </div>
        : null
      )
    }
  }


  class Sequence extends React.Component {

    renderEmContainers() {

      const containers = this.props.sequence.em_containers

        containers.sort(function(a,b) {
          a.order > b.order
      })

      return(
        containers.map(container=>(
          <EM_Container container={container} />
        ))
      )
    }

    render() {
      return (
        this.props.sequence ?
        <div>
          {this.renderEmContainers()}
        </div>
        : null
      )
    }
  }


  class EM_Container extends React.Component {

    renderExerciseMetrics() {
      const exerciseMetrics = this.props.container.exercise_metrics
      return (
        exerciseMetrics.map(e=>(
          <li> {e.display_string} </li>
        )
      )
    )
  }

      render() {
        return (
          this.props.container.exercise ?
          <div>
          <li> {this.props.container.exercise.name} </li>
          {this.renderExerciseMetrics()}
          </div>
          : null
        )
      }
  }

  class WorkoutItems extends React.Component {

    highlight(e) {
      e.target.style.backgroundColor = "blue"
    }

    unhighlight(e) {
      e.target.style.backgroundColor = "red"
    }



    render() {
      return (
        this.props.data.map(workout=> (
            <a style={listStyle}
            onClick= {()=>this.props.renderWorkout(workout)}
            onMouseEnter={this.highlight.bind(this)}
            onMouseLeave={this.unhighlight.bind(this)}
            >
            {workout.date}
            </a>
        ))
      )
    }
  }

  const main = {
    marginLeft: '260px',
    color: 'blue'
  }


  const sideNav = {
    height: '100%',
    width: '260px',
    backgroundColor:'red',
    position: 'fixed',
    overflowX: 'hidden',
    zIndex: '1',
    top: '0',
    left: '0',
  }

  const listStyle = {
    display: 'block',
    padding: '16px 12px',
    listStyleType: 'none',
  };



ReactDOM.render(<WorkoutList />, document.getElementById('container'))
