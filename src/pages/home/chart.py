import plotly.graph_objects as go

def skill_radio_chart():
  # Define the data for the Scatterpolar plot
  fig = go.Figure(data=go.Scatterpolar(
    r=[7, 7, 9, 8, 7, 9, 6, 6],
    theta=[
      "Machine Learning", 
      'Probability & Statistics', 
      'Math', 
      "Data Structure and Algorithms", 
      'Web Development',
      "Visualization", 
      "Storytelling", 
      "Research and Experimentation"
    ],
    fill='toself',  # Fill the area within the radar plot
    marker=dict(color='darkgoldenrod'),  # Customize marker color
    line=dict(color='seagreen')  # Customize line color
  ))

  # Update the layout of the figure
  fig.update_layout(
    polar=dict(
      radialaxis=dict(
        visible=True,  # Show the radial axis
        range=[0, 10],  # Set the range of the radial axis
        tickfont=dict(size=12),  # Customize font size of the ticks
        gridcolor='lightgray',  # Customize grid color
      ),
      angularaxis=dict(
        tickfont=dict(size=13, color='darkgoldenrod'),  # Customize font size of the angular ticks
      ),
    ),
    paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
    plot_bgcolor='rgba(0,0,0,0)',  # Transparent plot background
    showlegend=False,  # Hide the legend
  )
  return fig