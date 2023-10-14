from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

# Create your views here.

class ReviewView(CreateView):
    model= Review
    form_class= ReviewForm
    template_name= "reviews/review.html"
    success_url="/thank-you"


class ThankYouView(TemplateView):
    template_name= "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works"
        return context
    
class ReviewsListView(ListView):
    template_name= "reviews/review_list.html"
    model= Review
    context_object_name= "reviews"

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

    def get_context_data(self, **kwargs ):
        context= super().get_context_data(**kwargs)
        loaded_review = self.object
        request= self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] =  favorite_id == str(loaded_review)
        return context

class AddFavoriteView(View):
    def post(self, request):
        review_id = request.POST.get('review_id')
        print("Review ID from form:", review_id)  # Debugging: Print review_id to console
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)

# class AddFavoriteView(View):
#     def post(self, request):
#         review_id=request.POST['review_id']
#         #fav_review = Review.objects.get(pk=review_id)
#         request.session["favorite_review"] = review_id
#         return HttpResponseRedirect("/reviews/" + review_id)
    
# class ReviewView(FormView):
#     form_class= ReviewForm
#     template_name= "reviews/review.html"
#     success_url="/thank-you"

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
    
    # def get(self, request):
    #     form= ReviewForm()
        
    #     return render(request,"reviews/review.html", {
    #             "form": form
    #         })
       
    # def post(self, request):
    #     form= ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")



    # def get_queryset(self):
    #     base_query= super().get_queryset()
    #     data= base_query.filter(rating__gt=4)
    #     return data
    # def get_context_data(self, **kwargs) :
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context
    
   
# class SingleReviewView(TemplateView):
#     template_name= "reviews/single_review.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk=review_id)
#         # reviews = Review.objects.all()
#         context["review"] = selected_review
#         return context
    
    
    # def get(self, request):
    #     return render(request,"reviews/thank_you.html")




'''
# def thank_you(request):
#     return render(request,"reviews/thank_you.html")


def review(request):
    # if request.method == 'POST':
    #     entered_username=request.POST['username'] #extracting data from request Post parameter
    #     #validate
    #     if entered_username == "" and len(entered_username)<= 100:
    #         return render(request, "reviews/review.html", {
    #             "has_error":True #POST request,but have invalid data, we render the template again, with has_error set to true.
    #         })
    #     print(entered_username)
    #     return HttpResponseRedirect("/thank-you")
    if request.method == 'POST':
        #existing_data= Review.objects.get(pk=1) #updating
        form= ReviewForm(request.POST )

        if form.is_valid():
            #print(form.cleaned_data)
            #creates new Review object
            #form.cleaned_data is a dictionary containing all the form fields and their cleaned (validated) values.
            # review= Review(
            #     user_name= form.cleaned_data['user_name'],
            #     review_text=form.cleaned_data['review_text'],
            #     rating=form.cleaned_data['rating']
            # ) // since using model form skip this
            form.save()# saves it to database, creating a new record
            return HttpResponseRedirect("/thank-you")
    else:   
        form = ReviewForm() #constructor

    return render(request,"reviews/review.html", {
                #"has_error":True
                "form": form
            })
'''
