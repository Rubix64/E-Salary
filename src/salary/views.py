from django.shortcuts import render

from authenticate.models import Employee
import salary
from .models import Salary,Department, Deduction
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

# Create your views here.

@login_required(login_url='signin')
def details(request):
    # emp = request.user.eid
    # salary_list = Salary.objects.filter(eid=request.user) 
    salary_list = Salary.objects.filter(eid=request.user.id)
    deduction_list = Deduction.objects.filter(eid=request.user.id)
    emp_details = User.objects.filter(id=request.user.id)
    emp_details_2 = Employee.objects.get(user=request.user)

    return render(request, "salary/salary_details.html", 
    {
        'salary_list':salary_list,
        'ded_list': deduction_list,
        'emp_details': emp_details,
        'emp_details_2': emp_details_2,

    })

@login_required(login_url='signin')
def accountants(request):
    context={}
    context['employees'] = Employee.objects.all().order_by('user__first_name','user__last_name')
    context['employeeind']=None
    return render(request, 'salary/accountants.html',context)

@login_required(login_url='signin')
def accountantind(request,userid):
    context={
        'errors':[]
    }
    salaryForm=SalaryForm()
    deductionForm=DeductionForm()
    if request.method == 'POST':
        valid=True
        salaryForm=SalaryForm(request.POST)
        if salaryForm.is_valid:
            salaryobj=salaryForm.save(commit=False)
            eidobj=Employee.objects.get(userid=request.POST['eid'])
            salaryobj.eid = eidobj
            numDeductions=int(request.POST['num_deductions'])
            deductionobjs=[]
            totded=0
            for i in range(numDeductions):
                print(f'ded1{i+1}')
                deductionForm=DeductionForm()
                deductionForm.damt=request.POST.get(f'damt{i+1}')
                deductionForm.dcategory=request.POST.get(f'dcategory{i+1}')
                print(request.POST.get(f'damt{i+1}'))
                print(request.POST.get(f'dcategory{i+1}'))
                if valid and deductionForm.is_valid():
                    print(f'ded2{i+1}')
                    deductionobj=deductionForm.save(commit=False)
                    deductionobj.eid=eidobj
                    deductionobj.slipno=salaryobj
                    deductionobjs.append(deductionobj)
                    totded+=deductionobj.damt
                else:
                    context['errors'].append(deductionForm.errors)
                    valid=False
            totsal=salaryobj.basic_salary+salaryobj.hra+salaryobj.conveyance_allowance+salaryobj.medical_allowance+salaryobj.performance_bonus+salaryobj.others
            context['totsal']=totsal
            context['totded']=totded
            context['netsal']=totsal-totded
            if valid and totsal<totded:
                context['errors'].append({'netsal': "Total salary can't be less than total deductions"})
                valid=False
            if valid:
                print('ded3')
                salaryobj.save()
                for deductionobj in deductionobjs:
                    print(deductionobj)
                    deductionobj.save()
                context['success']=True
        else:
            context['errors'].append(salaryForm.errors)
    if len(context['errors'])>0:
        context['iserror']=True
    else:
        context['iserror']=False
    context['employees'] = Employee.objects.all().order_by('user__first_name','user__last_name')
    context['employeeind']= Employee.objects.get(userid=userid)
    return render(request, 'salary/accountants.html',context)