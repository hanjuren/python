from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ..form import QuestionForm, AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def question_create(request):
    """
    질문 등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_at = timezone.now()
            question.user_id = request.user.id
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})


@login_required(login_url='common:login')
def question_update(request, id_):
    """
    질문 수정
    """
    question = get_object_or_404(Question, pk=id_)
    if request.user != question.user:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pybo:detail', id_=question.id)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.updated_at = timezone.now()
            question.save()
            return redirect('pybo:detail', id_=question.id)
    else:
        form = QuestionForm(instance=question)
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, id_):
    """
    질문 삭제
    """
    question = get_object_or_404(Question, pk=id_)
    if request.user != question.user:
        messages.error(request, "삭제 권한이 없습니다.")
        return redirect('pybo:detail', id_=question.id)
    question.delete()
    return redirect('pybo:index')
