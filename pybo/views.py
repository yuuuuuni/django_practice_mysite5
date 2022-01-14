from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.utils import timezone

from .forms import QuestionForm
from .models import Question


def index(request):
    """
    pybo 질문 목록
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}  # 여기에서 부르는 키는 html에서 쓸 키, 값은 여기의 값
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    pybo 질문 상세
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):  # request에는 사용자가 적은 답변 내용이 넘어옴
    """
    pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question.id)


def question_create(request):
    """
    pybo 질문 등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # 데이터가 들어있는 post 방식의 QuestionForm을 form이라는 변수에 저장
        if form.is_valid():  # QuestionForm이 형식에 맞게 제대로 되어 있다면
            question = form.save(commit=False)  # form을 임시저장해서 question이라는 변수에 넣어라
            question.create_date = timezone.now()  # 그 변수의 작성일시를 현재로 해라
            question.save()  # 저장해라
            return redirect('pybo:index')
    else:  # 방식이 post가 아니면? get이겠지?
        form = QuestionForm()  # 데이터가 없는 빈 폼
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
