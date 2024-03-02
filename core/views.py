from django.shortcuts import render
import plotly.express as px
import pandas as pd
from core.forms import DateForm
from core.models import INDICATOR

# Create views here.
def chart(request):
    start = request.GET.get('start')
    end = request.GET.get('end')

    # Query the INDICATOR model for GDP data
    indicators = INDICATOR.objects.all()
    if start:
        indicators = indicators.filter(year__gte=start)
    if end:
        indicators = indicators.filter(year__lte=end)

    # Create a DataFrame from the query results
    df = pd.DataFrame(indicators.values())

    # Create a line graph using Plotly Express
    fig = px.line(
        df,
        x='year',
        y='value',
        color='country',
        title="GDP growth%",
        labels={'year': 'Year', 'value': 'GDP growth'},

    )

    # Update the layout of the graph
    fig.update_layout(
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        },
        height=600  # height of the figure
    )

    # Convert the Plotly graph to HTML
    chart = fig.to_html()

    # Render the HTML in a Django template
    context = {'chart': chart, 'form': DateForm()}
    return render(request, 'core/chart.html', context)
