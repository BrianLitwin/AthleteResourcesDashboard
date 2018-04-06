
var React = require('react')

export default class SidebarView extends React.Component {

    constructor(props) {
      super(props)
    }

    render() {

      const sideBarStyle = {
        borderStyle: 'solid',
        borderWidth: '1px',
        borderColor: '#ECEBEB',
        background: 'white',
        width: '230px',
        position: 'fixed',
        overflowX: 'hidden',
        top: '20px',
        left: '20px',
        zIndex: '1',
        padding: '8px',
      }

      const itemStyle = {
        padding: '6px 8px 6px 16px',
        textDecoration: 'none',
        fontSize: '25px',
        color: '#2196F3',
        display: 'block'
      }

      const highlight = (e) => {
        e.target.style.color = "#064579"
        e.target.style.cursor = "pointer"
      }

      const unhighlight = (e) => {
        e.target.style.color = '#2196F3'
      }

    return (
      <div style={sideBarStyle}>
      {this.props.sideBarOptions.map(option=>(
        <a style={itemStyle}
        onMouseEnter= {highlight.bind(this)}
        onMouseLeave= {unhighlight.bind(this)}
        >
        {option}
        </a>
        ))}
      </div>
    )
    }
  }
