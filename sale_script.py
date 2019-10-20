#! usr/bin/env python3
import praw
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta
import mail as mail

reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', \
                     client_secret='SECRET_KEY_27_CHARS ', \
                     user_agent='YOUR_APP_NAME', \
                     username='YOUR_REDDIT_USER_NAME', \
                     password='YOUR_REDDIT_LOGIN_PASSWORD')


email_info = {
				"send_from" : "FROM_EMAIL_NAME", \
				"password" : "PASSWORD", \
				"send_to" : ["TO_EMAIL_NAME"], \
				"subject" : "reddit sales", \
				"text" : "here are your sales", \
				"server" : "SERVER_NAME", \
				"files" : ["sales.csv"]
			}

# sale_items = ["Viotek GN35DA 35", "Seagate IronWolf 12TB NAS"]

sale_dict = {	"SUBTHREAD_NAME" : \
					[	"PRODUCT_OR_BRAND_NAME", \
						"PRODUCT_OR_BRAND_NAME", \
						"PRODUCT_OR_BRAND_NAME"], \
				"buildapcsales" : \
					[	"Viotek GN35DA 35", \
						"Seagate", \
						"12TB NAS"], \
				"frugalmalefashion" : \
					[	"Adidas",
						"Ultraboost",
						"J.Crew"]
}

found_sales = { "title":[], \
                "score":[], \
                "id":[], \
                "reddit_post":[], \
                "sale_url":[], \
                "comms_num": [], \
                "created": [], \
                "body":[], \
                "time": []}

# subreddit = reddit.subreddit('buildapcsales');
# submissions = subreddit.new(limit=50);
# print(subreddit.new(limit=500));

for sub in sale_dict:
	# print(sale_dict[sub]);
	subreddit = reddit.subreddit(sub);
	submissions = subreddit.new(limit=500);
	sale_items = sale_dict[sub];

	for submission in submissions:

	    # check if item found
	    item_found = [x for x in sale_items if(x.lower() in submission.title.lower())];
	    
	    # check when submission posted
	    date_created = dt.utcfromtimestamp(submission.created_utc);
	    time_between_created = dt.now() - date_created;


	    if (item_found and time_between_created.days<=30):
	    	# print(submission.permalink)
	    	found_sales["title"].append(submission.title);
	    	found_sales["score"].append(submission.score);
	    	found_sales["id"].append(submission.id);
	    	found_sales["reddit_post"].append("=HYPERLINK(\"https://reddit.com"+submission.permalink+"\", \"post link\")");
	    	found_sales["sale_url"].append("=HYPERLINK(\""+submission.url+"\", \"sale link\")");
	    	found_sales["comms_num"].append(submission.num_comments);
	    	found_sales["created"].append(submission.created);
	    	found_sales["body"].append(submission.selftext);
	    	found_sales["time"].append(date_created.strftime("%m/%d/%Y, %H:%M:%S"));

sale_data = pd.DataFrame(found_sales);
# print(sale_data.to_string())


sale_data.to_csv('sales.csv', index=False)


# send email
mail.send_mail(	email_info["send_from"], \
				email_info["password"], \
				email_info["send_to"], \
				email_info["subject"], \
				email_info["text"], \
				email_info["server"], \
				email_info["files"]);
