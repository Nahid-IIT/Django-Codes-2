from django.shortcuts import render
import datetime
def home(request):
    d = {
         'author': 'Rahim',
         'age':10,
         'lst':["Nahid","is","Best"],
         'courses':[
             {
                'id':1,
                'name':"python",
                'fee': 5000
             },
             {
                'id':2,
                'name':"django",
                'fee':6000
             },
             {
                'id':3,
                'name':"DSA",
                'fee':7000
             },
            ],
          'birthday': datetime.datetime.now()
        }
    return render(request, 'first_app/home.html',d)
