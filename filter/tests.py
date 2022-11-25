from django.test import TestCase

# 게시글 수정하기 - media 파일 동시 삭제 예제
# def notice_edit_view(request, pk):
#     notice = Notice.objects.get(id=pk)
#     if request.method == "POST":
#         if(notice.writer == request.user or request.user.level == '0'):
#             file_change_check = request.POST.get('fileChange', False)
#             file_check = request.POST.get('upload_files-clear', False)

#             if file_check or file_change_check:
#                 os.remove(os.path.join(settings.MEDIA_ROOT, notice.upload_files.path))

#             form = NoticeWriteForm(request.POST, request.FILES, instance=notice)
#             if form.is_valid():
#                 notice = form.save(commit = False)
#                 if request.FILES:
#                     if 'upload_files' in request.FILES.keys():
#                         notice.filename = request.FILES['upload_files'].name
#                 notice.save()
#                 messages.success(request, "수정되었습니다.")
#                 return redirect('/notice/'+str(pk))
#     else:
#         notice = Notice.objects.get(id=pk)
#         if notice.writer == request.user or request.user.level == '0':
#             form = NoticeWriteForm(instance=notice)
#             context = {
#                 'form': form,
#                 'edit': '수정하기',
#             }
#             if notice.filename and notice.upload_files:
#                 context['filename'] = notice.filename
#                 context['file_url'] = notice.upload_files.url
#             return render(request, "notice/notice_write.html", context)
#         else:
#             messages.error(request, "본인 게시글이 아닙니다.")
#             return redirect('/notice/'+str(pk))