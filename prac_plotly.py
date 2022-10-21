#%%
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
#%%
x = np.array([3, 4])
y1 = np.array([1, 2])
y2 = np.array([3, 4])
df = pd.DataFrame(np.array([x, y1, y2]).T, columns = ['x', 'y1', 'y2'])
#%%
fig = go.Figure()

fig.add_trace(go.Scatter(x = x, y = y1, mode='lines', name='lines'))
fig.add_trace(go.Scatter(x = x, y = y2, mode='lines', name='lines'))

# ticks
xdict = {'tickmode' : "array"
        , 'tickvals': [3, 3.3, 3.5, 4]
        , 'showgrid' : False}
ydict = {'showgrid' : False}
# Edit the layout
fig.update_layout(xaxis_title='能力',
                  yaxis_title='正確題數',
                  xaxis = xdict,
                  yaxis = ydict)

fig.show()

# labdict = {"x":"能力", "y":"正確題數"}
# px.line(df, x = 'x',y = 'y1', labels = labdict)
# px.line(df, x = 'x',y = 'y2', labels = labdict)


# %%
