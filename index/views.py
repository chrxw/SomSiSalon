from django.db.models.aggregates import Count, Sum
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.db.models import Max
from django.db import connection

from index.models import *
import json


# Create your views here.

def index(request):
    data = {}
    return render(request, 'index.html', data)


class CustomerList(View):
    def get(self, request):
        customers = list(Customer.objects.all().values())
        data = dict()
        data['customers'] = customers
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class CustomerDetail(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        data = dict()
        data['customers'] = model_to_dict(customer)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class EmployeeList(View):
    def get(self, request):
        employees = list(Employee.objects.all().values())
        data = dict()
        data['employees'] = employees
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class EmployeeDetail(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        data = dict()
        data['employees'] = model_to_dict(employee)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class AboutUsList(View):
    def get(self, request):
        about_us = list(AboutUs.objects.all().values())
        data = dict()
        data['about_us'] = about_us
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class AboutUsDetail(View):
    def get(self, request, pk):
        about_us = get_object_or_404(AboutUs, pk=pk)
        data = dict()
        data['about_us'] = model_to_dict(about_us)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class RewardList(View):
    def get(self, request):
        rewardes = list(Reward.objects.all().values())
        data = dict()
        data['rewardes'] = rewardes
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class RewardDetail(View):
    def get(self, request, pk):
        reward = get_object_or_404(Reward, pk=pk)
        data = dict()
        data['rewardes'] = model_to_dict(reward)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class PaymentMethodList(View):
    def get(self, request):
        payment_methods = list(PaymentMethod.objects.all().values())
        data = dict()
        data['payment_method'] = payment_methods
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class PaymentMethodDetail(View):
    def get(self, request, pk):
        payment_method = get_object_or_404(PaymentMethod, pk=pk)
        data = dict()
        data['payment_method'] = model_to_dict(payment_method)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class ProductList(View):
    def get(self, request):
        products = list(Product.objects.all().values())
        data = dict()
        data['products'] = products
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class ProductDetail(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        data = dict()
        data['products'] = model_to_dict(product)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class ServiceList(View):
    def get(self, request):
        services = list(Service.objects.all().values())
        data = dict()
        data['services'] = services
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class ServiceDetail(View):
    def get(self, request, pk):
        service = get_object_or_404(Service, pk=pk)
        data = dict()
        data['services'] = model_to_dict(service)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class OrderList(View):
    def get(self, request):
        orders = list(Order.objects.all().values())
        data = dict()
        data['orders'] = orders
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class OrderDetail(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        data = dict()
        data['orders'] = model_to_dict(order)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class AppointmentList(View):
    def get(self, request):
        appointments = list(Appointment.objects.all().values())
        data = dict()
        data['appointments'] = appointments
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class AppointmentDetail(View):
    def get(self, request, pk):
        appointment = get_object_or_404(Appointment, pk=pk)
        data = dict()
        data['appointments'] = model_to_dict(appointment)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class ReceiptList(View):
    def get(self, request):
        receipts = list(Receipt.objects.all().values())
        data = dict()
        data['receipts'] = receipts
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class ReceiptDetail(View):
    def get(self, request, pk):
        receipt = get_object_or_404(Receipt, pk=pk)
        data = dict()
        data['receipts'] = model_to_dict(receipt)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class PromotionList(View):
    def get(self, request):
        promotions = list(Promotion.objects.all().values())
        data = dict()
        data['promotions'] = promotions
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class PromotionDetail(View):
    def get(self, request, pk):
        promotion = get_object_or_404(Promotion, pk=pk)
        data = dict()
        data['promotions'] = model_to_dict(promotion)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class NotifiesList(View):
    def get(self, request):
        notifies = list(Notifies.objects.all().values())
        data = dict()
        data['notifies'] = notifies
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class NotifiesDetail(View):
    def get(self, request, pk):
        notifies = get_object_or_404(Notifies, pk=pk)
        data = dict()
        data['notifies'] = model_to_dict(notifies)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class MailList(View):
    def get(self, request):
        mails = list(MailRegisterForInformation.objects.all().values())
        data = dict()
        data['mails'] = mails
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class MailDetail(View):
    def get(self, request, pk):
        mail = get_object_or_404(MailRegisterForInformation, pk=pk)
        data = dict()
        data['mails'] = model_to_dict(mail)
        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response


class MailForm(forms.ModelForm):
    class Meta:
        model = MailRegisterForInformation
        fields = '__all__'


class BestServiceSeller(View):
    def get(self, request):

        appointment = Appointment.objects.order_by(
            'service_id').values('service_id')

        newAppointment = []
        index = 0

        for a in appointment:
            service = Service.objects.values().get(
                service_id=a['service_id'])
            a['service_name'] = service['service_name']
            a['service_cost'] = float(service['service_cost'])
            a['service_img'] = service['service_img']

            if (index == 0):
                newAppointment.append(a)
                newAppointment[-1]['count'] = 1
            else:
                if (appointment[index-1]['service_id'] != a['service_id']):
                    newAppointment.append(a)
                    newAppointment[-1]['count'] = 1
                else:
                    newAppointment[-1]['count'] += 1

            index += 1

        newAppointment = sorted(
            newAppointment, key=lambda x: x['count'], reverse=True)
        appointment_json = json.dumps(newAppointment)

        return HttpResponse(appointment_json, content_type='application/json')


class BestProductSeller(View):
    def get(self, request):

        # with connection.cursor() as cursor:
        #     cursor.execute('SELECT o.prod_qty as "Product quantity", p.prod_id as "Product ID" '
        #                    ' , p.prod_name as "Product Name", p.prod_detail as "Product Detail" '
        #                    ' , p.prod_description as "Product Description", p.prod_review as "Review" '
        #                    ' , p.prod_price as "Product Price" '
        #                    ' FROM "order" o JOIN product p '
        #                    ' ON o.prod_id = p.prod_id')

        #     row = dictfetchall(cursor)
        #     column_name = [col[0] for col in cursor.description]

        # data = dict()
        # data['column_name'] = column_name
        # data['data'] = row

        # response = JsonResponse(data)
        # response["Access-Control-Allow-Origin"] = "*"

        # # return JsonResponse(data)

        # return response
        # return render(request, 'index.html', data)

        order = Order.objects.order_by('prod_id').values('prod_id', 'prod_qty')

        newOrder = []
        index = 0

        for o in order:
            product = Product.objects.values().get(
                prod_id=o['prod_id'])
            o['prod_name'] = product['prod_name']
            o['prod_price'] = float(product['prod_price'])
            o['prod_detail'] = product['prod_detail']
            o['prod_description'] = product['prod_description']
            o['prod_review'] = product['prod_review']
            o['prod_img'] = product['prod_img']

            if (index == 0):
                newOrder.append(o)
            else:
                if (order[index-1]['prod_id'] != o['prod_id']):
                    newOrder.append(o)
                else:
                    newOrder[-1]['prod_qty'] = newOrder[-1]['prod_qty'] + \
                        o['prod_qty']
            index += 1

        newOrder = sorted(newOrder, key=lambda x: x['prod_qty'], reverse=True)
        order_json = json.dumps(newOrder)

        return HttpResponse(order_json, content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class MailRegister(View):

    def post(self, request):
        data = dict()
        request.POST = request.POST.copy()

        form = MailForm(request.POST)
        if form.is_valid():
            mail_register_for_infomation = form.save()

        else:
            data['error'] = 'form not valid!'

        response = JsonResponse(data)
        response["Access-Control-Allow-Origin"] = "*"
        return response
