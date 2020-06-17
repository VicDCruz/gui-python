import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl

import plotly
import plotly.graph_objs as go

sys.argv.append("--disable-web-security")
app = QApplication(sys.argv)

x1 = [10, 3, 4, 5, 20, 4, 3]
trace1 = go.Box(x=x1)
layout = go.Layout(showlegend=True)
data = [trace1]

# fig = go.Figure(data=data, layout=layout)
fig =go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

path = QDir.current().filePath('plotly-latest.min.js')
local = QUrl.fromLocalFile(path).toString()

raw_html = '<html><head><meta charset="utf-8" />'
raw_html += '<script src="{}"></script></head>'.format(local)
raw_html += '<body>'
raw_html += plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
raw_html += '</body></html>'

view = QWebEngineView()
view.setHtml(raw_html)
view.show()

sys.exit(app.exec_())
