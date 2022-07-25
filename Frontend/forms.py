from django import forms
from .models import Members, Competition, Appointment

# 新增最新消息填寫表單

class MembersForm(forms.ModelForm):

    class Meta:
        model = Members
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '標題',
            'content': '內容',
            'type': '類型',
        }

# 新增課程表單

class CompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        
        fields = ('title', 'content', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '課程名稱',
            'content': '課程內容',
            'type': '課程類型',
        }

# 新增校級共用實驗室

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        
        fields = ('title', 'content', 'imageone')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '教室名稱',
            'content': '教室描述',
            'imageone': '教室照片',
        }
