from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Calculation
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

# def index(request):
    # original version

#     latest_calc_list = Calculation.objects.order_by("-created")[:5]

#     template = loader.get_template("django_calc/index.html")
#     context = {
#         "latest_calc_list": latest_calc_list
#     }


#     return HttpResponse(template.render(context, request))


class Calc:
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def sub(x, y):
        return x - y
    
    @staticmethod
    def mul(x, y):
        return x * y
    
    @staticmethod
    def pow(x, y):
        return x**y
    
    @staticmethod
    def div(x, y):
        if y != 0:
            return x/y
        
        return "ZeroDivisionError"
    

def index(request):
    # shortened version that uses render()

    latest_calc_list = Calculation.objects.order_by("-created")[:5]

    context = {
        "latest_calc_list": latest_calc_list
    }


    return render(request, "django_calc/index.html", context)



def calc(request):
    # return "Make a calculation."
    
    if request.method == "POST":
        
        print(f"request = {request}")
        print(f"{dir(request)=}")
        print(f"{request.POST=}")
        print(f"{request.POST['x']=}")
        print(f"{request.POST['y']=}")
        print(f"{request.POST['operation']=}")


        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['operation']


        op_func_map = {
            "add": Calc.add,
            "sub": Calc.sub,
            "div": Calc.div,
            "mul": Calc.mul,
            "pow": Calc.pow
        }

        calc = op_func_map[op](x, y)
        
        op_title_map = {
            "add": "Add",
            "sub": "Subtract",
            "div": "Divide",
            "mul": "Multiply",
            "pow": "Power"
        }

        title = op_title_map[op]

        c = Calculation(created = timezone.now(), x = x, y = y, operation = title, answer = float(calc))
        print(f"calc = {c}")
        c.save()

        context = {"answer": calc}

        return render(request, "django_calc/calc.html", context)

        


        # calc = get_object_or_404(Calculation, )

        # print("---------------------------------------")
        # print(calc)
        # print("---------------------------------------")
    else:
        
        return render(request, "django_calc/calc.html")

       

    