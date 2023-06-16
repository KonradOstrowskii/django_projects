from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Write a program that calculates the factorial of a given number.",
    "february": "Create a program that generates a random password with a specified length.",
    "march": "Write a program that converts a given sentence to Pig Latin.",
    "april": "Implement a binary search algorithm to find an element in a sorted list.",
    "may": "Create a program that generates the Fibonacci sequence up to a specified limit.",
    "june": "Write a program that determines whether a given number is a prime number.",
    "july": "Implement a stack data structure using a list in Python.",
    "august": "Create a program that simulates a game of rock-paper-scissors against the computer.",
    "september": "Write a program that counts the occurrences of each word in a given text file.",
    "october": "Implement a binary tree data structure and perform a tree traversal.",
    "november": "Create a program that generates a maze and solves it using a suitable algorithm.",
    "december": "Write a program that simulates a simple quiz game with multiple-choice questions."
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months":months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        return HttpResponseNotFound("This month is not supported")