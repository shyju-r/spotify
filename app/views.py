from django.shortcuts import render,redirect,get_object_or_404
from app.forms import SignupForm,ForgetpassForm,SongForm,SongupdateForm,subcategoryForm,CategoryForm
from app.models import Signupmodel,Songmodel,Subcategorymodel,CategoryModel

# Create your views here.

                    #    login page
                      
                      
def login(request):
    if request.method=="POST":
        print(request.POST)
        if Signupmodel.objects.filter(email=request.POST['logemail']).exists():
            sig=Signupmodel.objects.get(email=request.POST['logemail'])
            if sig.password==request.POST['logpass']:
                return redirect('subcateview')
    return render(request,'login.html')                      
                      
                      
def signup(request):
    print(request.POST)
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
           return render(request,"signup.html")       
    return render(request,"signup.html")



def forgotpassword(request):
    if request.method == "POST":
        print(request.POST)
        if Signupmodel.objects.filter(email=request.POST['email']).exists:
            data=Signupmodel.objects.get(email=request.POST['email'])
            return redirect(f'/passwordupdate/{data.id}')

    return render(request,"forgotpassword.html")


def passwordupdate(request,id):
    data=Signupmodel.objects.get(id=id)
    if request.method =="POST":
        form=ForgetpassForm(request.POST,instance=data)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=ForgetpassForm(instance=data)
    return render(request,"passwordupdate.html",{"data":data,"form":form})


                        #  index category


def Category(request):
    if request.method == "POST":
        print(request.POST)
        form=CategoryForm(request.POST)       
        if form.is_valid():
            form.save()
            return redirect('subcateview')
        else:
            return render(request,'category.html')
    return render(request,'category.html')





                #  subcategory views


def Subcategorydata(request):
    if request.method == "POST":
        print(request.POST,request.FILES)
        category=CategoryModel.objects.get(category_name=request.POST["category_name"])
        Subcategorymodel.objects.create(
            category=category,
            category_name=request.POST["category_name"],
            playlistimage=request.FILES["playlistimage"],
            playlistname=request.POST["playlistname"],
            playlistartists=request.POST["playlistartists"],
            
        )
        return redirect('subcateview')
    return render(request,'subcatedata.html')


def subcateupdate(request,id):
    data=get_object_or_404(Subcategorymodel,id=id)
    print(data)
    if request.method == "POST":
        data.category_name= request.POST.get("category_name",data.category_name)
        if "playlistimage" in request.FILES:
            data.playlistimage = request.FILES["playlistimage"]
        data.playlistname = request.POST.get("playlistname",data.playlistname)
        data.playlistartists = request.POST.get("playlistartists",data.playlistartists)
        data.save()
        return redirect('subcateview')
    return render(request, 'subcateupdate.html', {"data": data})    


def subcateview(request):
    data=Subcategorymodel.objects.all()
    return render(request,"index.html",{"data":data})







                            #  song datas




def songdata(request):
    if  request.method == "POST":
        print(request.POST,request.FILES)
        playlist=Subcategorymodel.objects.get(playlistname=request.POST["playlistname"])
        Songmodel.objects.create(
            palylist=playlist,
            playlistname=request.POST["playlistname"],
            number=request.POST["number"],
            songimage=request.FILES["songimage"],
            songname=request.POST["songname"],
            songartist=request.POST["songartist"],
            moviename=request.POST["moviename"],
            plays=request.POST["plays"],
            duration=request.POST["duration"],
            song=request.FILES["song"],
        )     
        print("save")
        return redirect('subcateview')
    return render(request,'songdata.html')

# def songlist(request):
#     return render(request,'songlist.html')

def songdetail(request, id):
    data = Subcategorymodel.objects.get(id=id)
    songdata=Songmodel.objects.filter(palylist_id=id)
    print(songdata)
    return render(request, "songlist.html", {"data": data ,"songdata":songdata})

def songdataupdate(request, id):
    data = get_object_or_404(Songmodel, id=id)
    print(data)
    if request.method == "POST":
        data.playlistname = request.POST.get("playlistname", data.playlistname)
        data.number = request.POST.get("number", data.number)
        if "songimage" in request.FILES:
            data.songimage = request.FILES["songimage"]
            data.songname = request.POST.get("songname", data.songname)
            data.songartist = request.POST.get("songartist", data.songartist)
            data.moviename = request.POST.get("moviename", data.moviename)
            data.plays = request.POST.get("plays", data.plays)
            data.duration = request.POST.get("duration", data.duration)
        if "song" in request.FILES:
            data.song = request.FILES["song"]
        data.save()        
        return redirect('subcateview')
    return render(request, 'songdata.html', {"data": data})


def songpageview(request,id):
    data=Songmodel.objects.get(id=id)
    return render(request,"songpage.html",{"data":data})




# def songdataview(request):
#     data=Songmodel.objects.all()
#     return render(request,'songlist.html',{"data":data})








