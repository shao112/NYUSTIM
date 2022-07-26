from django import forms
from .models import Members, Competition, Appointment, Events

# 成員表單

class MembersForm(forms.ModelForm):

    class Meta:
        model = Members
        
        fields = ('name', 'description', 'grade', 'thumb', 'position')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'grade': forms.TextInput(attrs={'class': 'form-control'}),
            'thumb': forms.NumberInput(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '姓名',
            'description': '成員介紹',
            'grade': '級次',
            'thumb': '按讚次數',
            'position': '位置',
        }

# 賽事表單

class CompetitionForm(forms.ModelForm):

    class Meta:
        model = Competition
        
        fields = ('title', 'content', 'editor', 'type')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'editor': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'title': '標題',
            'content': '內容',
            'editor': '編輯者',
            'type': '報導類別',
        }

# 活動公告表單

class EventForm(forms.ModelForm):

    class Meta:
        model = Events
        
        fields = ('type', 'content')

        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'type': '類別',
            'content': '內容',
        }

# 預約友誼賽表單

class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        
        fields = ('name', 'department', 'date', 'time', 'email', 'msg')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.TextInput(attrs={'class': 'form-control'}),
            'time': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'msg': forms.TextInput(attrs={'class': 'form-control'}),
        }

        #預設會是顯示英文欄位，可用labels改成對應中文欄位
        labels = {
            'name': '稱謂',
            'department': '系級',
            'date': '預約日期',
            'time': '預約時間',
            'email': '電子信箱',
            'msg': '留言',
        }
