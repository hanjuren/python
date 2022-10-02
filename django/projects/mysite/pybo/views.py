from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .form import QuestionForm

from .models import Question


# Create your views here.
def index(request):
    # 질문 리스트 출력
    query = Question.objects.order_by('-created_at')
    result = {
        'total': len(query),
        'result': query,
    }

    return render(request, 'question_list.html', result)


def detail(request, q_id):
    """
    질문 상세
    """
    question = get_object_or_404(Question, pk=q_id)
    result = {"question": question}

    return render(request, "question_detail.html", result)


def answer_create(request, q_id):
    """
    질문 답변 등록
    """
    question = get_object_or_404(Question, pk=q_id)
    question.answer_set.create(
        content=request.POST.get('content'),
        created_at=timezone.now(),
    )

    return redirect('pybo:detail', q_id=question.id)


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
        return render(request, 'question_form.html', {'form': form})
