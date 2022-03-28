from django.shortcuts import render

from .models import FeedbackData
from .forms import FeedbackForm
from django.http.response import HttpResponse
import datetime as dt
date1 = dt.datetime.now()


def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')

            FeedbackData(
                name=name1,
                rating=rating1,
                feedback=feedback1,
                date=date1
            ).save()

            form = FeedbackForm()
            feedbacks = FeedbackData.objects.all()

            return render(request, 'feedback.html', {'harendra': form, 'feedbacks': feedbacks})

        else:
            return HttpResponse("invalid feedback")

    else:
        form = FeedbackForm()
        feedbacks = FeedbackData.objects.all()

        return render(request, 'feedback.html', {'harendra': form, 'feedbacks': feedbacks})
