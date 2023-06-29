import instaloader 
from celery import shared_task
#from algorithms.get_cred import instagram_email,instagram_password
import re
import time
from leads.profile import ProfileRecords
from leads.models import Leads, Task

loader = instaloader.Instaloader()

 
def get_following(username,task_id):
    try:
        loader.login(str("cortifoxsystems"), str("Balkot12123"))
        profile = instaloader.Profile.from_username(loader.context, username)
        following_list = []
        followings = profile.get_followees()
        for following in followings:
            following_list.append(following.username)
        return following_list
    except:
        task = Task.objects.get(id=task_id)
        task.description = "There Was An Error in Authentication , Please Check your Instagram Account ."
        task.status="s"     

@shared_task
def set_data(lead_id, task_id, username):     
    instance = Leads.objects.get(id=lead_id)
    task = Task.objects.get(id=task_id)             
    following_list = get_following(username=username,task_id=task)
    print(following_list)
    task.description = "Followers fetched successfully. Now fetching their details"
    print("Followers Fetched Successfully")
    start_time = time.perf_counter()
    for username in following_list:
        try:
            profile = instaloader.Profile.from_username(loader.context, username)
            fullname = profile.full_name
            print("Full Name", fullname)
            followers_count = profile.followers
            following_count = profile.followees
            bio = profile.biography
            emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", bio)
            
            if len(emails) > 0:
                profile_record = ProfileRecords(
                    leads=instance,
                    name=fullname,
                    username=username,
                    source='Instagram',
                    follower=followers_count,
                    following=following_count,
                    email=emails[0]
                )
                profile_record.save()
            time.sleep(3)
        except instaloader.exceptions.QueryReturnedBadRequestException as e:
            task.description = "Too Many Requests last time , Trying Again After 30 minutes"+"\n "+e
            task.status = "s"
            time.sleep(1800)
            continue
        except:
            continue
        finally:
            end_time = time.perf_counter()
            execution_time = end_time - start_time

            task.status = "c"
            task.description = "The Task Successfully Completed in " + str(execution_time) + " seconds."
            task.save()
