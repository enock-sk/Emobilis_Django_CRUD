from django.shortcuts import render

from course.models import Count, WhyUs, Feature, Course, Team, FooterLink


# Create your views here.
def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def courses(request):
    return render(request,'courses.html')

def course_details(request):
    return render(request,'course-details.html')

def events(request):
    return render(request,'events.html')

def pricing(request):
    return render(request,'pricing.html')

def startpage(request):
    return render(request,'starter-page.html')

def trainers(request):
    return render(request,'trainers.html')

def index(request):
    counts = Count.objects.all()
    whyUs=WhyUs.objects.all()
    feature=Feature.objects.all()
    course=Course.objects.all()
    team=Team.objects.all()
    footerlink = FooterLink.objects.all()
    return render(request,'index.html',{'footerlink':footerlink,'whyUs':whyUs,'counts':counts,'feature':feature,'course':course,'team':team})