from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone

from .models import score

def countscore(m):
    l = [
        m.H_1,
        m.H_2,
        m.H_3,
        m.H_4,
    ]
    return l.count('E')


def timetaken(m):
    delta = m.end_time - m.start_time
    print(delta)
    return delta


def login_page(request):
    if request.method == 'POST':
        E_id = request.POST['Employee_ID']
        E_name = request.POST['Employee_Name']
        test = authenticate(request, username=E_id, password=E_id)
        if test is None:
            nuser = User.objects.create_user(username=E_id, password=E_id)
        user = authenticate(request, username=E_id, password=E_id)
        login(request, user)
        check_ = score.objects.filter(employee_id=E_id)
        ds = score(employee_id=E_id, employee_name=E_name, attempts=(len(check_) + 1))
        ds.save()
        return redirect('ins')
    return render(request, "game/login/login.html")


@login_required(login_url='login')
def instructions(request):
    check = score.objects.filter(employee_id=request.user.username)
    context = {'name': check[len(check) - 1].employee_name}
    return render(request, "game/login/instruction.html", context)


@login_required(login_url='login')
def h1(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_1 != None:
        return redirect('h2')
    if check[len(check) - 1].start_time == None:
        st = timezone.now()
        check[len(check) - 1].start_time = st
        check[len(check) - 1].save()
    if request.method == 'POST':
        if request.POST.get("E"):
            return redirect('h1q')
        else:
            return redirect('h1w')
    else:
        return render(request, "game/Hurdle_1/hurdle_Ethical_Ques.html")


@login_required(login_url='login')
def h1q(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_1 != None:
        return redirect('h2')
    if request.method == 'POST':
        if request.POST.get("C"):
            check[len(check) - 1].H_1 = "E"
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_1/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h1w')
        else:

            return render(request, "game/Hurdle_1/hurdle_Ques_Retry.html")
    elif check[len(check) - 1].H1t == 0:
        return render(request, "game/Hurdle_1/options_exhausted.html")
    else:
        context = {'txt': """Oh...Looks like they are busy in a meeting. While you wait for them answer the question below."""}
        return render(request, "game/Hurdle_1/hurdle_Question.html", context)

@login_required(login_url='login')
def h1w(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_1 != None:
        return redirect('h2')
    check[len(check) - 1].H_1 = "UE"
    check[len(check) - 1].save()
    return render(request, "game/Hurdle_1/Unethical.html")

@login_required(login_url='login')
def h1t(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_1 != None:
        return redirect('h2')
    if request.method == 'POST':
        if request.POST.get("C"):
            check[len(check) - 1].H_1 = "E"
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_1/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h1w')
        else:
            check[len(check) - 1].H1t -= 1
            check[len(check) - 1].save()
            if check[len(check) - 1].H1t == 0:
                return render(request, "game/Hurdle_1/options_exhausted.html")
            return render(request, "game/Hurdle_1/hurdle_Ques_Retry.html")
    t = 'Good job you should never give up here you got another chance to choose the correct option ! '
    if check[len(check) - 1].H1t == 2:
        context = {'txt': t + "2 attempts more"}
    elif check[len(check) - 1].H1t == 1:
        context = {'txt': t + "Only 1 attempt left"}
    else:
        return render(request, "game/Hurdle_1/options_exhausted.html")
    return render(request, "game/Hurdle_1/hurdle_Question.html", context)


@login_required(login_url='login')
def h2(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_2 != None:
        return redirect('h3')
    if check[len(check) - 1].H_1 == None:
        return redirect('h1')
    if check[len(check) - 1].start_time == None:
        st = timezone.now()
        check[len(check) - 1].start_time = st
        check[len(check) - 1].save()
    if request.method == 'POST':
        if request.POST.get("E"):
            return redirect('h2q')
        else:
            return redirect('h2w')
    else:
        return render(request, "game/Hurdle_2/hurdle_Ethical_Ques.html")


@login_required(login_url='login')
def h2q(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_2 != None:
        return redirect('h3')
    if check[len(check) - 1].H_1 == None:
        return redirect('h1')
    if request.method == 'POST':
        if request.POST.get("C"):
            check[len(check) - 1].H_2 = "E"
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_2/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h2w')
        else:

            return render(request, "game/Hurdle_2/hurdle_Ques_Retry.html")
    elif check[len(check) - 1].H2t == 0:
        return render(request, "game/Hurdle_2/options_exhausted.html")
    else:
        context = {'txt': """Oh looks like you need wait for vehicles to pass !. While you wait for clearance, please answer
                the question below."""}
        return render(request, "game/Hurdle_2/hurdle_Question.html", context)

@login_required(login_url='login')
def h2w(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_2 != None:
        return redirect('h3')
    if check[len(check) - 1].H_1 == None:
        return redirect('h1')
    check[len(check) - 1].H_2 = "UE"
    check[len(check) - 1].save()
    return render(request, "game/Hurdle_2/Unethical.html")

@login_required(login_url='login')
def h2t(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_2 != None:
        return redirect('h3')
    if check[len(check) - 1].H_1 == None:
        return redirect('h1')
    if request.method == 'POST':
        if request.POST.get("C"):
            check[len(check) - 1].H_2 = "E"
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_2/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h2w')
        else:
            check[len(check) - 1].H2t -= 1
            check[len(check) - 1].save()
            if check[len(check) - 1].H2t == 0:
                return render(request, "game/Hurdle_2/options_exhausted.html")
            return render(request, "game/Hurdle_2/hurdle_Ques_Retry.html")
    t = 'Good job you should never give up here you got another chance to choose the correct option ! '
    if check[len(check) - 1].H2t == 2:
        context = {'txt': t + "2 attempts more"}
    elif check[len(check) - 1].H2t == 1:
        context = {'txt': t + "Only 1 attempt left"}
    else:
        return render(request, "game/Hurdle_2/options_exhausted.html")
    return render(request, "game/Hurdle_2/hurdle_Question.html", context)


@login_required(login_url='login')
def h3(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 != None:
        return redirect('h4')
    if check[len(check) - 1].H_2 == None:
        return redirect('h2')
    if check[len(check) - 1].start_time == None:
        st = timezone.now()
        check[len(check) - 1].start_time = st
        check[len(check) - 1].save()
    if request.method == 'POST':
        if request.POST.get("E"):
            return redirect('h3q')
        else:
            return redirect('h3w')
    else:
        return render(request, "game/Hurdle_3/hurdle_Ethical_Ques.html")


@login_required(login_url='login')
def h3q(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 != None:
        return redirect('h4')
    if check[len(check) - 1].H_2 == None:
        return redirect('h2')
    if request.method == 'POST':
        if request.POST.get("C"):
            check[len(check) - 1].H_3 = "E"
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_3/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h3w')
        else:

            return render(request, "game/Hurdle_3/hurdle_Ques_Retry.html")
    elif check[len(check) - 1].H3t == 0:
        return render(request, "game/Hurdle_3/options_exhausted.html")
    else:
        context = {'txt': """Good decision ! You have chosen to stay with the biker while the ambulance arrives. Please
                answer the following question."""}
        return render(request, "game/Hurdle_3/hurdle_Question.html", context)

@login_required(login_url='login')
def h3w(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 != None:
        return redirect('h4')
    if check[len(check) - 1].H_2 == None:
        return redirect('h2')
    check[len(check) - 1].H_3 = "UE"
    check[len(check) - 1].save()
    return render(request, "game/Hurdle_3/Unethical.html")

@login_required(login_url='login')
def h3t(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 != None:
        return redirect('h4')
    if check[len(check) - 1].H_2 == None:
        return redirect('h2')
    if request.method == 'POST':
        if request.POST.get("C"):
            check[len(check) - 1].H_3 = "E"
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_3/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h3w')

        else:
            check[len(check) - 1].H3t -= 1
            check[len(check) - 1].save()
            if check[len(check) - 1].H3t == 0:
                return render(request, "game/Hurdle_3/options_exhausted.html")
            return render(request, "game/Hurdle_3/hurdle_Ques_Retry.html")
    t = 'Good job you should never give up here you got another chance to choose the correct option ! '
    if check[len(check) - 1].H3t == 2:
        context = {'txt': t + "2 attempts more"}
    elif check[len(check) - 1].H3t == 1:
        context = {'txt': t + "Only 1 attempt left"}
    else:
        return render(request, "game/Hurdle_3/options_exhausted.html")
    return render(request, "game/Hurdle_3/hurdle_Question.html", context)


@login_required(login_url='login')
def h4(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 == None:
        return redirect('h3')
    if check[len(check) - 1].H_4 != None:
        return redirect('end')
    if check[len(check) - 1].start_time == None:
        st = timezone.now()
        check[len(check) - 1].start_time = st
        check[len(check) - 1].save()
    if request.method == 'POST':
        if request.POST.get("E"):
            return redirect('h4q')
        else:
            return redirect('h4w')
    else:
        return render(request, "game/Hurdle_4/hurdle_Ethical_Ques.html")


@login_required(login_url='login')
def h4q(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 == None:
        return redirect('h3')
    if check[len(check) - 1].H_4 != None:
        return redirect('end')
    if request.method == 'POST':
        if request.POST.get("C"):
            et = timezone.now()
            check[len(check) - 1].H_4 = "E"
            check[len(check) - 1].save()
            check[len(check) - 1].end_time = et
            check[len(check) - 1].marks = countscore(check[len(check) - 1])
            check[len(check) - 1].time_taken = timetaken(check[len(check) - 1])
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_4/congrats.html")

        elif request.POST.get("UE"):
            return redirect('h4w')

        else:

            return render(request, "game/Hurdle_4/hurdle_Ques_Retry.html")

    elif check[len(check) - 1].H4t == 0:
        return render(request, "game/Hurdle_4/options_exhausted.html")
    else:
        context = {'txt': """Good decision… You have decided to obey traffic rules. Its Ponnamallee Junction. Will take
    time. Please answer the following question while you wait."""}
        return render(request, "game/Hurdle_4/hurdle_Question.html", context)


@login_required(login_url='login')
def h4w(request):
    et = timezone.now()
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 == None:
        return redirect('h3')
    if check[len(check) - 1].H_4 != None:
        return redirect('end')
    check[len(check) - 1].H_4 = "UE"
    check[len(check) - 1].save()
    check[len(check) - 1].end_time = et
    check[len(check) - 1].marks = countscore(check[len(check) - 1])
    check[len(check) - 1].time_taken = timetaken(check[len(check) - 1])
    check[len(check) - 1].save()
    return render(request, "game/Hurdle_4/Unethical.html")

@login_required(login_url='login')
def h4t(request):
    check = score.objects.filter(employee_id=request.user.username)
    if check[len(check) - 1].H_3 == None:
        return redirect('h3')
    if check[len(check) - 1].H_4 != None:
        return redirect('end')
    if request.method == 'POST':
        if request.POST.get("C"):
            et = timezone.now()
            check[len(check) - 1].H_4 = "E"
            check[len(check) - 1].save()
            check[len(check) - 1].end_time = et
            check[len(check) - 1].marks = countscore(check[len(check) - 1])
            check[len(check) - 1].time_taken = timetaken(check[len(check) - 1])
            check[len(check) - 1].save()
            return render(request, "game/Hurdle_4/congrats.html")
        elif request.POST.get("UE"):
            return redirect('h4w')
        else:
            check[len(check) - 1].H4t -= 1
            check[len(check) - 1].save()
            if check[len(check) - 1].H4t == 0:
                return render(request, "game/Hurdle_4/options_exhausted.html")
            return render(request, "game/Hurdle_4/hurdle_Ques_Retry.html")
    t = "Don't Give up ! It's a trait of an ethical driver who doesnt give up in any situation"
    if check[len(check) - 1].H4t == 2:
        context = {'txt': t + " 2 attempts more"}
    elif check[len(check) - 1].H4t == 1:
        context = {'txt': t + " Only 1 attempt left"}
    else:
        return render(request, "game/Hurdle_4/options_exhausted.html")
    return render(request, "game/Hurdle_4/hurdle_Question.html", context)


@login_required(login_url='login')
def end(request):
    check = score.objects.filter(employee_id=request.user.username)
    context = {'name': check[len(check) - 1].employee_name}
    return render(request, "game/login/end.html", context)


def test1(request):
    return render(request, "game/login/instruction.html")


def test2(request):
    return render(request, "game/Hurdle_1/congrats.html")
def test3(request):
    return render(request, "game/Hurdle_1/hurdle_Ethical_Ques.html")
def test4(request):
    return render(request, "game/Hurdle_1/hurdle_Ques_Retry.html")
def test5(request):
    return render(request, "game/Hurdle_1/hurdle_Question.html")
def test6(request):
    return render(request, "game/Hurdle_1/options_exhausted.html")
def test7(request):
    return render(request, "game/Hurdle_1/Unethical.html")