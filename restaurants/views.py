from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { "my_list": [{"restaurant_name": "Al Sorror",
                     "food_type": "Rice And Meat"
                     },
                    {"restaurant_name": "Al Baik",
                     "food_type": "Fast Foods"
                     },
                    {"restaurant_name": "Khalof",
                     "food_type": "Foul"
                     }],



    }
    return render(request, 'list.html', context)


def restaurant_detail(request):
    context = {"my_object": {"restaurant_name": "Al Sorror",
                            "food_type": "Rice And Meat"},

               }
    return render(request, 'detail.html', context)
