from django.shortcuts import render
from django.http import Http404,HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    #list_items = ""
    days = list(weekly_challenges.keys())

    # for day in days:
    #     capitalized_day = day.capitalize()
    #     day_path = reverse("week", args=[day])
    #     list_items += f"<li><a href=\"{day_path}\">{capitalized_day}</a></li>"

    # # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

    return render(request,"challenges/index.html",{
        "days":days
    })

def january(request):
    return HttpResponse("<h1>Hey!!! This is January Month<h1>")

def february(request):
    return HttpResponse("<h1>Hey!!! This is February Month<h1>")

def monthly_challenge_month(request,month):
    challenge_text=None
    if month == "march":
        challenge_text="Hey!!! This is March Month"
    elif month == "april":
        challenge_text="Hey!!! This is April Month"
    elif month ==  "may":
        challenge_text="Hey!!! This is May Month"
    elif month == "june":
        challenge_text="Hey!!! This is June Month"
    elif month == "july":
        challenge_text="Hey!!! This is July Month"
    elif month =="august":
        challenge_text="Hey!!! This is August Month"
    elif month=="september":
        challenge_text="Hey!!! This is September Month"
    else:
        return HttpResponseNotFound("This month is not supported")
    return HttpResponse(challenge_text)

def weekly_challenge_by_number(request, day):
    days=list(weekly_challenges.keys())
    if day > len(days):
        return HttpResponseNotFound("Invalid Day")
    redirect_day=days[day-1]
    #return HttpResponseRedirect("/challenges/"+ redirect_day)
    redirect_path = reverse("week", args=[redirect_day]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

weekly_challenges={
    "sunday":"Hey!!! This is Sunday",
    "monday":"Hey!!! This is Monday",
    "tuesday":"Hey!!! This is Tuesday",
    "wednesday":"Hey!!! This is Wednesday",
    "thursday":"Hey!!! This is Thursday",
    "friday":"Hey!!! This is Friday ",
    "saturday":None
}

def weekly_challenge(request, day):
    try:
        challenge_text = weekly_challenges[day]
        #response=f"<h1>{challenge_text}</h1>"
        #response = render_to_string("challenges/challenge.html")
        #return HttpResponse(challenge_text)
        return render(request, "challenges/challenge.html",{
            "text":challenge_text,
            "month_name": day.capitalize()
        })
    except:
        # response=render_to_string("404.html")
        # return HttpResponseNotFound(response)
        raise Http404()
   