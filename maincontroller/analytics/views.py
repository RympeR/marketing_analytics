from django.core.mail import send_mail
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import re
import os
from icecream import ic
import numpy as np
import pandas as pd
from plotly.offline import plot
import plotly.graph_objects as go


def index(request):
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30, 35, 25, 45]
        
        trace = go.Scatter(
            x=x1,
            y=y1,
            visible=True,
            opacity=0.6,
            mode='markers',
        )
        layout = dict(
            title='Simple graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis=dict(range=[min(y1), max(y1)]),
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div
    
    context = {
        'plot' : scatter()
    }
    return render(request, 'analytics/index.html', context)
