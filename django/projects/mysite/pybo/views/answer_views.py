from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from ..form import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, id_):
    """
    질문 답변 등록
    """
    question = get_object_or_404(Question, pk=id_)
    if request.method != "POST":
        return HttpResponseNotAllowed('Only POST is possible.')
    else:
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_at = timezone.now()
            answer.question = question
            answer.user = request.user
            answer.save()
            return redirect('pybo:detail', id_=question.id)
        else:
            context = {'question': question, 'form': form}
            return render(request, 'pybo/question_detail.html', context)


@login_required(login_url='common:login')
def answer_update(request, id_):
    answer = get_object_or_404(Answer, pk=id_)
    if request.user != answer.user:
        messages.error(request, "수정권한이 없습니다.")
        return redirect('pybo:detail', id_=answer.question_id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.updated_at = timezone.now()
            answer.save()
            return redirect('pybo:detail', id_=answer.question_id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'pybo/answer_form.html', context)


@login_required(login_url='common:login')
def answer_delete(request, id_):
    answer = get_object_or_404(Answer, pk=id_)
    if request.user != answer.user:
        messages.error(request, '삭제권한이 없습니다.')
    else:
        answer.delete()
    return redirect('pybo:detail', id_=answer.question_id)
