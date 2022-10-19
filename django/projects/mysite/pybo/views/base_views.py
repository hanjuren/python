from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question


def index(request):
    """
    질문목록 조회
    """
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')

    query = Question.objects.order_by('-created_at')

    if kw:
        query = query.filter(
            Q(subject__icontains=kw) |
            Q(content__icontains=kw) |
            Q(answer__content__icontains=kw) |
            Q(user__username__icontains=kw) |
            Q(answer__user__username__icontains=kw)
        ).distinct()

    paginator = Paginator(query, 10)
    page_obj = paginator.get_page(page)
    context = {'result': page_obj, 'page': page, 'kw': kw}

    return render(request, 'pybo/question_list.html', context)


def detail(request, id_):
    """
    질문 상세
    """
    question = get_object_or_404(Question, pk=id_)
    result = {"question": question}

    return render(request, "pybo/question_detail.html", result)
