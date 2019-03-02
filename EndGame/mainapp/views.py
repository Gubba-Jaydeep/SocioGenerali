from django.shortcuts import render
from django.template import loader
from .models import AdvisorDatabase, CustomerDatabase
from django.http import HttpResponseRedirect
from selenium import webdriver
from PIL import Image
# Create your views here.

def index(request):
    if request.COOKIES.get("loggedIn",None):
        db = AdvisorDatabase()
        email=request.COOKIES.get("userName")
        user = db.getDataFromEmail(email)
        return render(request, 'mainapp/home.html', {'user': user})
    return render(request, 'mainapp/login.html', {})

def login(request):
    '''retrieving data from form and validation and redirection to dashboard page'''
    db = AdvisorDatabase()
    dict_of_officials = db.getData()
    uname = request.GET['username']
    psw = request.GET['pass']
    try:
        if dict_of_officials[uname] == psw:
            user = db.getDataFromEmail(uname)
            response=render(request, 'mainapp/home.html', {'user': user})
            response.set_cookie("loggedIn",True)
            response.set_cookie("userName", uname)
            return response
        else:
            return render(request, 'mainapp/index.html', {})
    except Exception as ae:
        ctx = {'ae': ae}
        return render(request, 'mainapp/error.html', ctx)

def dashboard(request):

    '''with open("./mklog.txt","wt") as f:
        f.write(str(request))'''
    if request.COOKIES.get("loggedIn",None):
        db = AdvisorDatabase()
        email=request.COOKIES.get("userName")
        user = db.getDataFromEmail(email)
        return render(request, 'mainapp/home.html', {'user': user})
    else:
        return render(request, 'mainapp/login.html', {})

def logout(request):
    if request.COOKIES.get("loggedIn"):
        response = render(request,'mainapp/login.html',{})
        response.delete_cookie("userName")
        response.delete_cookie("loggedIn")
        return response
    else:
        render(request, 'mainapp/error.html', {})

def myCustomers(request):
    if request.COOKIES.get("loggedIn"):
        db = CustomerDatabase()
        customers= db.getData()[:10]
        return render(request, 'mainapp/customers.html' ,{'customers' : customers})
    else:
        return render(request, 'mainapp/login.html', {})

def customerDetail(request, pk):
    db = CustomerDatabase()
    customer = db.getDataFromPk(int(pk))
    return render(request,'mainapp/showdetails.html',{'customer' : customer})

def searchDetails(request):
    if request.COOKIES.get("loggedIn"):
        return render(request, 'mainapp/searchdetails.html',{})
    else:
        return render(request, 'mainapp/login.html', {})

def sendEmail(request):
    return HttpResponseRedirect("https://mail.google.com/mail/?view=cm&fs=1&to=neotrix1111@gmail.com&su=SUBJECT&body=BODY&bcc=someone.else@example.com")


def grabPhoto(request):
    links = request.GET['photoLinks']
    links = links.split(",")
    index=0
    driver = webdriver.Chrome(executable_path='D:/chromedriver.exe')
    for link in links:
        driver.get(link)
        ss = driver.save_screenshot('ss'+str(index)+'.png')
        index+=1
    driver.quit()
    #all photos are stored in mainapp level
    for x in range(index):
        if '/public/' in links[x]:
            img_obj=Image.open('ss'+str(x)+'.png')
            crop_img=img_obj.crop((211, 315, 295, 395))
            crop_img.save('ss'+str(x)+'.png')
        else:
            img_obj = Image.open('ss' + str(x) + '.png')
            crop_img = img_obj.crop((101, 257, 265, 420))
            crop_img.save('ss' + str(x) + '.png')
    #harsha has to write code for comparing the photos
    # srcImage = Image.open('src.png')
    # srcImage = srcImage.resize((400, 400) ,Image.ANTIALIAS)
    di={}
    # for x in range(index):
    #     desImg = Image.open('ss' + str(x) + '.png')
    #     desImg = desImg.resize((400, 400) ,Image.ANTIALIAS)
    #
    #     assert srcImage.mode == desImg.mode, "different kinds of images"
    #     assert srcImage.size == desImg.size, "different sizes"
    #
    #     pairs = zip(srcImage.getdata(), desImg.getdata())
    #     dif=0
    #     if len(srcImage.getbands()) == 1:
    #         #for gray-scale jpegs
    #         dif=sum(abs(p1-p2) for p1,p2 in pairs)
    #     else:
    #         dif=sum(abs(c1-c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))
    #     noComponents = srcImage.size[0] * srcImage.size[1] * 3
    #     di[str((dif/255.0 *100)/noComponents)]="<a href='"+links[x]+"'> JD </a>"

    img1='src.png'
    for x in range(index):
        img2 = 'ss' + str(x) + '.png'
        ans = faceVerify(img1,img2)
        di[links[x]]=ans


    return render(request,'mainapp/screenShotDone.html',{'di':di})

def getFaceId(path):
    import requests

    # Replace 'KEY_1' with your subscription key as a string
    subscription_key = 'a8304edad2824566a6ed18bd6b6a34b4'
    filename = path

    uri_base = 'https://westcentralus.api.cognitive.microsoft.com'
    # Request headers
    # for locally stored image files use
    # 'Content-Type': 'application/octet-stream'
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    params = {
        'returnFaceId': 'true',
        'returnFaceAttributes': 'smile',
    }
    # route to the face api
    path_to_face_api = '/face/v1.0/detect'
    # open jpg file as binary file data for intake by the MCS api
    with open(filename, 'rb') as f:
        img_data = f.read()
    try:

        response = requests.post(uri_base + path_to_face_api,
                                 data=img_data,
                                 headers=headers,
                                 params=params)

        print('Response:')
        # json() is a method from the request library that converts
        # the json reponse to a python friendly data structure
        parsed = response.json()

        # display the image analysis data
        return parsed[0]['faceId']


    except Exception as e:
        print('Error:')
        print(e)
        return None

def faceVerify(im1,im2):
    import requests

    # Replace 'KEY_1' with your subscription key as a string
    subscription_key = 'a8304edad2824566a6ed18bd6b6a34b4'
    #filename = path
    # Replace or verify the region.
    #
    # You must use the same region in your REST API call as you used to obtain your subscription keys.
    # For example, if you obtained your subscription keys from the westus region, replace
    # "westcentralus" in the URI below with "westus".
    #
    # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
    # a free trial subscription key, you should not need to change this region.
    uri_base = 'https://westcentralus.api.cognitive.microsoft.com'
    # Request headers
    # for locally stored image files use
    # 'Content-Type': 'application/octet-stream'
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }
    # Request parameters
    # The detection options for MCS Face API check MCS face api
    # documentation for complete list of features available for
    # detection in an image
    # these parameters tell the api I want to detect a face and a smile
    params = {
        'faceid1':getFaceId(im1),
        'faceid2':getFaceId(im2)
    }
    #print(params)
    # route to the face api
    path_to_face_api = '/face/v1.0/verify'
    # open jpg file as binary file data for intake by the MCS api
    import json
    body1=json.dumps(params)
    try:
        # Execute the api call as a POST request.
        # What's happening?: You're sending the data, headers and
        # parameter to the api route & saving the
        # mcs server's response to a variable.
        # Note: mcs face api only returns 1 analysis at time
        response = requests.post(uri_base + path_to_face_api,
                                 headers=headers,
                                 data=body1)

        #print('Response:')
        # json() is a method from the request library that converts
        # the json reponse to a python friendly data structure
        faces=response.json()

        # display the image analysis data
        return faces['confidence']


    except Exception as e:
        print('Error:')
        print(e)
        return None




