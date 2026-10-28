from django.contrib import admin
from portal.models import Contect
from portal.models import Enquiry
from portal.models import AdmissionApplication
from .models import NewsAndAnnouncement

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'news_date')

# Register your models here.
admin.site.register(Contect)
admin.site.register(Enquiry)
admin.site.register(AdmissionApplication)
admin.site.register(NewsAndAnnouncement, NewsAdmin)


#student profile
from django.contrib import admin
from .models import NewsAndAnnouncement, StudentProfile # StudentProfile को इम्पोर्ट करें

# अगर NewsAndAnnouncement पहले से रजिस्टर है तो उसे छेड़ने की ज़रूरत नहीं
# admin.site.register(NewsAndAnnouncement)

# स्टूडेंट प्रोफाइल को रजिस्टर करें
@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_number', 'course', 'semester', 'phone_number')
    search_fields = ('user__username', 'roll_number', 'course')
    list_filter = ('course', 'semester')




from django.contrib import admin

from .models import Gallery, GallerySlider

admin.site.register(Gallery)
# अगर Gallery पहले से रजिस्टर है, तो उसके नीचे बस इसे जोड़ दो:
admin.site.register(GallerySlider)



#cource fee
from django.contrib import admin
from .models import Course, Fee

# फीस को टेबल के रूप में दिखाने के लिए
class FeeInline(admin.TabularInline):
    model = Fee
    extra = 1

# एडमिन पैनल में रजिस्टर करना
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [FeeInline]


#result

from .models import ExamResult

@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('course', 'result_title', 'session', 'upload_date')
    list_filter = ('course',) # इससे एडमिन कोर्स के हिसाब से रिजल्ट फ़िल्टर कर पाएगा





