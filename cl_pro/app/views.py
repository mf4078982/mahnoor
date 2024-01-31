from django.shortcuts import render,HttpResponse

# Create your views here.
def cal(request):
    re  = None
    
    if request.method == 'POST':
            opare = request.POST.get('opare')
            opar1 = float(request.POST.get('opar1'))
            opar2 = float(request.POST.get('opar2'))
            if opare == 'add':
                re  = opar1 + opar2
            elif opare == 'sub':
                re = opar1 - opar2
            elif opare == 'mul':
                re = opar1 * opar2
            elif opare == 'div':
                if opar2 != 0:
                    re = opar1 / opar2
                else:
                    return HttpResponse('connot divi by zero')
    return render(request,'add.html',{'result':re})
                    
                
