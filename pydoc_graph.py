# 21/04/2020 redandgreen.co.uk

from matplotlib import pyplot as plt
from matplotlib import style
import csv
import json
import warnings
warnings.simplefilter("ignore")

style.use('ggplot')

class Matgraph(object):

	"""  Read a CSV file and generate 1 graph per row"""
 
	def __init__(self):
		self.vals = []
		self.row_num = 2

	def make_graphs(self):
		with open('gsd.csv','r') as f:
			reader = csv.reader(f)
			next(reader)
			for row in reader:
					self.vals =  row
					input_x = (self.vals[:5])
					input_y = (self.vals[5:])
					input_x = list(map(int,input_x))
					input_y = list(map(int,input_y))
					print(input_x)
					print(input_y)
					print(f"Making Graph number {self.row_num}")
					fig, ax = plt.subplots()
					ax.set_title(f"redandgreen.co.uk graph {self.row_num}",fontsize=14)
					plt.bar(input_x,input_y)
					plt.savefig(f"plot{self.row_num}.png")
					plt.clf()
					self.row_num += 1

if __name__ == "__main__":

	autograph = Matgraph()
	autograph.make_graphs()

	print("\nGraphs made - Check CWD  for your .png files")
	print("Make multiple DOCX files next? - Put .png file in '/images'")
	print("Then run multi_doc.py\n")
