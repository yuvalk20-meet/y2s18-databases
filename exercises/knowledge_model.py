from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	__tablename__ = 'Knowledge'
	article_id = Column(Integer, primary_key=True)
	topic = Column(String)
	rating = Column(Integer)
	url = Column(String)

	def __repr__(self):
		stars = self.rating * "*"
		
		return ("I have read the article {}\n"
   				"I rate it {}\n"
   				"Would you like to read it too? \n"
   				"{}").format(self.topic, stars, self.url)


	

# x = Knowledge()
# x.article_id = 0
# x.topic = "Tomato"
# x.url = "https://en.wikipedia.org/wiki/Tomato"
# x.rating = 3




		
