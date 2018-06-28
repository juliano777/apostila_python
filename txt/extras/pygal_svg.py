#_*_ encoding: utf-8 _*_
import pygal

# http://blog.codeeval.com/codeevalblog/2014
# most popular coding languages according to @codeeval
# python for the win! w00t!

data = (
  ("Python", 77.7),
  ("Java", 22.2),
  ("C++", 13),
  ("Ruby", 10.6),
  ("Javascript", 5.2),
  ("TCL", 0.03)
)
    

# Make a Pygal chart
pie_chart = pygal.Pie()

# add a title
pie_chart.title = "CodeEval Most Popular Coding Languages of 2014"

# add the data
for label, data_points in data:
    pie_chart.add(label, data_points)

# Render the chart    
xml_string = pie_chart.render()


f = raw_input('Digite o nome do arquivo que deseja criar:\n')

f = open(f, 'w+')

print >> f, xml_string

f.close()
