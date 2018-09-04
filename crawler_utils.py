import json
import os.path


def comments_to_json(comments):
         result = []
         for comment in comments:
            try:
             print comment.id
             result.append({#"url": comment.url,
                       "body": comment.body,
                       "id": comment.id,
                       "replies": comments_to_json(comment.replies)})
            except:
             continue

         return result
     
        


def save_submission(submission, storage_dir):
    with open(os.path.join(storage_dir, submission.id), "w") as f:
        f.write(json.dumps({"url": submission.url,
                            "text": submission.selftext,
                            "title": submission.title,
                            "score": submission.score,
                            "comments": comments_to_json(submission.comments)}))
        f.close()
