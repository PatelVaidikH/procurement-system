from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import logout, authenticate, login
import uuid
import hashlib 
from django.db.models import Q
from django.http import HttpResponse
from django.template import loader
from .helper import send_reset_password,send_room_add 

# Create your views here.


def home(request):
    global pay,uses,namel,chatroomval
    pay = ""
    uses = ""
    namel = ""
    chatroomval = "0"
    if user_login:

        ufname = UserMaster.objects.filter(username=username).values()
        ufshow = ufname[0]["user_full_name"]
        if user_data_type == "1":
                room_access = RoomDetail.objects.filter(user_id_id=user_id).values('chat_room_id_id')
                room_access_list = list(room_access)
                roomaccess = []
                roomid =[]
                a = ['id']
                b = []
                c = ['name']
                d = []
                dz = []
                blist = []
                for id_list in room_access_list:
                    roomid.append(id_list['chat_room_id_id'])
                    b.append(id_list['chat_room_id_id'])
                    dzid = dict(zip(a,b))
                    # print(dzid)
                    blist.append(dzid)
                    b.remove(id_list['chat_room_id_id'])
                # print("blist  ",blist)

                l = len(roomid)
                for i in range(0,l):
                    idi = roomid[i]
                    room_name = RoomMaster.objects.filter(chat_room_id = idi).values('chat_room_name')
                    room_name = list(room_name)
                    roomaccess.append(room_name[0]['chat_room_name'])
                    blist[i]['name'] = room_name[0]['chat_room_name']

                    room_last = RoomMaster.objects.filter(chat_room_id = idi).values('last_message')
                    room_last = list(room_last)
                    blist[i]['last_message'] = room_last[0]['last_message']
                    
                    room_named = RoomMaster.objects.filter(chat_room_id = idi).values('date_creation')
                    room_named = list(room_named)
                    blist[i]['date_creation'] = room_named[0]['date_creation']
                contexta = {
                "showname":ufshow,
                "rooms":blist,
                            }
                return render(request,'home.html',contexta) 
        else:
            if user_data_type == "2":
                # print("emp home")
                room_access = RoomDetail.objects.filter(user_id_id=user_id).values('chat_room_id_id')
                room_access_list = list(room_access)
                roomaccess = []
                roomid =[]
                a = ['id']
                b = []
                c = ['name']
                d = []
                dz = []
                blist = []
                for id_list in room_access_list:
                    roomid.append(id_list['chat_room_id_id'])
                    b.append(id_list['chat_room_id_id'])
                    dzid = dict(zip(a,b))
                    # print(dzid)
                    blist.append(dzid)
                    b.remove(id_list['chat_room_id_id'])
                # print("blist  ",blist)

                l = len(roomid)
                for i in range(0,l):
                    idi = roomid[i]
                    room_name = RoomMaster.objects.filter(chat_room_id = idi).values('chat_room_name')
                    room_name = list(room_name)
                    roomaccess.append(room_name[0]['chat_room_name'])
                    blist[i]['name'] = room_name[0]['chat_room_name']

                    room_last = RoomMaster.objects.filter(chat_room_id = idi).values('last_message')
                    room_last = list(room_last)
                    blist[i]['last_message'] = room_last[0]['last_message']
                    
                    room_named = RoomMaster.objects.filter(chat_room_id = idi).values('date_creation')
                    room_named = list(room_named)
                    blist[i]['date_creation'] = room_named[0]['date_creation']
                contexte = {
                "showname":ufshow,
                "rooms":blist,
            }
                return render(request,"employe-home.html",contexte)
            elif user_data_type == "3":
                room_access = RoomDetail.objects.filter(user_id_id=user_id).values('chat_room_id_id')
                room_access_list = list(room_access)
                roomaccess = []
                roomid =[]
                a = ['id']
                b = []
                c = ['name']
                d = []
                dz = []
                blist = []
                for id_list in room_access_list:
                    roomid.append(id_list['chat_room_id_id'])
                    b.append(id_list['chat_room_id_id'])
                    dzid = dict(zip(a,b))
                    # print(dzid)
                    blist.append(dzid)
                    b.remove(id_list['chat_room_id_id'])
                # print("blist  ",blist)

                l = len(roomid)
                for i in range(0,l):
                    idi = roomid[i]
                    room_name = RoomMaster.objects.filter(chat_room_id = idi).values('chat_room_name')
                    room_name = list(room_name)
                    roomaccess.append(room_name[0]['chat_room_name'])
                    blist[i]['name'] = room_name[0]['chat_room_name']

                    room_last = RoomMaster.objects.filter(chat_room_id = idi).values('last_message')
                    room_last = list(room_last)
                    blist[i]['last_message'] = room_last[0]['last_message']
                    
                    room_named = RoomMaster.objects.filter(chat_room_id = idi).values('date_creation')
                    room_named = list(room_named)
                    blist[i]['date_creation'] = room_named[0]['date_creation']
                contextc = {
                "showname":ufshow,
                "rooms":blist,
            }
                return render(request,"client-home.html",contextc)
    else:
        return render(request, "home.html")

def hash_password(password):
   # uuid is used to generate a random number of the specified password
   salt = uuid.uuid4().hex
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

def loginUser(request):
    global user_data_type,user_login,username,userl,namerc,rid,user_id
    user_login=False

    if request.method == 'POST': 
        username = request.POST['username']
        pass1 = request.POST['pass1'] 

        userM = UserMaster.objects.values_list('username')
        uM = []
        lis = list(userM)
        for i in lis:
            uM.append(i[0])
        # print(uM)


        userA = User.objects.values_list('username')
        uA = []
        lis = list(userA)
        for i in lis:
            uA.append(i[0])
        # print(uA)
        
        if username in uA:
            # print("yes auth")
            user = authenticate(username=username, password=pass1)
            p=str(user)
            # print(p in uA)
            login(request, user)
            
            return redirect("/admin") 
            

        elif username in uM:
            namerc = ""
            rid = '0'
            # print("yes master")
            #userl = True
            data = UserMaster.objects.filter(username__contains=username).values()
            user_data_type = data[0]['user_type']
            user_id = data[0]['user_id']
            # print(user_id)
            # print('user_id')
            hash = data[0]['password']
            # print(hash) 

            if check_password(hash, pass1):
                # print('You entered the right password')
                userl = username
                user_login = True
                request.session.set_test_cookie()
                
                #user = authenticate(username=username, password=pass1)
                #userauthenticated = True
                if data[0]['user_type'] == "1":
                    return redirect("/home")
                elif data[0]['user_type'] == "2":
                    return redirect("/home")
                elif data[0]['user_type'] == "3":
                    return redirect("/home")
                
                return redirect("/home")
            else:
                messages.error(request, 'Username and passsword did not match')
                return render(request, "login.html")
            
        else:
            messages.error(request, 'Username not found')
            return render(request, "login.html")
            
    return render(request, "login.html") 

def resetpass(request,token):
    
    profile_obj = UserMaster.objects.get(token = token)
    p = profile_obj.username
    context = {
            "name":p,
    }

    if request.method == 'POST':
        user_n = request.POST['username']
        new_pass = request.POST['newpass1']
        new_cpass = request.POST['newpass2']

        hashed = hash_password(new_pass)

        if new_pass == new_cpass:
            # print("Changes")
            UserMaster.objects.filter(username=user_n).update(password = hashed)
            messages.success(request,"Your password is reset")
            UserMaster.objects.filter(username=user_n).update(token = "")
            return redirect("/") 

        else:
            messages.error(request,"Enter matching passwords")
            # print("Password does not match")

    return render (request,'resetpass.html',context)

def forgot(request):

    userA = UserMaster.objects.values_list('username')
    uA = []
    lis = list(userA)
    for i in lis:
        uA.append(i[0])

    token = str(uuid.uuid4())

    if request.method == 'POST':
        name = request.POST['username']

        if name in uA:
            email = UserMaster.objects.filter(username = name).values('email')
            email = list(email)
            email = email[0]['email']
            # print(email)

            tok = UserMaster.objects.get(username = name)
            tok.token = token
            tok.save()
            send_reset_password(email,token)
            messages.success(request,"The email is sent!!")
            return redirect("/") 
        else:
            messages.error(request,"User not found!!")

    return render(request,"forgot.html")

def logoutUser(request):
    global user_login
    user_login=False
    request.session.delete_test_cookie()
    logout(request)
    return redirect("/")

def edituser(request):
    if user_login:
        if user_data_type=="1":
            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])


            userdata = UserMaster.objects.filter(user_id=u_id).values()
            # print('userdata ',userdata)
            t = userdata[0]["user_type"]
            if t == "1":
                typ = "Admin"
            elif t == "2":
                typ = "Employee"
            else:
                typ = "Client"
            context = {
                'edit_user':userdata,
                'com':c,
                "type":typ,
            }
            userM = UserMaster.objects.values_list('username')
            uM = []
            lis = list(userM)
            for i in lis:
                uM.append(i[0])

            uM.remove(u)
            if request.method == 'POST':
                # print("Edit user if")
                cname = request.POST['company_name']
                # print(cname)
                ufullname = request.POST['user_full_name']
                uname = request.POST['user_name']
                type=request.POST['user_type']
                # print(type)
                num = request.POST['phone']
                
                uemail = request.POST['email']

                cid = CompanyMaster.objects.filter(company_name__icontains=cname).values()
                # print(cid)
                comid = cid[0]["id"]
                comname = cid[0]["company_name"]
                # print(comid)

                if uname in uM:
                    messages.error(request, 'Username already exists')
                else:
                    UserMaster.objects.filter(username=uname).update(user_type = type)
                    if ufullname:
                        UserMaster.objects.filter(username=uname).update(user_full_name = ufullname)
                    if uemail:
                        UserMaster.objects.filter(username=uname).update(email=uemail)
                    if num:
                        UserMaster.objects.filter(username=uname).update(contact_number=num)
                    if cname:
                        UserMaster.objects.filter(username=uname).update(company_id=comid)
                        UserMaster.objects.filter(username=uname).update(company_name=comname)
                        
                    messages.success(request, 'The changes have been made!!')
                
            return render(request,"Edituser.html",context)
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")

def createcompany(request):
    if user_login:
        ufname = UserMaster.objects.filter(username=username).values()
        ufshow = ufname[0]["user_full_name"]
        context = {
            "showname":ufshow
        }

        if user_data_type == "1":
            userA = CompanyMaster.objects.values_list('company_name')
            uA = []
            lis = list(userA)
            for i in lis:
                uA.append(i[0])
            # print(uA)
            if request.method == 'POST':
                    cname = request.POST['company_name']
                    cdesc = request.POST['company_desc']

                    if cname in uA:
                        messages.error(request, 'Company already exists')
                    else:
                        company = CompanyMaster(company_name=cname,company_desc=cdesc)
                        company.save()
                        messages.success(request, 'Company Created Succesfully!')
            return render(request,"createcompany.html",context)
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")


def createuser(request):
    if user_login:
        if user_data_type == "1":
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]

            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
            context={
                "com":c,
                "showname":ufshow,
            }
            return render(request, "createuser.html",context) 
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")
    

def searchuser(request):
    if user_login:
        if user_data_type == "1":
            if request.method == 'POST':
                uname = request.POST['user_full_name']
                num = request.POST['contact_number']
                uemail = request.POST['email']
                data = UserMaster.objects.filter(user_full_name=uname).values()
            else:
                data = UserMaster.objects.none()
        
            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
            
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                "showname":ufshow
            }
            context = {
                    'com':c,
                    'show_user':data,
                    "showname":ufshow
                }
            return render(request,"user-search.html",context)
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")

def searchcompany(request):
    if user_login:
        if user_data_type == "1":
            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                "showname":ufshow
            }
            context = {
                'com':c,
                "showname":ufshow
            }
            return render(request,"companysearch.html",context)
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")

def showuser(request):
    global user_name,user_data
    if user_login:
        if user_data_type == "1":
            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                "showname":ufshow,
            }

            if request.method == 'POST':
                user_name = request.POST['user_name']
                company_name = request.POST['company_name']
                # print(company_name)
                uf = request.POST['user_full_name']
                typeu = request.POST['user_type']
                #c_num = request.POST['phone']
                email = request.POST['email']

                multiple_q = Q(Q(user_type=typeu) & Q(username__icontains=user_name) & Q(user_full_name__icontains=uf) & Q(company_name__icontains = company_name))

                user_data = UserMaster.objects.filter(multiple_q).values()

                #print(user_data)
                for i in user_data:
                    print(i)

            context = {
                    'show_user':user_data,
                    'com':c,
                    "showname":ufshow,
                } 
            return render(request,"showuser.html",context) 
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")

def showcompany(request):
    if user_login:
        if user_data_type=="1":
            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
                ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                "showname":ufshow
            }

            if request.method == 'POST':
                cname = request.POST['company_name']
                cdesc = request.POST['company_desc']

                if cname:
                    com_name = CompanyMaster.objects.filter(company_name__icontains=cname).values()
                else:
                    com_name = CompanyMaster.objects.none()

                context = {
                    'show_company':com_name,
                    'com':c,
                    "showname":ufshow,
                } 
            return render(request,"showcompany.html",context)
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
       return redirect("/")

def createuser1(request):
    if user_login:
        if user_data_type=="1":
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                "showname":ufshow
            }

            userA = UserMaster.objects.values_list('username')
            uA = []
            lis = list(userA)
            for i in lis:
                uA.append(i[0])
            # print(uA)

            userE = UserMaster.objects.values_list('email')
            uE = []
            lis = list(userE)
            for i in lis:
                uE.append(i[0])

            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
            # print(c)

            context={
                "com":c,
                "showname":ufshow,
            }

            if request.method == 'POST':
                uname = request.POST['user_name']
                cname=request.POST["company_name"]
                ufullname = request.POST['user_full_name']
                password = request.POST['pass']
                type = request.POST['user_type']
                num = request.POST['phone']
                uemail = request.POST['email']
                type=int(type)
                hashed = hash_password(password)
                # print(cname)

                
                cid = CompanyMaster.objects.filter(company_name__icontains=cname).values()
                comid = cid[0]["id"]
                cname = cid[0]['company_name']

                if uname in uA:
                    messages.error(request, 'Username already exists') 
                elif uemail in uE:
                    messages.error(request, 'Duplicate entry for email not allowed')
                else:
                    userm = UserMaster(username=uname,user_full_name=ufullname,email=uemail,password=hashed,user_type=type,company_id=comid,contact_number=num,company_name=cname)
                    userm.save()
                    messages.success(request, 'User Created Succesfully!')

            return render(request, "createuser.html",context)
        else:
            if user_data_type == "2":
                return redirect("/home")
            elif user_data_type == "3":
                return redirect("/home")
    else:
        return redirect("/")

def remove(request):

    if request.method == 'POST':
        usern = request.POST['username']
        # print(usern)
        userid = UserMaster.objects.get(username = usern)
        # print(userid.user_id)
        userroom = RoomDetail.objects.get(user_id_id=userid,chat_room_id_id=rooid)
        # print("userroom     ",userroom)
        userroom.delete()
        # messages.success(request, 'The user has been removed from the chat room')

    return redirect("/sendmessage")

def removeemp(request):

    if request.method == 'POST':
        usern = request.POST['username']
        # print(usern)
        userid = UserMaster.objects.get(username = usern)
        # print(userid.user_id)
        userroom = RoomDetail.objects.get(user_id_id=userid,chat_room_id_id=rooid)
        # print("userroom     ",userroom)
        userroom.delete()

    return redirect("/sendmessageemp")

def addemp(request):

    if request.method == 'POST':
        usern = request.POST['username']
        # print(usern)
        userid = UserMaster.objects.get(username = usern)
        userid = userid.user_id
        # print(userid)

        room_obj = RoomDetail(chat_room_id_id = roid,user_id_id=userid)
        email = UserMaster.objects.get(user_id=userid)
        email = email.email
        send_room_add(email, namer)
        room_obj.save()
        # messages.success(request, 'The user has been added to the chat room')

    return redirect("/sendmessageemp")

def chatroom1(request):

    roid = int(chatroomval)

    if request.method == 'POST':
        usern = request.POST['username']
        # print(usern)
        userid = UserMaster.objects.get(username = usern)
        userid = userid.user_id
        # print(userid)

        room_obj = RoomDetail(chat_room_id_id = roid,user_id_id=userid)
        email = UserMaster.objects.get(user_id=userid)
        email = email.email
        send_room_add(email, namer)
        room_obj.save()
        messages.success(request, 'The user has been added to the chat room')

    return redirect("/editchatroom")

def addchatroom(request):
    if user_login:
        if user_data_type == "1":
            com = UserMaster.objects.all()
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            
            context = {
                "users":com,
                "showname":ufshow,
            }

            if request.method == 'POST':
                name = request.POST['chat_room_name']
                # print(name)

                ids = RoomMaster.objects.values_list('chat_room_id')
                #print(ids)
                ids_name = list(ids)
                c=[]
                for i in ids_name:
                    c.append(i[0])
                # print(c)

                new_id = len(c)+1

                room = RoomMaster(chat_room_name = name)
                room.save()

                ids = RoomMaster.objects.values_list('chat_room_id')
                ids_name = list(ids)
                c=[]
                for i in ids_name:
                    c.append(i[0])

                c.sort()
                new_id = c[-1]

                users = request.POST.getlist('users')
                # print("users ",users)
                
                u = UserMaster.objects.filter(user_type = "1").values_list('user_id') 
                u = list(u)
                # print(u)
                for i in u:
                    k = i[0]
                    k = str(k) 
                    # print("k ",k)
                    detail = RoomDetail(chat_room_id_id = new_id,user_id_id=k)
                    detail.save()
                
                for j in users:
                    if j == str(user_id):
                        continue
                    else:
                        detail = RoomDetail(chat_room_id_id = new_id,user_id_id=j)
                        email = UserMaster.objects.get(user_id=j)
                        email = email.email
                        send_room_add(email, name)
                        detail.save()
                
                messages.success(request, 'Chat Room Created Succesfully!')
        else:
            return redirect("/home")

        return render(request,"addchatroom.html",context)
    else:
        return redirect("/")


def chatroom4(request):
    global chatroomval,namer, pay, namerc, rid,uses,roid,rooid
    if user_login:
        if user_data_type == "1":

            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            
            uid = UserMaster.objects.filter(username=userl).values('user_id')
            uid = list(uid)
            u = uid[0]['user_id']

            if namerc:
                namer = namerc
            else:
                namer = 'Test'
            
            
            
            if rid:
                chatroomvalid = rid
            else:
                chatroomvalid = '0'

            if request.method == 'GET':

                if 'chatroom' in request.GET:
                    chatroomval = request.GET['chatroom']
                    # print(type(chatroomval))
                    pid = chatroomval
                    namer = RoomMaster.objects.filter(chat_room_id = chatroomval).values('chat_room_name')
                    namer = list(namer)
                    namer = namer[0]['chat_room_name']

                # print("chatroomval ",chatroomval)
            
            else:
                chatroomval = chatroomval
                namer = namer

            room_access = RoomDetail.objects.filter(user_id_id=user_id).values('chat_room_id_id')
            room_access_list = list(room_access)
            roomaccess = []
            roomid =[]
            a = ['id']
            b = []
            c = ['name']
            d = []
            dz = []
            blist = []
            for id_list in room_access_list:
                roomid.append(id_list['chat_room_id_id'])
                b.append(id_list['chat_room_id_id'])
                dzid = dict(zip(a,b))
                # print(dzid)
                blist.append(dzid)
                b.remove(id_list['chat_room_id_id'])
            # print("blist  ",blist)

            l = len(roomid)
            for i in range(0,l):
                idi = roomid[i]
                room_name = RoomMaster.objects.filter(chat_room_id = idi).values('chat_room_name')
                room_name = list(room_name)
                roomaccess.append(room_name[0]['chat_room_name'])
                blist[i]['name'] = room_name[0]['chat_room_name']
            # print("blist  ",blist)

            msg = RoomContent.objects.values_list('message')
            name=[]

            msg = RoomContent.objects.filter(chat_room_id_id=chatroomval).values()
            msgid = RoomContent.objects.filter(chat_room_id_id=chatroomval).values('sender_id_id')
            sid = []
            for i in msgid:
                sid.append(i['sender_id_id'])


            name=[]
            for j in sid:
                idname = UserMaster.objects.filter(user_id=j).values('username') 
                idname = list(idname)

                for a in idname:
                    name.append(a['username'])
            
                        #remove user
            rooid = int(chatroomval)
            # print("rid      ",rooid)
            use = RoomDetail.objects.filter(chat_room_id_id=rooid).values_list('user_id_id')
            # print(use)
            uses = []
            for i in use:
                j = i[0]
                use1 = UserMaster.objects.filter(user_id = j).values_list('username')
                # print(use1)
                uses.append(use1[0][0])
            # print("uses     ",uses)
            
            # print("Pay  ",pay)
            if pay == True:
                # print("Pay Detail")

                uid = UserMaster.objects.filter(username=userl).values('user_id')
                uid = list(uid)
                u = uid[0]['user_id']
                # print(u)

                cid = UserMaster.objects.filter(user_id=u).values('company_id')
                cid = list(cid)
                c = cid[0]['company_id']
                # print(c)

                details_pay = PayDetail.objects.filter(c_id_id = c).values()
                details_pay = list(details_pay)
                # print(details_pay)
                # print("Detail pay")

                det = f"Bank Details: \n IFSC Code: {details_pay[0]['ifsc']} \n Account Number: {details_pay[0]['acc_num']} \n Account Name: {details_pay[0]['acc_name']} \n Bank Name: {details_pay[0]['bank_name']} \n Branch Name: {details_pay[0]['branch_name']}"
                # print(det)

                uid = UserMaster.objects.filter(username=userl).values('user_id')
                # print("send message if")

                uid = list(uid)
                u = uid[0]['user_id']

                namerc = namer
                rid = chatroomval

                # print(det)
                # print(userl)
                # print(u)
                # print(rooid)
                # print("chatroomval ",chatroomval)

                paymess = RoomContent(message = det,username=userl, sender_id_id = u, chat_room_id_id = rooid)
                paymess.save()

                namer = RoomMaster.objects.get(chat_room_id = chatroomval)
                namer = namer.chat_room_name

            else:
                # print("Detail pay else")
                details_pay = []

            context = {
                "rooms":blist,
                "messages":msg,
                "users":name,
                "chatroomval":chatroomval,
                "user":userl,
                "name":namer,
                "defid":chatroomvalid,
                "showname":ufshow,
                "details":details_pay,
                "pay":pay,
                "userss":uses,
                # "names":namel,
            }

            pay = 'False'
        else:
            return redirect("/home")

        return render(request, "chat_admin.html",context)
    else:
        return redirect("/")

def sendmessage(request):
    global namerc, rid
    
    # print("send message before if")
    if request.method == 'POST':
        message = request.POST['message']
        uid = UserMaster.objects.filter(username=userl).values('user_id')
        # print("send message if")

        uid = list(uid)
        u = uid[0]['user_id']

        namerc = namer
        rid = chatroomval

        if message:

            mess = RoomContent(message = message,username=userl, sender_id_id = u, chat_room_id_id = chatroomval)
            mess.save()

            ids = RoomContent.objects.values_list('id')
            ids = list(ids)
            c=[]
            for i in ids:
                c.append(i[0])

            c.sort()
            new_id = c[-1]

            lstmsg = RoomContent.objects.filter(id = new_id).values_list('timestamp')
            # print(lstmsg)
            RoomMaster.objects.filter(chat_room_id = chatroomval).update(last_message = lstmsg)
            # print("msg last     ",new_id)
            # print("message saved to database")
        else:
            print("Not saved")
    return redirect("/chatrooms_admin")

def paydetail(request): #user_data_type
    global pay
    pay = True 
        # print(" Pay true in paydetail view")

    if user_data_type == "1":
            return redirect("/chatrooms_admin")
    else:
        if user_data_type == "2":
            return redirect("/chatrooms_emp")
        elif user_data_type == "3":
            return redirect("/chatrooms_client")
    


def chatroom6(request):
    global chatroomval,namer, namerc, rid, pay
    if user_login:
        if user_data_type == "3":
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]

            uid = UserMaster.objects.filter(username=userl).values('user_id')
            uid = list(uid)
            u = uid[0]['user_id']

            if namerc:
                namer = namerc
            else:
                namer = 'Test'

            if rid:
                chatroomvalid = rid
            else:
                chatroomval = '0'

            # crooms = RoomMaster.objects.all()
            # msg = RoomContent.objects.values_list('message')
            # name=[]
            
            room_access = RoomDetail.objects.filter(user_id_id=user_id).values('chat_room_id_id')
            room_access_list = list(room_access)
            roomaccess = []
            roomid =[]
            a = ['id']
            b = []
            c = ['name']
            d = []
            dz = []
            blist = []
            for id_list in room_access_list:
                roomid.append(id_list['chat_room_id_id'])
                b.append(id_list['chat_room_id_id'])
                dzid = dict(zip(a,b))
                # print(dzid)
                blist.append(dzid)
                b.remove(id_list['chat_room_id_id'])
            # print("blist  ",blist)

            l = len(roomid)
            for i in range(0,l):
                idi = roomid[i]
                room_name = RoomMaster.objects.filter(chat_room_id = idi).values('chat_room_name')
                room_name = list(room_name)
                roomaccess.append(room_name[0]['chat_room_name'])
                blist[i]['name'] = room_name[0]['chat_room_name']

            # print("blist    ",blist)

            # print("room_access ",roomaccess) 
            # print("room_id ",roomid) 

            if request.method == 'GET':

                if 'chatroom' in request.GET:
                    chatroomval = request.GET['chatroom']
                    # print(type(chatroomval))
                    namer = RoomMaster.objects.filter(chat_room_id = chatroomval).values('chat_room_name')
                    namer = list(namer)
                    namer = namer[0]['chat_room_name']

                # print("chatroomval ",chatroomval)
            
            else:
                chatroomval = chatroomval
                namer = namer

            msg = RoomContent.objects.filter(chat_room_id_id=chatroomval).values()
            msgid = RoomContent.objects.filter(chat_room_id_id=chatroomval).values('sender_id_id')
            sid = []
            for i in msgid:
                sid.append(i['sender_id_id'])


            name=[]
            for j in sid:
                idname = UserMaster.objects.filter(user_id=j).values('username') 
                idname = list(idname)

                for a in idname:
                    name.append(a['username'])
                
                # print("Pay  ",pay)
            if pay == True:
                # print("Pay Detail")

                uid = UserMaster.objects.filter(username=userl).values('user_id')
                uid = list(uid)
                u = uid[0]['user_id']
                # print(u)

                cid = UserMaster.objects.filter(user_id=u).values('company_id')
                cid = list(cid)
                c = cid[0]['company_id']
                # print(c)

                details_pay = PayDetail.objects.filter(c_id_id = c).values()
                details_pay = list(details_pay)
                # print(details_pay)
                # print("Detail pay")

                det = f"Bank Details: \n IFSC Code: {details_pay[0]['ifsc']} \n Account Number: {details_pay[0]['acc_num']} \n Account Name: {details_pay[0]['acc_name']} \n Bank Name: {details_pay[0]['bank_name']} \n Branch Name: {details_pay[0]['branch_name']}"
                # print(det)

                uid = UserMaster.objects.filter(username=userl).values('user_id')
                # print("send message if")

                uid = list(uid)
                u = uid[0]['user_id']

                namerc = namer
                rid = chatroomval

                paymess = RoomContent(message = det,username=userl, sender_id_id = u, chat_room_id_id = rooid)
                paymess.save()

                namer = RoomMaster.objects.get(chat_room_id = chatroomval)
                namer = namer.chat_room_name

            else:
                # print("Detail pay else")
                details_pay = []
            
            context = {
                "messages":msg,
                "users":name,
                "chatroomval":chatroomval,
                "user":userl,
                "name":namer,
                "defid":chatroomvalid,
                "showname":ufshow,
                "room_id":roomid,
                "room_name":roomaccess,
                "rooms":blist, 
                "pay":pay,
                "detail_pay":details_pay
            }

            pay = False
        else:
            return redirect("/home")

        return render(request, "chat_client.html",context)
    else:
        return redirect("/")

def sendmessagec(request):
    global namerc, rid
    #chatroomval
    
    # print("send message before if")
    if request.method == 'POST':
        message = request.POST['message']
        uid = UserMaster.objects.filter(username=userl).values('user_id')
        # print("send message if")
        # print(userl)
        # print("uid, uid list")
        # print(uid)
        uid = list(uid)
        u = uid[0]['user_id']
        # print(message)

        namerc = namer
        rid = chatroomval

        if message:

            mess = RoomContent(message = message,username=userl, sender_id_id = u, chat_room_id_id = chatroomval)
            mess.save()

            ids = RoomContent.objects.values_list('id')
            ids = list(ids)
            c=[]
            for i in ids:
                c.append(i[0])

            c.sort()
            new_id = c[-1]

            lstmsg = RoomContent.objects.filter(id = new_id).values_list('timestamp')
            # print(lstmsg)
            RoomMaster.objects.filter(chat_room_id = chatroomval).update(last_message = lstmsg)
            # print("msg last     ",new_id)
            # print("message saved to database")
        else:
            print("Not saved")
    return redirect("/chatrooms_client")

def addchatroom2(request):
    if user_login:
        if user_data_type == '2':
            com = UserMaster.objects.all()
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                    "showname":ufshow,
                    "users":com,
                }
            
            if request.method == 'POST':
                name = request.POST['chat_room_name']
                # print(name)

                ids = RoomMaster.objects.values_list('chat_room_id')
                #print(ids)
                ids_name = list(ids)
                c=[]
                for i in ids_name:
                    c.append(i[0])
                # print(c)

                new_id = len(c)+1

                room = RoomMaster(chat_room_name = name)
                room.save()

                ids = RoomMaster.objects.values_list('chat_room_id')
                ids_name = list(ids)
                c=[]
                for i in ids_name:
                    c.append(i[0])

                c.sort()
                new_id = c[-1]

                users = request.POST.getlist('users')
                # print("users ",users)

                # print("id   ",user_id) 
                if str(user_id) in users: 
                    print("pass")
                else:
                    print("not pass")
                    j = str(user_id) 
                    # print(j)
                    # print(type(j))
                    detail = RoomDetail(chat_room_id_id = new_id,user_id_id=j)
                    detail.save()
                
                u = UserMaster.objects.filter(user_type = "1").values_list('user_id') 
                u = list(u)
                # print(u)
                for i in u:
                    k = i[0]
                    k = str(k) 
                    # print("k ",k)
                    detail = RoomDetail(chat_room_id_id = new_id,user_id_id=k)
                    detail.save()
                
                for j in users:
                        detail = RoomDetail(chat_room_id_id = new_id,user_id_id=j)
                        email = UserMaster.objects.get(user_id=j)
                        email = email.email
                        send_room_add(email, name)
                        detail.save()
                
                messages.success(request, 'Chat Room Created Succesfully!')

        else:
            return redirect("/home")
        return render(request,"addchatroom2.html",context)
    else:
        return redirect("/")

def readuser(request):
    global u_id,u,usercname
    if user_login:
        if user_data_type == "1":
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]

            if request.method == 'POST':
                u_id = request.POST['userid']
            
                userdata = UserMaster.objects.filter(user_id=u_id).values()
                u = userdata[0]["username"]
                usercname = userdata[0]["company_name"]

                t = userdata[0]["user_type"]
                if t == "1":
                    typ = "Admin"
                elif t == "2":
                    typ = "Employee"
                else:
                    typ = "Client"
            
            context = {
                    "users" : userdata,
                    "name":u,
                    "type":typ,
                    "showname":ufshow,
                }
            return render(request,"readuser.html",context)
        else:
            return redirect("/home")
    else:
        return redirect("/")

def editcompany(request):
    if user_login:
        if user_data_type == "1":
            companydata = CompanyMaster.objects.filter(id=c_id).values()
            desct = companydata[0]["company_desc"]
            context = {
                "edit_com":companydata,
                "desc":desct,
            }

            com_n = CompanyMaster.objects.values_list('company_name')
            com_name = list(com_n)
            c=[]
            for i in com_name:
                c.append(i[0])
            c.remove(comname)

            if request.method == 'POST':
                name = request.POST['company_name']
                desc = request.POST['company_desc']

                if name in c:
                    messages.error(request, 'Company already exists')
                else:
                    if desc:
                        CompanyMaster.objects.filter(company_name=comname).update(company_desc=desc)
                    if name:
                        CompanyMaster.objects.filter(company_name=comname).update(company_name=name)
                    messages.success(request,"The changes have been made!!")

            return render(request,"editcompany.html",context)
        else:
            return redirect("/home")
    else:
        return redirect("/")

def readcompany(request):
    global c_id,comname
    if user_login:
        if user_data_type == '1':
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]
            context = {
                "showname":ufshow
            }
            if request.method == 'POST':
                c_id = request.POST['comid']
                # print(c_id)
                comdata = CompanyMaster.objects.filter(id=c_id).values()
                comname = comdata[0]["company_name"]

                c = comdata[0]['company_name']
                context = {
                    "companys" : comdata,
                    "name":c,
                    "showname":ufshow
                }

            return render(request,"readcompany.html",context)
        else:
            return redirect("/home")
    else:
        return redirect("/")

def chatroom_sidebar(request):
    return render(request,"chatroom_sidebar.html")

def payment(request):

    if user_data_type == "1":
        uid = UserMaster.objects.filter(username=userl).values('user_id')
        uid = list(uid)
        u = uid[0]['user_id']
        u = int(u)
        # print(u)

        cid = UserMaster.objects.filter(user_id=u).values('company_id')
        cid = list(cid)
        c = cid[0]['company_id']
        c = int(c)
        # print(c)
        if request.method == 'POST':
            # c = request.FILES['qrCode']
            ifsc = request.POST['IFSC_code']
            accnum = request.POST['account_number']
            accname = request.POST['account_name']
            bname = request.POST['branch_name']
            bank = request.POST['bank_name']

            pay = PayDetail(ifsc = ifsc, acc_num = accnum, acc_name = accname, bank_name = bank, branch_name = bname,c_id_id = c, user_id_id = u)
            pay.save()

            # print("Saved succesfully")
            messages.success(request,"Payment Details Added")


        ufname = UserMaster.objects.filter(username=username).values()
        ufshow = ufname[0]["user_full_name"]

        pdet = PayDetail.objects.filter(c_id_id = c).values()
        pdet = list(pdet)
        # for i in pdet:
        #     print(i['ifsc'])
        # print("pdet     ", pdet)
        
        context = {
            "showname":ufshow,
            "type":user_data_type,
            "details":pdet,
            }

        return render(request,"payment.html",context)
    
    elif user_data_type == "3":
        uid = UserMaster.objects.filter(username=userl).values('user_id')
        uid = list(uid)
        u = uid[0]['user_id']
        u = int(u)
        # print(u)

        cid = UserMaster.objects.filter(user_id=u).values('company_id')
        cid = list(cid)
        c = cid[0]['company_id']
        c = int(c)
        if request.method == 'POST':
            # c = request.FILES['qrCode']
            ifsc = request.POST['IFSC_code']
            accnum = request.POST['account_number']
            accname = request.POST['account_name']
            bname = request.POST['branch_name']
            bank = request.POST['bank_name']

            pay = PayDetail(ifsc = ifsc, acc_num = accnum, acc_name = accname, bank_name = bank, branch_name = bname,c_id_id = c, user_id_id = u)
            pay.save()

            # print("Saved succesfully")
            messages.success(request,"Payment Details Added")

        # print(c)

        ufname = UserMaster.objects.filter(username=username).values()
        ufshow = ufname[0]["user_full_name"]

        pdet = PayDetail.objects.filter(c_id_id = c).values()
        pdet = list(pdet)
        # print("pdet     ", pdet)

        context = {
            "showname":ufshow,
            "type":user_data_type,
            "details":pdet,
            }
        return render(request,"payment.html",context)
 
    else:
        return redirect("/home")
    

        
def chatroom5(request):
    global chatroomval,namer, namerc, rid, pay,namel,roid,rooid,uses
    if user_login:
        if user_data_type == '2':
            ufname = UserMaster.objects.filter(username=username).values()
            ufshow = ufname[0]["user_full_name"]

            uid = UserMaster.objects.filter(username=userl).values('user_id')
            uid = list(uid)
            u = uid[0]['user_id']

            if namerc:
                namer = namerc
            else:
                namer = 'Test'

            if rid:
                chatroomvalid = rid
            else:
                chatroomval = '0'
            
            room_access = RoomDetail.objects.filter(user_id_id=user_id).values('chat_room_id_id')
            room_access_list = list(room_access)
            roomaccess = []
            roomid =[]
            a = ['id']
            b = []
            c = ['name']
            d = []
            dz = []
            blist = []
            for id_list in room_access_list:
                roomid.append(id_list['chat_room_id_id'])
                b.append(id_list['chat_room_id_id'])
                dzid = dict(zip(a,b))
                # print(dzid)
                blist.append(dzid)
                b.remove(id_list['chat_room_id_id'])
            # print("blist  ",blist)

            l = len(roomid)
            for i in range(0,l):
                idi = roomid[i]
                room_name = RoomMaster.objects.filter(chat_room_id = idi).values('chat_room_name')
                room_name = list(room_name)
                roomaccess.append(room_name[0]['chat_room_name'])
                blist[i]['name'] = room_name[0]['chat_room_name']


                        #remove user
            rooid = int(chatroomval)
            # print("rid      ",rooid)
            use = RoomDetail.objects.filter(chat_room_id_id=rooid).values_list('user_id_id')
            # print(use)
            uses = []
            for i in use:
                j = i[0]
                use1 = UserMaster.objects.filter(user_id = j).values_list('username')
                # print(use1)
                uses.append(use1[0][0])
            # print("uses     ",uses)

            #add user
            roid = int(chatroomval)
            usea = UserMaster.objects.values_list('user_id')
            # print('usea     ',usea)
            useid = []
            for i in usea:
                useid.append(i[0])
            useid.sort()
            # print("useid        ",useid)

            usere = RoomDetail.objects.filter(chat_room_id_id=roid).values_list('user_id_id')
            # print("usere    ",usere)
            for j in usere:
                # print("j    ",j)
                useid.remove(j[0])
            # print("useid        ",useid)

            namel = []
            for ele in useid:
                name = UserMaster.objects.get(user_id=ele)
                name = name.username
                namel.append(name)
            # print(namel)

            if request.method == 'GET':

                if 'chatroom' in request.GET:
                    chatroomval = request.GET['chatroom']
                    # print(type(chatroomval))
                    namer = RoomMaster.objects.filter(chat_room_id = chatroomval).values('chat_room_name')
                    namer = list(namer)
                    namer = namer[0]['chat_room_name']

                # print("chatroomval ",chatroomval)
            
            else:
                chatroomval = chatroomval
                namer = namer

            rem = RoomDetail.objects.filter(chat_room_id_id = chatroomval).values('user_id_id')
            rem = list(rem)
            remo = []
            for i in rem:
                remo.append(i['user_id_id'])
            # print("rem0  ",remo)
            usess = []
            for j in remo:
                uses = UserMaster.objects.filter(user_id = j).values('username')
                usess.append(uses[0]['username'])
            # print(usess) 


            msg = RoomContent.objects.filter(chat_room_id_id=chatroomval).values()
            msgid = RoomContent.objects.filter(chat_room_id_id=chatroomval).values('sender_id_id')
            sid = []
            for i in msgid:
                sid.append(i['sender_id_id'])


            name=[]
            for j in sid:
                idname = UserMaster.objects.filter(user_id=j).values('username') 
                idname = list(idname)

                for a in idname:
                    name.append(a['username'])
                
            # print("Pay  ",pay)
            if pay == True:
                # print("Pay Detail")

                uid = UserMaster.objects.filter(username=userl).values('user_id')
                uid = list(uid)
                u = uid[0]['user_id']
                # print(u)

                cid = UserMaster.objects.filter(user_id=u).values('company_id')
                cid = list(cid)
                c = cid[0]['company_id']
                # print(c)

                details_pay = PayDetail.objects.filter(c_id_id = c).values()
                details_pay = list(details_pay)
                # print(details_pay)
                # print("Detail pay")

                det = f"Bank Details: \n IFSC Code: {details_pay[0]['ifsc']} \n Account Number: {details_pay[0]['acc_num']} \n Account Name: {details_pay[0]['acc_name']} \n Bank Name: {details_pay[0]['bank_name']} \n Branch Name: {details_pay[0]['branch_name']}"
                # print(det)

                uid = UserMaster.objects.filter(username=userl).values('user_id')
                # print("send message if")

                uid = list(uid)
                u = uid[0]['user_id']

                namerc = namer
                rid = chatroomval

                paymess = RoomContent(message = det,username=userl, sender_id_id = u, chat_room_id_id = rooid)
                paymess.save()

                namer = RoomMaster.objects.get(chat_room_id = chatroomval)
                namer = namer.chat_room_name

            else:
                # print("Detail pay else")
                details_pay = [] 
            
            context = {
                "messages":msg,
                "users":name,
                "chatroomval":chatroomval,
                "user":userl,
                "name":namer,
                "defid":chatroomvalid,
                "showname":ufshow,
                "room_id":roomid,
                "room_name":roomaccess,
                "rooms":blist, 
                "pay":pay,
                "details_pay":details_pay,
                "users":uses,
                "userss":usess,
                "names":namel,
            }

            pay = False

            return render(request, "chat_emp.html",context)
        else:
            return redirect("/home")
    else:
        return redirect("/")

def sendmessageemp(request):
    global namerc, rid
    #chatroomval
    # print("chatroomval      ",chatroomval)
    
    # print("send message before if")
    if request.method == 'POST':
        message = request.POST['message']
        uid = UserMaster.objects.filter(username=userl).values('user_id')
        # print("send message if")
        uid = list(uid)
        u = uid[0]['user_id']


        namerc = namer
        rid = chatroomval

        if message:

            mess = RoomContent(message = message,username=userl, sender_id_id = u, chat_room_id_id = chatroomval)
            mess.save()

            ids = RoomContent.objects.values_list('id')
            ids = list(ids)
            c=[]
            for i in ids:
                c.append(i[0])

            c.sort()
            new_id = c[-1]

            lstmsg = RoomContent.objects.filter(id = new_id).values_list('timestamp')
            # print(lstmsg)
            RoomMaster.objects.filter(chat_room_id = chatroomval).update(last_message = lstmsg)
            # print("msg last     ",new_id)
            # print("message saved to database")
            
        else:
            print("Not saved")
    return redirect("/chatrooms_emp")

def room(request):
    return render(request, "tempchatroom.html")

def editchatroom(request):
    global namel

    room_id = chatroomval
    if request.method == 'POST':
        usid = request.POST['userid']

        userroom = RoomDetail.objects.get(user_id_id=usid,chat_room_id_id=room_id)
        userroom.delete()
        messages.success(request, 'The user has been removed from the chat room')
        
    userid = RoomDetail.objects.filter(chat_room_id_id = room_id).values_list('user_id_id')
    userid = list(userid)
    uid = []
    table = []
    a = ['id']
    b = []
    # print(table)
    for i in userid:
        j = i[0]
        uid.append(j)
        b.append(j)

    l = len(b)
    # print("lem ",l)
    for i in range(0,l):
        # print(i)
        j = b[i]
        obj = UserMaster.objects.filter(user_id = j).values()
        obj = list(obj)
        # print(obj)

        c = {'id':obj[0]['user_id'],'name':obj[0]['user_full_name'],'cname':obj[0]['company_name']}
        # print("c    ",c)
        table.append(c) 

    #add user
        roid = int(chatroomval)
        usea = UserMaster.objects.values_list('user_id')
        # print('usea     ',usea)
        useid = []
        for i in usea:
            useid.append(i[0])
        useid.sort()
        # print("useid        ",useid)

        usere = RoomDetail.objects.filter(chat_room_id_id=roid).values_list('user_id_id')
        # print("usere    ",usere)
        for j in usere:
            # print("j    ",j)
            useid.remove(j[0])
        # print("useid        ",useid)

        namel = []
        for ele in useid:
            name = UserMaster.objects.get(user_id=ele)
            name = name.username
            namel.append(name)
        # print(namel)
        
    # print('table')
    # print(table)

    context = {
        'table':table,
        'names':namel,
        'name':namer,
    }

    return render(request,"editchatroom.html",context)