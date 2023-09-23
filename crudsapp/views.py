from django.shortcuts import render

# Create your views here.

pp=[] # created a empty list

def index(request):
    if request.method =='POST':     # i used POST method for request
        if request.POST.get('1'):   # if user press 1 ,
            pa=pp.append('1')       # string 1 will be added to the list named PP
            rr = ''.join(pp)        # At this stage ,Html cant show list as output ,so we need to convert list to string
            print(rr)

        elif request.POST.get('2'):
            ra=pp.append('2')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('3'):
            ra=pp.append('3')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('4'):
            ra=pp.append('4')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('5'):
            ra=pp.append('5')
            rr = ''.join(pp)
            print(rr)
            
        elif request.POST.get('6'):
            ra=pp.append('6')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('7'):
            ra=pp.append('7')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('8'):
            ra=pp.append('8')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('9'):
            ra=pp.append('9')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('+'):
            ra=pp.append('+')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('-'):
            ra=pp.append('-')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('*'):
            qa=pp.append('*')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('/'):
            ra=pp.append('/')
            rr = ''.join(pp)
            print(rr)
        elif request.POST.get('0'):
            ra=pp.append('0')
            rr = ''.join(pp)
            if rr=="3240" :
                rr='THis_is_a_Secret_code'

            print(rr)
        elif request.POST.get('C'): #if user press C , list will be cleared
            ra=pp.clear()

        elif request.POST.get('='): #if user press only = 
            try:                    # if list is empty ,no items can be converted to string and can't eval() so this will error 
                r = ''.join(pp)     #list will be converted to sting
                rr=eval(r)          #eval() can calculate stings
                print(rr)
                ra=pp.clear()       #after calculation list will be cleared
            except:
                rr='NiceTry!'
                ra=pp.clear()        # i dont know why i cant add space to this string !

 
    return render(request, 'index.html',locals()) #used locals() for POST method 

