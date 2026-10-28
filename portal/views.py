from django.contrib.auth.decorators import login_required, user_passes_test

from django.shortcuts import render, HttpResponse
from datetime import datetime
from portal.models import Contect
from portal.models import Enquiry
from .models import AdmissionApplication
from django.contrib import messages
from .models import StudentProfile

from .models import Gallery

from .models import NewsAndAnnouncement

# Create your views here

def index(request):
    # डेटाबेस से न्यूज़ निकालें
    latest_news = NewsAndAnnouncement.objects.all().order_by('-news_date')[:4]
    # context बनाएँ
    context = {'latest_news': latest_news ,}
    
    return render(request, 'index.html', context)


#def index(request):
 #  return render(request, 'index.html')

def home(request):
    latest_news = NewsAndAnnouncement.objects.all().order_by('-news_date')[:4]
    context = {'latest_news': latest_news}
    #return render(request, 'index.html', context)
    return render(request, 'home.html', context)

def about_institute(request):
    return render(request, 'about_institute.html')

def facilities(request):
    return render(request, 'facilities.html')

#def contect(request):
    #return render(request, 'contect.html')

def courses_mmhapu(request):
    return render(request, 'courses_mmhapu.html')

def courses_ncpul(request):
    return render(request, 'courses_ncpul.html')

def from_mmhapu(request):
    return render(request, 'from_mmhapu.html')

def from_ncpul(request):
    return render(request, 'from_ncpul.html')

#def gallery(request):
    # डेटाबेस से सारी फोटो लें, और सबसे नई फोटो सबसे ऊपर दिखाएं (-upload_date)
   # gallery_images = Gallery.objects.all().order_by('-upload_date')
    
    # इन फोटो को HTML पेज पर भेजें
   # context = {
    #    'images': gallery_images
   # }
   # return render(request, 'gallery.html', context)

from django.shortcuts import render
from .models import Gallery, GallerySlider 

def gallery(request):
    # डेटाबेस से दोनों फोटो निकाल रहे हैं
    gallery_images = Gallery.objects.all().order_by('-upload_date')
    sliders = GallerySlider.objects.all()
    
    # दोनों को HTML में भेज रहे हैं
    context = {
        'images': gallery_images,
        'sliders': sliders
    }
    
    return render(request, 'gallery.html', context)



def news(request):
    latest_news = NewsAndAnnouncement.objects.all().order_by('-news_date')[:]
    context = {'latest_news': latest_news}
    #return render(request, 'index.html', context)
    return render(request, 'news.html', context)

def university_fee(request):
    return render(request, 'university_fee.html')


def admission_enquiry(request):
    return render(request, 'admission_enquiry.html')

def our_organization(request):
    return render(request, 'our_organization.html')

def our_mission_vision(request):
    return render(request, 'our_mission_vision.html')

def our_motto(request):
    return render(request, 'our_motto.html')

def affiliation(request):
    return render(request, 'affiliation.html')

def location(request):
    return render(request, 'location.html')

def admission_form(request):
    return render(request, 'admission_form.html')

def student_portal(request):
    return render(request, 'login/student_portal.html')

def faculty_portal(request):
    return render(request, 'login/faculty_portal.html')

from django.shortcuts import render
from .models import ExamResult  # मॉडल इम्पोर्ट करना ज़रूरी है

def exam_results(request):
    # डेटाबेस से हर कोर्स का रिजल्ट निकाल कर context में डाल रहे हैं
    context = {
        'bca_results': ExamResult.objects.filter(course='BCA').order_by('-upload_date'),
        'bba_results': ExamResult.objects.filter(course='BBA').order_by('-upload_date'),
        'blis_results': ExamResult.objects.filter(course='BLIS').order_by('-upload_date'),
        'pris_results': ExamResult.objects.filter(course='PRIS').order_by('-upload_date'),
        'diploma_results': ExamResult.objects.filter(course='DIPLOMA').order_by('-upload_date'),
    }
    # अब यह context (डेटा) HTML पेज को भेजा जा रहा है
    return render(request, 'exam_results.html', context)

def contect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        my_form = Contect(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        my_form.save()
        messages.success(request, "Your message has been send")
    return render(request, 'contect.html') 

def form_data_admission_enquiry(request):
    if request.method == 'POST':
        studentName = request.POST.get('studentName')
        dob = request.POST.get('dob')
        courceCategory = request.POST.get('courceCategory')
        courseInterested = request.POST.get('courseInterested')
        city = request.POST.get('city')
        zipCode = request.POST.get('zipCode')
        phoneNo = request.POST.get('phoneNo')
        email = request.POST.get('email')
        my_form_enquiry = Enquiry(studentName=studentName, dob=dob, courceCategory=courceCategory, courseInterested=courseInterested, city=city, zipCode=zipCode, phoneNo=phoneNo, email=email, date=datetime.today())
        my_form_enquiry.save()
        messages.success(request, "Your message has been send")
        return render(request, 'admission_enquiry.html')


#addmision form
def form_data_admission(request):
    if request.method == 'POST':
        # 1. Course & Session Details
        courseApplied = request.POST.get('courseApplied')
        session = request.POST.get('session')

        # 2. Personal Information
        studentName = request.POST.get('studentName')
        fatherName = request.POST.get('fatherName')
        motherName = request.POST.get('motherName')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        Nationality = request.POST.get('Nationality')
        maritalStatus = request.POST.get('maritalStatus')
        background = request.POST.get('background')
        phyHandicapped = request.POST.get('phyHandicapped')
        category = request.POST.get('category')
        religion = request.POST.get('religion')
        bloodGroup = request.POST.get('bloodGroup')
        markIden = request.POST.get('markIden')

        # 3. Document Uploads (फ़ोटो और सिग्नेचर FILES में आते हैं)
        student_photo = request.FILES.get('student_photo')
        student_signature = request.FILES.get('student_signature')

        # 4. Contact & Address Details
        mobileNO = request.POST.get('mobileNO')
        email = request.POST.get('email')

        PermanentAddress = request.POST.get('PermanentAddress')
        per_district = request.POST.get('per_district')
        per_state = request.POST.get('per_state')
        per_pinCode = request.POST.get('per_pinCode')

        correspondenceAddress = request.POST.get('correspondenceAddress')
        corr_district = request.POST.get('corr_district')
        corr_state = request.POST.get('corr_state')
        corr_pinCode = request.POST.get('corr_pinCode')

        # 5. Educational Qualification
        tenth_board = request.POST.get('tenth_board')
        tenth_passYear = request.POST.get('tenth_passYear')
        tenth_percentage = request.POST.get('tenth_percentage')
        tenth_division = request.POST.get('tenth_division')

        twelth_board = request.POST.get('twelth_board')
        twelth_passYear = request.POST.get('twelth_passYear')
        twelth_percentage = request.POST.get('twelth_percentage')
        twelth_division = request.POST.get('twelth_division')

        ug_board = request.POST.get('ug_board')
        ug_passYear = request.POST.get('ug_passYear')
        ug_percentage = request.POST.get('ug_percentage')
        ug_division = request.POST.get('ug_division')

        pg_board = request.POST.get('pg_board')
        pg_passYear = request.POST.get('pg_passYear')
        pg_percentage = request.POST.get('pg_percentage')
        pg_division = request.POST.get('pg_division')

        # ========================================================
        # डेटाबेस मॉडल में डेटा सेव करना (Saving to Model)
        # ========================================================
        my_admission_form = AdmissionApplication(
            course_applied=courseApplied,
            session=session,
            
            student_name=studentName,
            father_name=fatherName,
            mother_name=motherName,
            dob=dob,
            gender=gender,
            nationality=Nationality,
            marital_status=maritalStatus,
            background=background,
            physically_handicapped=phyHandicapped,
            category=category,
            religion=religion,
            blood_group=bloodGroup,
            mark_of_identification=markIden,

            # फाइल सेविंग
            student_photo=student_photo,
            student_signature=student_signature,

            mobile_no=mobileNO,
            email=email,

            permanent_address=PermanentAddress,
            per_district=per_district,
            per_state=per_state,
            per_pincode=per_pinCode,

            correspondence_address=correspondenceAddress,
            corr_district=corr_district,
            corr_state=corr_state,
            corr_pincode=corr_pinCode,

            tenth_board=tenth_board,
            tenth_pass_year=tenth_passYear,
            tenth_percentage=tenth_percentage,
            tenth_division=tenth_division,

            twelth_board=twelth_board,
            twelth_pass_year=twelth_passYear,
            twelth_percentage=twelth_percentage,
            twelth_division=twelth_division,

            ug_board=ug_board,
            ug_pass_year=ug_passYear,
            ug_percentage=ug_percentage,
            ug_division=ug_division,

            pg_board=pg_board,
            pg_pass_year=pg_passYear,
            pg_percentage=pg_percentage,
            pg_division=pg_division
        )
        
        my_admission_form.save()
        messages.success(request, "Your admission form has been successfully submitted!")
        
        # फॉर्म भरने के बाद पेज को रीफ्रेश करने के लिए
        return render(request, 'admission_form.html')

    # अगर रिक्वेस्ट GET है (यानी यूजर ने पहली बार पेज खोला है)
    return render(request, 'admission_form.html')

#admin

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# ==========================================
# 1. Student Login (सिर्फ स्टूडेंट्स के लिए)
# ==========================================
def student_portal(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        
        # ऑथेंटिकेशन चेक
        user = authenticate(request, username=usr, password=pwd)
        
        if user is not None:
            if not user.is_staff: # चेक करो कि स्टूडेंट ही है
                login(request, user)
                return redirect('student_dashboard') # सही होने पर डैशबोर्ड पर भेजो
            else:
                messages.error(request, "Access Denied: Please use Faculty portal.")
        else:
            # गलत पासवर्ड होने पर यह मैसेज ट्रिगर होगा
            messages.error(request, "Invalid Username or Password")
            
    # अगर GET रिक्वेस्ट है या पासवर्ड गलत है, तो वापस लॉगिन पेज दिखाओ
    return render(request, 'login/student_portal.html')

# ==========================================
# 2. Faculty Login (सिर्फ फैकल्टी/स्टाफ के लिए)
# ==========================================
def faculty_portal(request):
    if request.method == 'POST':
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        
        user = authenticate(request, username=usr, password=pwd)
        
        if user is not None:
            # यहाँ हम चेक कर रहे हैं कि यूज़र के पास स्टाफ की परमिशन है या नहीं
            if user.is_staff:
                login(request, user)
                # यहाँ 'faculty_dashboard' का URL नाम डालें जो हम आगे बनाएंगे
                return redirect('faculty_dashboard') 
            else:
                # अगर कोई स्टूडेंट यहाँ से लॉगिन करने की कोशिश करे
                messages.error(request, "Access Denied: You do not have Faculty permissions.")
        else:
            messages.error(request, "Invalid Username or Password")
            
    return render(request, 'login/faculty_portal.html')

# ==========================================
# सिक्योरिटी गार्ड्स (चेक करने वाले फंक्शन्स)
# ==========================================
def is_student(user):
    return not user.is_staff

def is_faculty(user):
    return user.is_staff

# ==========================================
# सुरक्षित किए गए डैशबोर्ड्स (Secure Views)
# ==========================================





@login_required(login_url='faculty_portal')
@user_passes_test(is_faculty, login_url='faculty_portal')
def faculty_dashboard(request):
    return render(request, 'dashboard/faculty_dashboard.html')


#student dashboard
@login_required(login_url='student_portal')
@user_passes_test(is_student, login_url='student_portal')
def student_dashboard(request):
    # लॉगिन किए हुए यूज़र की प्रोफाइल ढूंढो
    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        profile = None # अगर प्रोफाइल नहीं बनी है, तो क्रैश होने से बचाएगा
        
    # प्रोफाइल डेटा को HTML पेज पर भेजने के लिए Dictionary बनाएं
    context = {
        'profile': profile
    }
    return render(request, 'dashboard/student_dashboard.html', context)

# लॉगआउट करने का फंक्शन
def user_logout(request):
    from django.contrib.auth import logout # सिक्योरिटी के लिए लॉगआउट मॉड्यूल
    logout(request)
    return redirect('home') # लॉगआउट होने के बाद वापस होमपेज पर भेज देगा


#cource fee
from django.shortcuts import render
from .models import Course

def university_fee(request):
    courses = Course.objects.all()
    return render(request, 'university_fee.html', {'courses': courses})