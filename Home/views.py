from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

def home(request):
    return render(request, 'index.html')

def staff_augmentation(request):
    return render(request, 'staff_augmentation.html')


def development_services(request):
    return render(request, 'development_services.html')

def it_infrastructure_services(request):
    return render(request, 'it_infrastructure_services.html')

def design_services(request):
    return render(request, 'design_services.html')

def managed_cloud_services(request):
    return render(request, 'managed_cloud_services.html')

def digital_marketing_services(request):
    return render(request, 'digital_marketing_services.html')



def send_email(data, subject, fields):
    try:
        rows = "".join(f"""
        <tr>
            <td>{field}</td>
            <td>{data.get(key, 'None')}</td>
        </tr>
        """ for field, key in fields.items())

        message = f"""
        <html>
        <head>
            <style>
                table {{
                    font-family: Arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%;
                }}
                th, td {{
                    border: 1px solid #dddddd;
                    text-align: left;
                    padding: 8px;
                }}
                th {{
                    background-color: #f2f2f2;
                }}
                tr:nth-child(even) {{
                    background-color: #f9f9f9;
                }}
            </style>
        </head>
        <body>
            <h2>{subject}</h2>
            <table>
                <tr>
                    <th>Field</th>
                    <th>Value</th>
                </tr>
                {rows}
            </table>
        </body>
        </html>
        """

        from_email = settings.EMAIL_HOST_USER
        recipient_list = [settings.EMAIL_HOST_USER]
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.content_subtype = "html"
        email.send()

        return JsonResponse({"message": "Form submitted successfully and email sent!"}, status=200)
    except Exception as e:
        print(f"Error while sending email: {e}")
        return JsonResponse({"error": str(e)}, status=500)


@csrf_protect
def contact_form(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "subject": request.POST.get("subject"),
            "message": request.POST.get("message"),
        }

        fields = {
            "Name": "name",
            "Email": "email",
            "Subject": "subject",
            "Message": "message",
        }

        return send_email(data, "New Contact Form Submission", fields)

    return JsonResponse({"error": "Invalid request"}, status=400)