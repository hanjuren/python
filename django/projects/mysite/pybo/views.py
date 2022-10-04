from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .form import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from .models import Question


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
            answer.save()
            return redirect('pybo:detail', id_=question.id)
        else:
            context = {'question': question, 'form': form}
            return render(request, 'pybo/question_detail.html', context)


def question_create(request):
    """
    질문 등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_at = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})
