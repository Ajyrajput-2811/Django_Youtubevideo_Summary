from django.shortcuts import render ,redirect
from summarizer.models import *
from summarizer.summarize_fun import *
from urllib.parse import urlparse
from urllib.parse import parse_qs
from django.http import JsonResponse,HttpResponse

######## Home Page
def home(request):
    if request.method == "POST":
        youtube_url = request.POST.get('youtube_url')
        video = Video.objects.create(youtube_url=youtube_url)
        try:
            yt = YouTube(youtube_url)
            video.title = yt.title
            video.save()
        except Exception as e:
            print(f"Error retrieving video title: {str(e)}")
        
        url=urlparse(youtube_url)
        video_id = parse_qs(url.query)['v'][0]
        summary = summarize_video(youtube_url,video_id)
        video.summary = summary
        video.save()
        return redirect('summary',pk=video.pk)
    return render(request,'home.html')

############ Summary Page
def summary(request,pk):
    video = Video.objects.get(pk=pk)
    context = {
        "video":video,
    }    
    return render(request,'summary.html',context)


######### Summary API
def get_summary(request):
    try:
        video_summray = Video.objects.all()
        if(request.GET.get('sortby')):
            sortby = request.GET.get('sortby')
            print("sortby is :",sortby)
            if sortby == 'asc':
                video_summray = video_summray.order_by('id')
            elif sortby =="dsc":
                video_summray = video_summray.order_by("-id")
        if(request.GET.get('id')):
            video_id = request.GET.get('id')
            print("video-id:",video_id)
            video_summray = Video.objects.filter(id = video_id)        
                
        payload = []
        for data in video_summray:
              payload.append({
                "id":data.id,
                 "Title":data.title,
                 "Video_url":data.youtube_url,
                 "Transcript":data.summary
            })
        return JsonResponse(payload,safe = False)  


    except Exception as e:
        print(e)
        return JsonResponse({"message":"Something went wrong!"})     





