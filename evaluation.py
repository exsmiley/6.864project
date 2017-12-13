

class Evaluation():

	def __init__(self,data):

		self.data = data

    def evaluate(self):
        p_at_one = self.precision(1)
        p_at_five = self.precision(5)
        map = self.map()
        mrr = self.mrr()
        return map, mrr, p_at_one, p_at_five


	def precision(self,precision_at):
		scores = []
		for item in self.data:
			temp = item[:precision_at]
			if any(val==1 for val in item):
				scores.append(sum([1 if val==1 else 0 for val in temp])*1.0 / len(temp) if len(temp) > 0 else 0.0)
		return sum(scores)/len(scores) if len(scores) > 0 else 0.0


	def map(self):
		scores = []
		missing_MAP = 0
		for item in self.data:
			temp = []
			count = 0.0
			for i,val in enumerate(item):
				if val == 1:
					count += 1.0
					temp.append(count/(i+1))
			if len(temp) > 0:
				scores.append(sum(temp) / len(temp))
			else:
				missing_MAP += 1
		return sum(scores)/len(scores) if len(scores) > 0 else 0.0


	def mrr(self):

		scores = []
		for item in self.data:
			for i,val in enumerate(item):
				if val == 1:
					scores.append(1.0/(i+1))
					break

		return sum(scores)/len(scores) if len(scores) > 0 else 0.0
