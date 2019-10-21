# RedditSaleFinder
Script that finds sales on Reddit for products & brands that you want based on subreddits you hand it and sends that catalog in csv format to your email

## Usage

must use python 3.

```
python3 sale_script.py
```


## Configuration


Configure your [Reddit Api](https://www.reddit.com/prefs/apps) by creating an app of a script type and copy the pai information down into the following lines in *sale_script.py*

```
reddit = praw.Reddit(client_id='PERSONAL_USE_SCRIPT_14_CHARS', \
                     client_secret='SECRET_KEY_27_CHARS ', \
                     user_agent='YOUR_APP_NAME', \
                     username='YOUR_REDDIT_USER_NAME', \
                     password='YOUR_REDDIT_LOGIN_PASSWORD')
```

**Configure email info**
if using Gmail make replace *SERVER_NAME* with *smtp.gmail.com:587* and make sure you change permissions to turn **ON** [Allow less secure apps](https://myaccount.google.com/lesssecureapps) in your mail settings and modify the following info in *sale_script.py*
```
email_info = {
				"send_from" : "FROM_EMAIL_NAME", \
				"password" : "PASSWORD", \
				"send_to" : ["TO_EMAIL_NAME"], \
				"subject" : "reddit sales", \
				"text" : "here are your sales", \
				"server" : "SERVER_NAME", \
				"files" : ["sales.csv"]
			}
```
lastly modify *sales_dict* with the products or brands that you would like to search for based on a specific subreddits 

some example are left in
```
sale_dict = {
				"SUBTHREAD_NAME" : \
					[	"PRODUCT_OR_BRAND_NAME1", \
						"PRODUCT_OR_BRAND_NAME2", \
						"PRODUCT_OR_BRAND_NAME"3],
				"SUBTHREAD_NAME2" : \
					[	"PRODUCT_OR_BRAND_NAME1", \
						"PRODUCT_OR_BRAND_NAME2", \
						"PRODUCT_OR_BRAND_NAME3"],
			}
```

## Installation
```
pip install -r requirements.txt
```

