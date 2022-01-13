from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from pybo.models import Question


def index(request):
    """
    pybo 질문 목록
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list} # 여기에서 부르는 키는 html에서 쓸 키, 값은 여기의 값
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 질문 상세
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id): # request에는 사용자가 적은 답변 내용이 넘어옴
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)