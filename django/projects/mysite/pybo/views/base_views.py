from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


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
