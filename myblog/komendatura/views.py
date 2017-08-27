from django.shortcuts import render

# Create your views here.
def who_is_on_post(request):
    def shift(l, n):
        return l[n:] + l[:n]

    smena = [9,11,13,15,17,19,21,23,1,3,5,7]
    kom_otd_begin_time = 9
    kom_otd_end_time = 17
    sol_count = int(request.GET.get('sol_count', 0))
    kom_otd = request.GET.get('kom_otd', '')
    soldiers = []
    soldier_names = []
    result_post = []
    if sol_count > 0:
        soldiers.append(kom_otd)
        for i in range(0, sol_count):
            soldiers.insert(0, request.GET.get('soldier'+str(i), ''))
            soldier_names.append(['soldier'+str(i), request.GET.get('soldier'+str(i), '')])

        for i in smena:
            time_for_2post = i+2
            if time_for_2post > 24: time_for_2post=-24

            if i in (9,11,13,15,17,7):
                if soldiers[1]==kom_otd: soldiers = shift(soldiers, -1)
                post1 = str(i) + ':00 ' + kom_otd
            else:
                post1 = str(i) + ':00 ' + soldiers[0]
            post2 = str(i) + ':00 ' + soldiers[1]

            soldiers = shift(soldiers, -1)    
            result_post.append([post1,post2])

    params = {
        'sol_count':sol_count, 
        'sol_count_range':range(sol_count), 
        'smena':smena, 
        'result_post':result_post, 
        'kom_otd':kom_otd,
        'soldier_names':soldier_names,
    }

    return render(request, 'who_is_on_post.html', params)
