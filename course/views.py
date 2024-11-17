from django.shortcuts import render

from course.models import Count, WhyUs, Feature, Course, Team, FooterLink, About


# Create your views here.
def contact(request):
    return render(request,'contact.html')

def about(request):
    about = About.objects.all()
    footerlink = FooterLink.objects.all()
    return render(request, 'about.html', {'about': about, 'footerlink': footerlink})

def courses(request):
    footerlink = FooterLink.objects.all()
    return render(request,'courses.html', {'footerlink': footerlink})

def course_details(request):
    footerlink = FooterLink.objects.all()
    return render(request,'course-details.html', {'footerlink': footerlink})

def events(request):
    footerlink = FooterLink.objects.all()
    return render(request,'events.html', {'footerlink': footerlink})

def pricing(request):
    footerlink = FooterLink.objects.all()
    return render(request,'pricing.html', {'footerlink': footerlink})

def startpage(request):
    footerlink = FooterLink.objects.all()
    return render(request,'starter-page.html', {'footerlink': footerlink})

def trainers(request):
    footerlink = FooterLink.objects.all()
    return render(request,'trainers.html', {'footerlink': footerlink})

def index(request):
    counts = Count.objects.all()
    whyUs=WhyUs.objects.all()
    feature=Feature.objects.all()
    course=Course.objects.all()
    team=Team.objects.all()
    footerlink = FooterLink.objects.all()
    return render(request,'index.html',{'footerlink':footerlink,'whyUs':whyUs,'counts':counts,'feature':feature,'course':course,'team':team})