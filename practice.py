# from django.shortcuts import render
# from django.http import HttpResponse 
# from datetime import datetime, time

# from django.shortcuts import render

# from django import forms
# import sys

# class word_number_form(forms.Form):

#     word = forms.CharField(label = 'a word', max_length = 1)
#     number = forms.IntegerField(label = 'a number', max_val = sys.maxsize)


# #views.py

# def word_number_form(request):

#     if request.method == 'POST':
#         form = word_number_form(request.POST)

#         if form.is_valid():
#             submitted_word = form.cleaned_data["word"]
#             submitted_number = form.cleaned_data["number"]
#             output = ""

#             for i in range(0, submitted_number):
#                 output += submitted_word + " "
            
#             return HttpResponse(output)
#         else:
#             return HttpResponse("Invalid input")
#     else:
#         return HttpResponse("Invalid request.method")


from typing import List


def rotate_ntimes(nums: List[int], n):

    while(n > 0):
        replaced_item = nums[0]
        for i in range(1, len(nums)):
            nums[i-1] = nums[i]
        n -=1
        nums[len(nums)-1] = replaced_item

    
    return nums, nums[0]

print(rotate_ntimes([1,2,3,4,5,6], 6-6))




