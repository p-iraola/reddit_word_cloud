import praw
import nltk
from collections import Counter
import re
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop_words = set(stopwords.words('english'))

#Add Reddit API information
reddit_read_only = praw.Reddit(client_id='QE3wRk_wltunBxw2aCGFVg', client_secret='dfScNZts4H2XSeEBEVwlcTQX_pePug', user_agent='creamcheesenips')

#Add URL
url = 'https://www.reddit.com/r/AskReddit/comments/10y466h/what_is_the_best_pixar_movie/'
submission = reddit_read_only.submission(url=url)

# Expand all MoreComments objects and extract the comment bodies into a single list
submission.comments.replace_more(limit=None)
post_comments = [comment.body for comment in submission.comments.list()]

#Concatenate all the comment bodies into a single string
post_comments = " ".join(post_comments).lower()

#Split string into a list of words
post_comments = re.findall(r'\w+', post_comments)

#Exclude the stop words
post_comments = [word for word in post_comments if not word in stop_words]

#Get frequency of each word in the list
word_counts = Counter(post_comments)

#Create and display the word cloud
wordcloud = WordCloud(width=800, height=400, max_words=100).generate_from_frequencies(word_counts)

plt.figure(figsize=(15,8))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
