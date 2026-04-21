from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskModel, CompleteModel, TrashModel, Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate


# ================= HELPER =================
def get_next_task_id(user):
    last_task = TaskModel.objects.filter(user=user).order_by('-user_task_id').first()
    if last_task and last_task.user_task_id:
        return last_task.user_task_id + 1
    return 1


# ================= AUTH =================
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'msg': 'User already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('add')
        else:
            return render(request, 'login.html', {'msg': 'Invalid credentials'})

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


# ================= HOME =================
@login_required(login_url='login')
def home(request):
    data = TaskModel.objects.filter(user=request.user).order_by('user_task_id')
    return render(request, 'home.html', {'data': data})


# ================= ADD TASK =================
@login_required
def add(request):
    if request.method == 'POST':
        TaskModel.objects.create(
            user=request.user,
            title=request.POST['title'],
            desc=request.POST['desc'],
            user_task_id=get_next_task_id(request.user)
        )
        return redirect("home")

    return render(request, 'add.html')


# ================= COMPLETE PAGE =================
@login_required
def complete(request):
    data = CompleteModel.objects.filter(user=request.user).order_by('user_task_id')
    return render(request, 'complete.html', {'data': data})


# ================= TRASH PAGE =================
@login_required
def trash(request):
    data = TrashModel.objects.filter(user=request.user).order_by('user_task_id')
    return render(request, 'trash.html', {'data': data})


# ================= NOTES =================
@login_required
def notes(request):
    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            Note.objects.create(user=request.user, content=content)
        return redirect('notes')

    notes = Note.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'notes.html', {'notes': notes})


@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)

    if request.method == "POST":
        content = request.POST.get("content")
        if content:
            note.content = content
            note.save()
        return redirect('notes')

    return render(request, 'edit_note.html', {'note': note})


@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.delete()
    return redirect('notes')


# ================= TASK ACTIONS =================
@login_required
def complete_(request, id):
    task = get_object_or_404(TaskModel, id=id, user=request.user)

    CompleteModel.objects.create(
        user=request.user,
        title=task.title,
        desc=task.desc,
        user_task_id=task.user_task_id,
        created_at=task.created_at
    )

    task.delete()
    return redirect('complete')


@login_required
def delete_(request, id):
    task = get_object_or_404(TaskModel, id=id, user=request.user)

    TrashModel.objects.create(
        user=request.user,
        title=task.title,
        desc=task.desc,
        user_task_id=task.user_task_id,
        created_at=task.created_at
    )

    task.delete()
    return redirect('trash')


@login_required
def update(request, id):
    task = get_object_or_404(TaskModel, id=id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST['title']
        task.desc = request.POST['desc']
        task.save()
        return redirect('home')

    return render(request, 'update.html', {'data': task})


# ================= COMPLETE ACTIONS =================
@login_required
def complete_delete(request, id):
    task = get_object_or_404(CompleteModel, id=id, user=request.user)

    TrashModel.objects.create(
        user=request.user,
        title=task.title,
        desc=task.desc,
        user_task_id=task.user_task_id,
        created_at=task.created_at
    )

    task.delete()
    return redirect('trash')


@login_required
def complete_delete_all(request):
    tasks = CompleteModel.objects.filter(user=request.user)

    for task in tasks:
        TrashModel.objects.create(
            user=request.user,
            title=task.title,
            desc=task.desc,
            user_task_id=task.user_task_id,
            created_at=task.created_at
        )

    tasks.delete()
    return redirect('trash')


@login_required
def complete_all(request):
    tasks = TaskModel.objects.filter(user=request.user)

    for task in tasks:
        CompleteModel.objects.create(
            user=request.user,
            title=task.title,
            desc=task.desc,
            user_task_id=task.user_task_id,
            created_at=task.created_at
        )

    tasks.delete()
    return redirect('complete')


# ================= DELETE ALL =================
@login_required
def delete_all(request):
    tasks = TaskModel.objects.filter(user=request.user)

    for task in tasks:
        TrashModel.objects.create(
            user=request.user,
            title=task.title,
            desc=task.desc,
            user_task_id=task.user_task_id,
            created_at=task.created_at
        )

    tasks.delete()
    return redirect('trash')


# ================= RESTORE FROM COMPLETE =================
@login_required
def crestore(request, id):
    task = get_object_or_404(CompleteModel, id=id, user=request.user)

    TaskModel.objects.create(
        user=request.user,
        title=task.title,
        desc=task.desc,
        user_task_id=task.user_task_id,
        created_at=task.created_at
    )

    task.delete()
    return redirect('home')


@login_required
def crestore_all(request):
    tasks = CompleteModel.objects.filter(user=request.user)

    for task in tasks:
        if not TaskModel.objects.filter(
            user=request.user,
            user_task_id=task.user_task_id
        ).exists():

            TaskModel.objects.create(
                user=request.user,
                title=task.title,
                desc=task.desc,
                user_task_id=task.user_task_id,
                created_at=task.created_at
            )

    tasks.delete()
    return redirect('home')


# ================= TRASH ACTIONS =================
@login_required
def trash_delete(request, id):
    task = get_object_or_404(TrashModel, id=id, user=request.user)
    task.delete()
    return redirect('trash')


@login_required
def trash_delete_all(request):
    TrashModel.objects.filter(user=request.user).delete()
    return redirect('trash')


@login_required
def trash_restore(request, id):
    task = get_object_or_404(TrashModel, id=id, user=request.user)

    if not TaskModel.objects.filter(
        user=request.user,
        user_task_id=task.user_task_id
    ).exists():

        TaskModel.objects.create(
            user=request.user,
            title=task.title,
            desc=task.desc,
            user_task_id=task.user_task_id,
            created_at=task.created_at
        )

    task.delete()
    return redirect('home')


@login_required
def trash_restore_all(request):
    tasks = TrashModel.objects.filter(user=request.user)

    for task in tasks:
        if not TaskModel.objects.filter(
            user=request.user,
            user_task_id=task.user_task_id
        ).exists():

            TaskModel.objects.create(
                user=request.user,
                title=task.title,
                desc=task.desc,
                user_task_id=task.user_task_id,
                created_at=task.created_at
            )

    tasks.delete()
    return redirect('home')


# ================= Forget Password =================

def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
            request.session['reset_user'] = username
            return redirect('reset_password')
        else:
            return render(request, 'forgot_password.html', {'error': 'User not found'})

    return render(request, 'forgot_password.html')

def reset_password(request):
    username = request.session.get('reset_user')

    if not username:
        return redirect('forgot_password')

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()

            del request.session['reset_user']
            return redirect('login')
        else:
            return render(request, 'reset_password.html', {'error': 'Passwords do not match'})

    return render(request, 'reset_password.html')