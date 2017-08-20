# _*_ coding:utf-8 _*_
# __author__ = 'll'
from users.models import EmailVerifyRecode
from random import Random
from django.core.mail import send_mail

from mx.settings import EMAIL_FROM
# 生成随机字符串

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


# 发送邮箱验证码
def send_register_email(email, send_type="register"):
    email_recode = EmailVerifyRecode()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_recode.code = code
    email_recode.email = email
    email_recode.send_type = send_type
    email_recode.save()

    # 定义邮件内容
    if send_type == "register":
        email_type = u"慕学在线网注册激活链接"
        email_body = u"请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_type, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == "update_email":
        email_title = "慕学在线邮箱修改验证码"
        email_body = "你的邮箱验证码为: {0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass