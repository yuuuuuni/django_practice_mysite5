from django import forms
from pybo.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # QuestionForm도 어떤 모델을 기준으로 알려줘야 폼을 만들어 줄 수 있으니!
        fields = ['subject', 'content'] # create_date 속성은 데이터 저장 시점에 자동생성 되므로 등록하지 않음


        # widgets = {  # Meta 클래스의 widgets 속성을 지정하면 부트스트랩 사용 가능
        #    'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #    'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }


        labels = {
            'subject': '제목',
            'content': '내용',
        }
