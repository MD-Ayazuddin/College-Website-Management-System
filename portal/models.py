from django.db import models

# Create your models here.
class Contect(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Enquiry(models.Model):
    studentName = models.CharField(max_length=122)
    dob = models.DateField()
    courceCategory = models.CharField(max_length=122)
    courseInterested = models.CharField(max_length=122)
    city = models.CharField(max_length=122)
    zipCode = models.CharField(max_length=12)
    phoneNo = models.CharField(max_length=12)
    email = models.EmailField()
    date = models.DateField()

    def __str__(self):
        return self.studentName



class AdmissionApplication(models.Model):
    # =========================================
    # 1. Course & Session Details
    # =========================================
    course_applied = models.CharField(max_length=50)
    session = models.CharField(max_length=30)

    # =========================================
    # 2. Personal Information
    # =========================================
    student_name = models.CharField(max_length=150)
    father_name = models.CharField(max_length=150)
    mother_name = models.CharField(max_length=150)
    dob = models.DateField()
    gender = models.CharField(max_length=20)
    nationality = models.CharField(max_length=50, default="Indian")
    marital_status = models.CharField(max_length=30)
    background = models.CharField(max_length=30)
    physically_handicapped = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    religion = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    mark_of_identification = models.CharField(max_length=200, blank=True, null=True)

    # =========================================
    # 3. Document Uploads (Photos & Sign)
    # =========================================
    # Note: Pillow library is required for ImageField (pip install Pillow)
    student_photo = models.ImageField(upload_to='admission_docs/photos/')
    student_signature = models.ImageField(upload_to='admission_docs/signatures/')

    # =========================================
    # 4. Contact & Address Details
    # =========================================
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    
    # Permanent Address
    permanent_address = models.TextField()
    per_district = models.CharField(max_length=100)
    per_state = models.CharField(max_length=100)
    per_pincode = models.CharField(max_length=10)

    # Correspondence Address
    correspondence_address = models.TextField()
    corr_district = models.CharField(max_length=100)
    corr_state = models.CharField(max_length=100)
    corr_pincode = models.CharField(max_length=10)

    # =========================================
    # 5. Previous Educational Qualification
    # =========================================
    # 10th Details
    tenth_board = models.CharField(max_length=150)
    tenth_pass_year = models.CharField(max_length=10)
    tenth_percentage = models.CharField(max_length=10)
    tenth_division = models.CharField(max_length=20)

    # 12th Details
    twelth_board = models.CharField(max_length=150)
    twelth_pass_year = models.CharField(max_length=10)
    twelth_percentage = models.CharField(max_length=10)
    twelth_division = models.CharField(max_length=20)

    # UG Details (Optional - blank=True allowed because 12th pass students won't have this)
    ug_board = models.CharField(max_length=150, blank=True, null=True)
    ug_pass_year = models.CharField(max_length=10, blank=True, null=True)
    ug_percentage = models.CharField(max_length=10, blank=True, null=True)
    ug_division = models.CharField(max_length=20, blank=True, null=True)

    # PG Details (Optional)
    pg_board = models.CharField(max_length=150, blank=True, null=True)
    pg_pass_year = models.CharField(max_length=10, blank=True, null=True)
    pg_percentage = models.CharField(max_length=10, blank=True, null=True)
    pg_division = models.CharField(max_length=20, blank=True, null=True)

    # Auto-generated Timestamp
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name

#def __str__(self):
        #return f"{self.student_name} - {self.course_applied} ({self.session})"

#News
class NewsAndAnnouncement(models.Model):
    title = models.CharField(max_length=500)
    news_date = models.DateField()
    
    description = models.TextField(blank=True, null=True, help_text="")
    
    link = models.URLField(blank=True, null=True, help_text="") 

    def __str__(self):
        return self.title

#student profile
from django.db import models
from django.contrib.auth.models import User # Django का डिफ़ॉल्ट यूज़र टेबल

COURSE_CHOICES = (
    ('BCA', 'BCA'),
    ('BBA', 'BBA'),
    ('CABA-MDTP', 'CABA-MDTP'),
    ('Diploma in Urdu', 'Diploma in Urdu'),
)

SEMESTER_CHOICES = (
    ('Semester 1', 'Semester 1'),
    ('Semester 2', 'Semester 2'),
    ('Semester 3', 'Semester 3'),
    ('Semester 4', 'Semester 4'),
    ('Semester 5', 'Semester 5'),
    ('Semester 6', 'Semester 6'),
)

class StudentProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    
    # स्टूडेंट की एक्स्ट्रा डिटेल्स
    roll_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50, choices=COURSE_CHOICES)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    
    # प्रोफाइल पिक्चर (ऑप्शनल) - इमेजेज़ सेव करने के लिए
    profile_pic = models.ImageField(upload_to='student_pics/', default='default_student.png', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.course} ({self.roll_number})"


#gallary
class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery_images/')
    upload_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class GallerySlider(models.Model):
    image = models.ImageField(upload_to='gallery_slider/')
    caption = models.CharField(max_length=200, blank=True, null=True, help_text="फोटो के ऊपर दिखने वाला टेक्स्ट")

    def __str__(self):
        return self.caption if self.caption else f"Slide {self.id}"


#cource fee
from django.db import models

# 1. कोर्स की डिटेल
class Course(models.Model):
    name = models.CharField(max_length=100)
    university = models.CharField(max_length=200, default="Affiliated to Maulana Mazharul Haque Arabic & Persian University (MMHAPU)")
    duration = models.CharField(max_length=50)
    seats = models.CharField(max_length=20, default="-")
    description = models.TextField()
    eligibility = models.TextField()

    def __str__(self):
        return self.name

# 2. फीस की टेबल (जो कोर्स से जुड़ी होगी)
class Fee(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="fees")
    fee_type = models.CharField(max_length=100)  # जैसे: 1st Year Fee
    amount = models.CharField(max_length=50)     # जैसे: ₹ 10,500


#result result

from django.db import models

class ExamResult(models.Model):
    # एडमिन पैनल के ड्रॉपडाउन के लिए कोर्सेज की लिस्ट
    COURSE_CHOICES = [
        ('BCA', 'Bachelor of Computer Application (BCA - 3 Years)'),
        ('BBA', 'Bachelor of Business Administration (BBA - 3 Years)'),
        ('BLIS', 'Bachelor of Library and Information Science (BLIS - 1 Year)'),
        ('PRIS', 'Diploma in Accountancy for Panchayati Raj Institutions (PRIS - 1 Year)'),
        ('DIPLOMA', 'Diploma Courses (1 Year)'),
    ]

    course = models.CharField(max_length=20, choices=COURSE_CHOICES, verbose_name="Select Course")
    result_title = models.CharField(max_length=200, verbose_name="Result (e.g., BCA Part-1)")
    session = models.CharField(max_length=100, verbose_name="Examination Session")
    pdf_file = models.FileField(upload_to='results_pdf/', verbose_name="Upload PDF File")
    upload_date = models.DateField(auto_now_add=True) # यह डेट अपने-आप सेव हो जाएगी

    def __str__(self):
        return f"{self.course} - {self.result_title}"