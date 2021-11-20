from django.db import models

# Create your models here.


class Data(models.Model):
    key = models.CharField(max_length=10, primary_key=True)
    value = models.CharField(max_length=100)


class Customer(models.Model):
    cus_id = models.CharField(max_length=10, primary_key=True)
    cus_name = models.CharField(max_length=100)
    cus_gender = models.CharField(max_length=10)
    cus_contact = models.CharField(max_length=10)
    cus_address = models.CharField(max_length=200)
    cus_birth = models.DateField(null=True, blank=True)
    cus_reward = models.CharField(max_length=10)
    somsi_coin = models.IntegerField(null=True)

    class Meta:
        db_table = "customer"
        managed = False

    def __str__(self):
        return self.cus_id


class Employee(models.Model):
    emp_id = models.CharField(max_length=10, primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_gender = models.CharField(max_length=10)
    emp_contact = models.CharField(max_length=10)
    emp_address = models.CharField(max_length=200)
    emp_position = models.CharField(max_length=100)
    emp_salary = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "employee"
        managed = False

    def __str__(self):
        return self.emp_id


class AboutUs(models.Model):
    branch_code = models.CharField(max_length=10, primary_key=True)
    branch_detail = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "aboutus"
        managed = False

    def __str__(self):
        return self.branch_code


class Reward(models.Model):
    reward = models.CharField(max_length=10, primary_key=True)
    rew_level = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = "reward"
        managed = False

    def __str__(self):
        return self.reward


class PaymentMethod(models.Model):
    payment_code = models.CharField(max_length=10, primary_key=True)
    description = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = "payment_method"
        managed = False

    def __str__(self):
        return self.payment_code


class Product(models.Model):
    prod_id = models.CharField(max_length=10, primary_key=True)
    prod_name = models.CharField(max_length=100)
    prod_cost = models.FloatField(null=True, blank=True)
    prod_price = models.FloatField(null=True, blank=True)
    prod_qty_stock = models.IntegerField(null=True)
    prod_date = models.DateField(null=True, blank=True)
    prod_detail = models.JSONField(encoder=None, decoder=None)
    prod_description = models.JSONField(encoder=None, decoder=None)
    prod_review = models.JSONField(encoder=None, decoder=None)
    prod_img = models.CharField(max_length=2000)

    class Meta:
        db_table = "product"
        managed = False

    def __str__(self):
        return self.prod_id


class Service(models.Model):
    service_id = models.CharField(max_length=10, primary_key=True)
    service_name = models.CharField(max_length=100)
    service_cost = models.FloatField(null=True, blank=True)
    service_img = models.CharField(max_length=2000)

    class Meta:
        db_table = "service"
        managed = False

    def __str__(self):
        return self.prod_id


class Order(models.Model):
    order_no = models.CharField(max_length=10, primary_key=True)
    prod_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='prod_id')
    prod_qty = models.IntegerField()
    prod_price = models.FloatField(null=True, blank=True)
    order_date = models.DateField(null=True, blank=True)
    ship_date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = "order"
        unique_together = (("order_no", "prod_id"),)
        managed = False

    def __str__(self):
        return '{"order_no":"%s","prod_id":"%s","prod_qty":"%s","prod_price":%s,"order_date":"%s","ship_date":"%s"}' % (self.order_no, self.prod_id, self.prod_qty, self.prod_price, self.order_date, self.ship_date)


class Appointment(models.Model):
    appo_id = models.CharField(max_length=10, primary_key=True)
    cus_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, db_column='cus_id')
    emp_id = models.ForeignKey(
        Employee, on_delete=models.CASCADE, db_column='emp_id')
    appo_date = models.DateField(null=True, blank=True)
    appo_time = models.DateField()
    service_id = models.ForeignKey(
        Service, on_delete=models.CASCADE, db_column='service_id')

    class Meta:
        db_table = "appointment"
        unique_together = (("appo_id", "cus_id"),)
        managed = False

    def __str__(self):
        return '{"appo_id":"%s","cus_id":"%s","emp_id":"%s","appo_date":%s,"appo_time":"%s","service_id":"%s"}' % (self.appo_id, self.cus_id, self.emp_id, self.appo_date, self.appo_time, self.service_id)


class Receipt(models.Model):
    receipt_id = models.CharField(max_length=10, primary_key=True)
    cus_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, db_column='cus_id')
    payment_code = models.ForeignKey(
        PaymentMethod, on_delete=models.CASCADE, db_column='payment_code')
    receipt_date = models.DateField(null=True, blank=True)
    total_price = models.FloatField(null=True)
    service_id = models.ForeignKey(
        Service, on_delete=models.CASCADE, db_column='service_id')
    order_no = models.ForeignKey(
        Order, on_delete=models.CASCADE, db_column='order_no')

    class Meta:
        db_table = "receipt"
        unique_together = (("receipt_id", "cus_id"),)
        managed = False

    def __str__(self):
        return '{"receipt_id":"%s","cus_id":"%s","payment_code":"%s","receipt_date":%s,"total_price":"%s","service_id":"%s","order_no":"%s"}' % (self.receipt_id, self.cus_id, self.payment_code, self.receipt_date, self.total_price, self.service_id, self.order_no)


class Promotion(models.Model):
    promo_id = models.CharField(max_length=10, primary_key=True)
    service_id = models.ForeignKey(
        Service, on_delete=models.CASCADE, db_column='service_id')
    prod_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, db_column='prod_id')
    noti_promo = models.CharField(max_length=100)

    class Meta:
        db_table = "promotion"
        unique_together = (("promo_id", "service_id", "prod_id"),)
        managed = False

    def __str__(self):
        return '{"promo_id":"%s","service_id":"%s","prod_id":"%s","noti_promo":%s}' % (self.promo_id, self.service_id, self.prod_id, self.noti_promo)


class Notifies(models.Model):
    cus_id = models.ForeignKey(
        Customer, on_delete=models.CASCADE, db_column='cus_id')
    noti_course = models.CharField(max_length=100)

    class Meta:
        db_table = "notifies"
        managed = False

    def __str__(self):
        return self.cus_id
