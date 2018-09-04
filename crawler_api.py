import praw
import logging
import argparse
from distutils.dir_util import mkpath
from praw.models.reddit.subreddit import SubredditStream
from crawler_utils import save_submission


def get_as_much_stuff_as_possible(storage_dir):
    mkpath(storage_dir, mode=0755)
    r = praw.Reddit(user_agent='searcheng by /u/mansa503',
                    client_id='XeYpcQ3WK7ST9A',
                    client_secret='O4SYscjZbsg5m0EU31caz1SbeiE')
    for method_name in ["hot", "new"]:
        method = getattr(r.subreddit('learnprogramming'), method_name)
        submissions = method(limit=1000)
        for s in submissions:
            save_submission(s, storage_dir)


def crawl_continuously(storage_dir):
    r = praw.Reddit(user_agent='searcheng by /u/mansa503',
                    client_id='XeYpcQ3WK7ST9A',
                    client_secret='O4SYscjZbsg5m0EU31caz1SbeiE')
    for s in submission_stream(r, "learnprogramming"):
        #submission.replace_more_comments(limit=None, threshold=0)
        s.replace_more_comments(limit=None,threshold=0)
        save_submission(s, storage_dir)


def main():
    logging.getLogger().setLevel(logging.DEBUG)

    parser = argparse.ArgumentParser(description='Crawl /r/learnprogramming using api')
    parser.add_argument("--storage_dir", dest="storage_dir", required=True)
    args = parser.parse_args()

    get_as_much_stuff_as_possible(args.storage_dir)
    crawl_continuously(args.storage_dir)


if __name__ == "__main__":
    main()


