from django.shortcuts import render
from django.http  import HttpResponse ,HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


montly_challenges = {
    'january': 'Overcoming Fear of Failure: Many individuals struggle with the fear of failing, which can prevent them from taking risks and pursuing their goals.',
    'februaru': 'Building and Maintaining Healthy Habits: Establishing and sticking to healthy habits, such as regular exercise and proper nutrition, can be difficult.',
    'march': 'Improving Communication Skills: Effectively communicating with others, whether in personal or professional settings, is a challenge for many.',
    'april': 'Managing Conflicts: Handling disputes and disagreements constructively and maintaining relationships despite conflicts.',
    'may': 'Developing Emotional Intelligence: Understanding and managing ones own emotions and recognizing the emotions of others to navigate social complexities.',
    'june': 'Balancing Digital Life: Managing the influence and time spent on digital devices and social media while maintaining real-world connections and activities.',
    'jully': 'Navigating Career Transitions: Switching careers or jobs, whether by choice or due to external circumstances, can be a significant challenge.',
    'august': 'Dealing with Rejection: Facing rejection, whether in personal relationships, job applications, or other areas, and learning to move forward.',
    'september': 'Maintaining Motivation and Focus: Staying motivated and focused on long-term goals in the face of distractions and setbacks.',
    'october': 'Handling Criticism: Receiving and processing constructive criticism without taking it personally or becoming discouraged.',
    'november': 'Cultivating Resilience: Building the ability to bounce back from setbacks, failures, and difficult situations.',
    'december': 'Finding Purpose and Direction: Identifying personal values, passions, and goals to create a fulfilling and meaningful life.'
}


# Create your views here.
def index(request):
    list_items = ''
    months = list(montly_challenges.keys())

    for month in months:
        capitalized_months = month.capitalize()
        month_path = reverse('month-challenge',args=[month] )
        list_items += f"<li><a href=\"{month_path}\">{capitalized_months}</a></li>"

    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def montly_challange_by_number(request, month):
    months = list(montly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid Number !!!')
    redirect_month = months[month - 1]
    redirect_path = reverse('month-challenge',args=[redirect_month] ) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def montly_challange(request, month):
    try:
        challenge_text = montly_challenges[month]
    except:
        return HttpResponseNotFound('This is not supported')
    return HttpResponse(challenge_text)

