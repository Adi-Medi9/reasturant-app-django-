from django.shortcuts import render
from django.http import HttpResponse
from Base_app.models import BookTable, AboutUS, Feedback, ItemList, Items
# Create your views here.

def HomeView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items':items, 'list':list, 'review':review})

def AboutView(request):
    data = AboutUS.objects.all()
    return render(request, 'about.html',{'data':data})

def MenuView(request):
    items = Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html',{'items':items, 'list':list})

def BookTableView(request):
    if(request.method == "POST"):
        name = request.POST.get('user_name')
        email = request.POST.get('user_email')
        phone_number = request.POST.get('phone_number')
        total_person = request.POST.get('total_person')
        booking_date = request.POST.get('booking_date')

        if(name != "" and email != "" and total_person != 0 and booking_date !=""):
            data = BookTable(Name=name,Email=email,Total_person=total_person,   Booking_date=booking_date, Phone_number=phone_number)

            data.save()


    return render(request, 'book_table.html')

def FeedbackView(request):
    if(request.method == "POST"):
        naame = request.POST.get('naame')
        text_area = request.POST.get('text_area')
        rate = request.POST.get('rate')
        img0 = request.POST.get('img0')

        if(naame != "" and text_area != "" and rate != 0 and img0 !=""):
            data = Feedback(User_name= naame,Description=text_area,Rating=rate,Image=img0)

            data.save()
    return render(request, 'feedback.html')