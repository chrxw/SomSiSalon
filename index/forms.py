from django import forms


class MailRegisterInformation(forms.Form):
    mail = forms.CharField(label='Email', max_length=100)

    # class Meta:
    #     db_table = "mail_register_for_infomation"
    #     managed = False

    # def __str__(self):
    #     return self.mail
