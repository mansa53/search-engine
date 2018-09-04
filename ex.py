import praw

r = praw.Reddit(user_agent='searcheng by /u/mansa503',
                    client_id='XeYpcQ3WK7ST9A',
                    client_secret='O4SYscjZbsg5m0EU31caz1SbeiE')
hotp=r.submission(id='6tpc97')
for top_level_comment in hotp.comments:
    print(top_level_comment.url)
#print hotp


