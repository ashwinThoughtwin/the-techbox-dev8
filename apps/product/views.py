from django.views import View, generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from .models import *
from .forms import EmployeeForm, ItemForm, TeamForm, CatagoryForm, AssignGadgetForm
import datetime
from django.core.paginator import Paginator
from django.core.mail import EmailMessage
from techbox import settings
from django.core.mail import send_mail
from django.db.models import Q
from django.views.decorators.cache import cache_page
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


from django.conf import settings 
from django.http.response import JsonResponse 
from django.views.decorators.csrf import csrf_exempt
import stripe 
stripe.api_key = settings.STRIPE_SECRET_KEY


class HomePageView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context
    
def charge(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        amount = int(request.POST['amount'])
        name = request.POST['uname']
        email = request.POST['email']
        customer = stripe.Customer.create(
            email=email,
            name=name,
            source=request.POST['stripeToken'],
            )
        charge = stripe.Charge.create(
            customer=customer,
            amount=amount*100,
            currency='inr',
            description="pay amount"
        )

        return redirect(reverse('success'))


class SuccessView(TemplateView):

    def get(self, request):
        
        return render(request, 'success.html')
           



# @csrf_exempt
# def stripe_config(request):
#     if request.method == 'GET':
#         stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
#         return JsonResponse(stripe_config, safe=False)

# @csrf_exempt
# def create_checkout_session(request):
#     if request.method == 'GET':
#         domain_url = 'http://localhost:8000/'
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         try:
#             # Create new Checkout Session for the order
#             # Other optional params include:
#             # [billing_address_collection] - to display billing address details on the page
#             # [customer] - if you have an existing Stripe Customer ID
#             # [payment_intent_data] - capture the payment later
#             # [customer_email] - prefill the email input in the form
#             # For full details see https://stripe.com/docs/api/checkout/sessions/create

#             # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
#             checkout_session = stripe.checkout.Session.create(
#                 success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
#                 cancel_url=domain_url + 'cancelled/',
#                 payment_method_types=['card'],
#                 mode='payment',
#                 line_items=[
#                     {
#                         'name': 'charger',
#                         'quantity': 1,
#                         'currency': 'inr',
#                         'amount': '10000',
#                     }
#                 ]
#             )
#             return JsonResponse({'sessionId': checkout_session['id']})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})

# class SuccessView(TemplateView):
#     template_name = 'success.html'


class CancelledView(TemplateView):
    template_name = 'cancelled.html'

# @login_required(login_url="/signin")
# def index(request):

#     context = {}
#     context['segment'] = 'index'

#     html_template = loader.get_template('index.html')
#     return HttpResponse(html_template.render(context, request))

class SearchResultsView(generic.ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name="context1"
    def get_queryset(self):
        query = self.request.GET.get('q') 
        context1 = Employee.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query)
        )
        return context1

class IndexView(SuccessMessageMixin,generic.ListView):
    template_name = "index.html"
    success_message = "login succesfully"
    queryset0 = Employee.objects.all()
    queryset1 = Item.objects.all()
    queryset2 = AssignItem.objects.all()
    queryset = AssignItem.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_employee'] = self.queryset0.all().count()
        context['total_items'] = self.queryset1.all().count()
        context['total_assign_items'] = self.queryset2.all().count()
        context['total_assign_items_list'] = self.queryset.all()

        return context

# @login_required(login_url="/login/")


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


# class Employees(View):
#     def get(self, request):
#         employee = Employee.objects.all()

#         # queryset = Employee.objects.all()
#         return render(request, "employee_list.html", {'context1': employee})


class EmployeesListView(generic.ListView):
    model = Employee
    template_name = 'employee_list.html'  
    context_object_name = 'context1'  
    paginate_by = 2
    queryset = Employee.objects.all()
    



class Gadgets(View):
    def get(self, request):

        gadget = Item.objects.all()
        return render(request, "gadgets_list.html", {'context2': gadget})


class Teams(View):
    def get(self, request):
        team = Team.objects.all()
        return render(request, "team_list.html", {'context3': team})


class Catagorys(View):
    def get(self, request):
        catagory = Catagory.objects.all()
        return render(request, "catagory.html", {'context4': catagory})


class EmployeeDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Employee
    # template_name = "employee_confirm_delete.html"
    success_url = "/employee_list/"
    success_message = "Employee was deleted successfully"



    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)


class GadgetsDeleteView(SuccessMessageMixin,generic.DeleteView):
    model = Item
    # template_name = "gadgets_confirm_delete.html"
    success_url = "/gadgets_list/"
    success_message = "gadgets was deleted successfully"

    def get(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return self.delete(request, *args, **kwargs)

class AssignItemsDeleteView(generic.DeleteView):
    model = AssignItem
    # template_name = "gadgets_confirm_delete.html"
    success_url = "/assign_item_create/"

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class TeamsDeleteView(generic.DeleteView):
    model = Team
    template_name = "team_confirm_delete.html"
    success_url = "/team_list/"


class CategorysDeleteView(generic.DeleteView):
    model = Catagory
    template_name = "catagory_confirm_delete.html"
    success_url = "/catagory/"


class EmployeeUpdateView(generic.UpdateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "employee_update.html"
    success_url = "/employee_list/"


class GadgetsUpdateView(generic.UpdateView):
    form_class = ItemForm
    model = Item
    template_name = "gadgets_update.html"
    success_url = "/gadgets_list/"


class TeamsUpdateView(generic.UpdateView):
    form_class = TeamForm
    model = Team
    template_name = "team_update.html"
    success_url = "/team_list/"


class CatagorysUpdateView(generic.UpdateView):
    form_class = CatagoryForm
    model = Catagory
    template_name = "catagory_update.html"
    success_url = "/catagory/"


class EmployeesCreateView(SuccessMessageMixin,generic.CreateView):
    form_class = EmployeeForm
    model = Employee
    template_name = "employee_create.html"
    success_url = "/employee_list/"
    success_message = "Employee was Created successfully"



class GadgetsCreateView(generic.CreateView):
    form_class = ItemForm
    model = Item
    template_name = "gadgets_create.html"
    success_url = "/gadgets_list/"

class AssignItemsCreateView(View):
    def get(self,request):#show
        form = AssignGadgetForm
        
        queryset=AssignItem.objects.all()
        return render(request,"assign_item_create.html",{'form':form,'queryset':queryset})
    def post(self,request,*args, **kwargs):#submit
        # import pdb; pdb.set_trace()
        form = AssignGadgetForm(request.POST or None)
        eid = request.POST['employee']
        recipient = Employee.objects.get(id=eid)
        print(recipient.email)
        # print(request.POS)
        if form.is_valid():
            employee = form.cleaned_data['employee']
            gadget = form.cleaned_data['item']
            # status = form.cleaned_data['status']
            # a = datetime.datetime.now()
            # date_data = int(a.strftime('%d'))+5
            # submit_date = datetime.datetime(a.year, a.month, date_data)
            # employee = str(employee)
            # item = str(gadget)

            form.save()
            subject = 'Requesting for'
            message = 'Hi We providing you '+ str(gadget)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [recipient.email]
            email = EmailMessage(subject, message, email_from, recipient_list)
            email.send(fail_silently=False)
            # tool_issue = AssignItem.objects.create(
            # employee=employee, item=gadget, submit_date=submit_date,status=status)
        return HttpResponseRedirect("/assign_item_create/")


# class AssignItemsView(View):
#     def get(self, request):
#         assign = AssignItem.objects.all()
#         emp = Employee.objects.all()
#         item = Item.objects.all()
#         return render(request, "assign_item.html", {'emp_data': emp, 'item_data': item, 'context5': assign})

#     def post(self, request, *args, **kwargs):
#         print(request.POST)
#         emp_id = request.POST.get('emp_id')
#         item_id = request.POST.get('item_id')
#         employee = Employee.objects.get(id=int(emp_id))
#         item = Item.objects.get(id=int(item_id))
#         a = datetime.datetime.now()
#         date_data = int(a.strftime('%d'))+5
#         submit_date = datetime.datetime(a.year, a.month, date_data)
#         tool_issue = AssignItem.objects.create(
#             employee=employee, item=item, submit_date=submit_date)

#         assign_items = AssignItem.objects.all()
#         emp = Employee.objects.all()
#         item = Item.objects.all()
#         return render(request, "assign_item.html", {'emp_data': emp, 'item_data': item, 'context5': assign_items})


