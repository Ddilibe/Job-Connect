from django.core.paginator import Paginator
from django.shortcuts import render, redirect
import datetime
import uuid
import requests
from core_root_api import api_url
# Create your views here.
jobs = [ 
        dict(
            pk=str(uuid.uuid4()),
            opening=30,
            title="software Engineer", 
            details="Experienced in Node.Js, Java, Spring, Bootstrap, Python and Selenium integration and Unit Testing",
            salary="26K - 30k Monthly",
            place='Poland',
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_1.jpeg",
            app_date=datetime.datetime.now(),
            last_date=datetime.datetime.now(),
            company_name="Microsoft"
        ),
        dict(
            pk=str(uuid.uuid4()),
            title="mobile App Engineer",
            details="Experienced in Flutter or React native for uilding a startup app",
            opening=10,
            salary="8k - 10K Monthly",
            place="USA",
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_2.jpeg",
            app_date=datetime.datetime.now(),
            last_date=datetime.datetime.now(),
            company_name="Microsoft"
        ),
        dict(
            pk=str(uuid.uuid4()),
            title="mobile App Developer needed in Binance",
            details="Binance is looking for senior mobile app developer with at least 10 years of experience building cross platform application with flutter, firebase and react native. The role is also remote based and also  willing to attend yearly meeting at binance head quarters in your country",
            opening=10,
            salary="50k - 100K Monthly",
            place="USA",
            time=datetime.date.fromisoformat("2024-04-24").isoformat(),
            image_url="jobs/job_5.jpeg",
            app_date=datetime.datetime.now(),
            last_date=datetime.datetime.now(),
            company_name="Microsoft"
        ),
    ]

def landing_page(request):
    return render(request, "landing_page.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def student_login(request):
    if request.method=='POST':
   
        login_data={"email":request.POST['email'],"password":request.POST['password']}
        response=requests.post(f"{api_url.base_url}/login/",json=login_data)

        if response.json()['status']==True:
            return redirect('landingpage')

        else:
            return redirect('studentsignup')
    return render(request, "auth/student_login.html")

def student_signup(request):
    if request.method=='POST':
    #      "id": "8fd354acae80425db147021537b75a01",
    # "email": "user@example.com",
    # "gender": "Male",
    # "full_name": "Eze Kc",
    # "password": "pbkdf2_sha256$600000$OkFHzcR0NhzqANQBePh4pb$RI4TgTN3LnWbOyA3kUEHpLXbnYveEPc9htIV6zuuCbk=",
    # "phone_number": "0808219999",
    # "student_id": "2019/24355555"
        signup_data={"email":request.POST['email'],"gender":request.POST['gender'],"full_name":request.POST['full_name'],"password":request.POST['password'],'confirm_password':request.POST['confirm_password'],'phone_number':request.POST['phone_number'],'student_id':request.POST['student_id']}
        response=requests.post(f"{api_url.base_url}/register/",json=signup_data)

        if response.json()['status']==True:
            return redirect('studentlogin')

        else:
            return redirect('studentsignup')

    return render(request, "auth/student_signup.html")

def admin_login(request):
    
    return render(request, "auth/company_login.html")

def admin_signup(request):
    return render(request, 'auth/company_signup.html')

def job_list_post(request):
    global jobs
    length = 10
    pages = Paginator(jobs, length)
    page_number = request.GET.get("page", 1)
    page_obj = pages.get_page(page_number)
    context = {'jobs': jobs[(int(page_number)*length)-length: (int(page_number)*length)], 'page_obj': page_obj}
    if query := request.GET.get("query"):
        context['query'] = query
    print(jobs, end="\n\n")
    return render(request, "job/job_list.html", context)

def job_single(request, primary_key):
    print(jobs, end="\n\n")
    if not (single := [i for i in jobs if i['pk'] == primary_key]):
        return redirect('landingpage')
    single = single[0]
    return render(request, "job/single_job.html", context={'single':single})

def reset_password(request):
    return render(request, "auth/reset_password.html")

def change_password(request):
    return render(request, "auth/change_password.html")

def company_profile(request):
    return render(request, "job/company_profile.html")

def student_profile(request):

    return render(request, "job/student_profile.html")

def admin_profile(request):
    return render(request, "job/admin_profile.html")