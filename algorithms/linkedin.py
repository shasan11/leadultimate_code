import requests
import re
from getpass import getpass
from celery import shared_task
from leads.profile import ProfileRecords
from leads.models import Leads


@shared_task
def retrieve_employees(input_name,employees_counter,id1):
    email="shasandkl4@gmail.com"
    password="Balkot11"
    session = login(email, password)
    employees = retrieve_employees(session, 'https://www.linkedin.com/company/' + input_name, employees_counter)

    for employee in employees:
        employee_url = 'https://www.linkedin.com/in/' + employee
        email, follower_count, following_count = get_employee_info(session, employee)

        print("Employee: " + employee)
        print("Email: " + email)
        print("Followers: " + str(follower_count))
        print("Following: " + str(following_count))
        print("-------------------------")

        # Create a new Leads instance and save it
        if email!=None:
                # Create a new ProfileRecords instance and fill in the data
                instance = Leads.objects.get(pk=id1)
                profile_record = ProfileRecords()
                profile_record.leads = instance
                profile_record.name = employee
                profile_record.username =""
                profile_record.source = 'LinkedIn'  # Fill in the appropriate source value
                profile_record.follower = follower_count
                profile_record.following = following_count
                # profile_record.company = ''  # Fill in the appropriate company value
                profile_record.email = email 

                # Save the ProfileRecords instance
                profile_record.save()
                print("Fetched", profile_record.email)
def login(email, password):
    session = requests.session()
    mobile_agent = ('Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 '
                    'Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) '
                    'Version/4.0 Mobile Safari/534.30')
    session.headers.update({'User-Agent': mobile_agent,
                            'X-RestLi-Protocol-Version': '2.0.0'})

    anon_response = session.get('https://www.linkedin.com/login')
    login_csrf = re.findall(r'name="loginCsrfParam" value="(.*?)"', anon_response.text)

    if email == '':
        email = input('What is your LinkedIn email (Your account might have 10+ relations):\n')

    if password == '':
        password = getpass('Enter your password:\n')

    auth_payload = {
        'session_key': email,
        'session_password': password,
        'isJsEnabled': 'false',
        'loginCsrfParam': login_csrf
    }

    response = session.post('https://www.linkedin.com/checkpoint/lg/login-submit?loginSubmitSource=GUEST_HOME',
                            data=auth_payload)

    try:
        if response.json()['challengeId']:
            print('You got locked by LinkedIn.\nTry again later or enter a good password if your password was incorrect.')
            exit()
    except KeyError:
        pass

    try:
        if response.json()['data']['url']:
            print('Bad email or password.\n')
            exit()
    except KeyError:
        pass

    try:
        if response.json()['data']['challengeResult']['challengeType']:
            print('Please validate your email address.\n')
            exit()
    except KeyError:
        pass

    try:
        if response.json()['data']['challengeResult']['actor']:
            print('Login succeeded.\n')
            return session
    except KeyError:
        print('Connection failed. Please check your credentials.')
        exit()
 

def get_employee_info(session, employee_id):
    url = 'https://www.linkedin.com/voyager/api/identity/profiles/' + employee_id + '/profileContactInfo'

    response = session.get(url)
    profile_data = response.json()['data']

    email = ''
    if 'emailAddress' in profile_data and 'emailAddress' in profile_data['emailAddress']:
        email = profile_data['emailAddress']['emailAddress']

    follower_count = 0
    following_count = 0
    if 'followerCount' in profile_data:
        follower_count = profile_data['followerCount']
    if 'followingCount' in profile_data:
        following_count = profile_data['followingCount']

    return email, follower_count, following_count
