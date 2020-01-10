import math

class Tf_idf:
	def __init__(self,text,url):
		self.text = text
		self.url = url
		self.tf_dict={}
		self.tf_idf_dict={}


	def get_wordFreq_page(self):
		temp_df_dict={}
		for line in self.text:
			for word in line:
				if word not in self.tf_dict.keys():	# get TF
					self.tf_dict[word]=1
				else:
					self.tf_dict[word]+=1
				if word not in temp_df_dict.keys():		# get DF
					temp_df_dict[word]=1

		return temp_df_dict
		


	def get_tf_idf(self,df_dict,total_n):
		for word in self.tf_dict.keys():
			tf_idf=self.tf_dict[word]*math.log(total_n/(df_dict[word]+1),10)
			self.tf_idf_dict[word]=tf_idf
		pass

	def sort_dict(self):
		return sorted(self.tf_idf_dict.items(),key=lambda t : t[1],reverse=True)

