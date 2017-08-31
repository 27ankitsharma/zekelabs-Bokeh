# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 14:31:54 2017

@author: ZekeLabs
"""

# stream.py
from math import cos, sin

from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
import itertools

p = figure(x_range=(-100.1, 100.1), y_range=(-100.1, 100.1))
p.circle(x=0, y=0, radius=1, fill_color=None, line_width=2)

# this is the data source we will stream to
source = ColumnDataSource(data=dict(x=[1], y=[0]))
p.line(x='x', y='y', line_width=2, source=source)

xd = itertools.chain(range(100))



def update():
    x, y = source.data['x'][-1], source.data['y'][-1]
    print (x,y)
    # construct the new values for all columns, and pass to stream
    new_data = dict(x=[next(xd)], y=[next(xd)])
    source.stream(new_data, rollover=20)
    
curdoc().add_periodic_callback(update, 1500)
curdoc().add_root(p)