from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .form import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from .models import Question, Answer


# Create your views here.
def index(request):
    """
    질문목록 조회
    """
    page = request.GET.get('page', '1')
    query = Question.objects.order_by('-created_at')
    paginator = Paginator(query, 10)
    page_obj = paginator.get_page(page)
    context = {'result': page_obj}

    return render(request, 'pybo/question_list.html', context)


def detail(request, id_):
    """
    질문 상세
    """
    question = get_object_or_404(Question, pk=id_)
    result = {"question": question}

    return render(request, "pybo/question_detail.html", result)


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
