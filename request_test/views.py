from django.shortcuts import render

def request_info_view(request):
 context = {
 'method': request.method,
 'get_data': request.GET,
 'post_data': request.POST,
 'user': request.user,
 'is_logged_in': request.user.is_authenticated,
 'session_value': request.session.get('demo', '없음'),
 'user_agent': request.META.get('HTTP_USER_AGENT', '알 수 없음'),
 'client_ip': request.META.get('REMOTE_ADDR', '알 수 없음'),
 'path': request.path,
 'full_url': request.build_absolute_uri()
 }
 # 세션에 값 저장
 request.session['demo'] = '세션에서 저장한 값입니다.'
 return render(request, 'request_test/request_info.html', context)

from .models import UploadedFile

def file_upload_view(request):
    uploaded_file_url = None
    title = None

    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']              # request.FILES에서 'file' 키로 추출
        title = request.POST.get('title', '')              # request.POST에서 'title' 키로 추출 (기본값 '')

        uploaded = UploadedFile.objects.create(
            title=title,
            file=uploaded_file
        )
        uploaded_file_url = uploaded.file.url

    return render(request, 'request_test/upload_file.html', {
        'uploaded_file_url': uploaded_file_url,
        'title': title
    })
