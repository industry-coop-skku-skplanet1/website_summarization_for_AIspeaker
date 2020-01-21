import math
import operator
from parsing import Tag_parser

class Tf_idf():
	def __init__(self,text,url):
		self.text = text
	#def __init__(self,url):
		self.url = url
		self.tf_dict={}
		self.tf_idf_dict={}
		self.word_rank={}


	def get_wordFreq_page(self):
		temp_df_dict={}
		for line in self.text:
			for word in line:
				if word not in self.tf_dict.keys():
					self.tf_dict[word]=1		# get TF
					temp_df_dict[word]=1		# get DF
				else:
					self.tf_dict[word]+=1	# get TF

		return temp_df_dict


	def get_tf_idf(self,df_dict,total_n):
		for word in self.tf_dict.keys():
			tf_idf=self.tf_dict[word]*math.log(total_n/(df_dict[word]+1),10)
			self.tf_idf_dict[word]=tf_idf
		pass

	def sort_dict(self):
		temp_dict=sorted(self.tf_idf_dict.items(),key=lambda t : t[1],reverse=True)
		return temp_dict

	def get_word_rank(self):
		temp_dict=sorted(self.tf_idf_dict.items(),key=lambda t : t[1],reverse=True)
		for idx, (key, _) in enumerate(temp_dict):
			self.word_rank[key]=idx+1
		pass
