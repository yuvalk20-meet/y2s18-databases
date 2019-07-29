from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(atopic, arating, aurl):
	aricle_ob = Knowledge(
		
		topic = atopic,
		rating = arating,
		url = aurl
		)

	session.add(aricle_ob)
	session.commit()
	print(aricle_ob)
add_article( "Pigs", 9, "https://en.wikipedia.org/wiki/Pig")

def query_all_articles():
	art = session.query(Knowledge).all()
	return art
print("l")
print(query_all_articles())
print("hi")
def query_article_by_topic():
	
	top = input("Enter a topic:")
	ar = session.query(
       Knowledge).filter_by(
       topic=top).first()

def delete_article_by_topic():
	top = input("Enter a topic to be deleted:")
	ar = session.query(
       Knowledge).filter_by(
       topic=top).delet()

def delete_all_articles():
	articleob = session.query(Knowledge).delete()
	print("everything was deleted")


def edit_article_rating():

	listallart = session.query(
      Knowledge).all()
	for l in listallart:
		l.rating = input("Insert a new rating to "+ l.topic + " article")
		print(l.topic + " rating is now " + l.rating)

#delete_all_articles()
edit_article_rating()
