"""
Database models.
"""
import uuid
import os

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Lower
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

def book_image_file_path(instance, filename):
    """Generate file path for new books related image."""
    ext = os.path.splitext(filename)[1]
    filename = f'{uuid.uuid5()}{ext}'
    return os.path.join('uploads', 'books', filename)

class LanguageChoices(models.TextChoices):
    SWAHILI = "sw", "Swahili"
    ENGLISH = "en", "English"
    FRENCH = "fr", "French"
    PORTUGUESE = "pt", "Portuguese"
    CHINESE = "zh", "Chinese"
    YORUBA = "yo", "Yoruba"
    ZULU = "zu", "Zulu"
    AFRIKAANS = "af", "Afrikaans"
    ALBANIAN = "sq", "Albanian"
    AMHARIC = "am", "Amharic"
    ARABIC = "ar", "Arabic"
    ARMENIAN = "hy", "Armenian"
    AZERBAIJANI = "az", "Azerbaijani"
    BASQUE = "eu", "Basque"
    BELARUSIAN = "be", "Belarusian"
    BENGALI = "bn", "Bengali"
    BOSNIAN = "bs", "Bosnian"
    BULGARIAN = "bg", "Bulgarian"
    BURMESE = "my", "Burmese"
    CATALAN = "ca", "Catalan"
    CHINESE = "zh", "Chinese"
    CORSICAN = "co", "Corsican"
    CROATIAN = "hr", "Croatian"
    CZECH = "cs", "Czech"
    DANISH = "da", "Danish"
    DUTCH = "nl", "Dutch"
    ESPERANTO = "eo", "Esperanto"
    ESTONIAN = "et", "Estonian"
    FINNISH = "fi", "Finnish"
    GEORGIAN = "ka", "Georgian"
    GERMAN = "de", "German"
    GREEK = "el", "Greek"
    GUJARATI = "gu", "Gujarati"
    HAITIAN_CREOLE = "ht", "Haitian Creole"
    HEBREW = "he", "Hebrew"
    HINDI = "hi", "Hindi"
    HUNGARIAN = "hu", "Hungarian"
    ICELANDIC = "is", "Icelandic"
    INDONESIAN = "id", "Indonesian"
    IRISH = "ga", "Irish"
    ITALIAN = "it", "Italian"
    JAPANESE = "ja", "Japanese"
    JAVANESE = "jv", "Javanese"
    KANNADA = "kn", "Kannada"
    KAZAKH = "kk", "Kazakh"
    KHMER = "km", "Khmer"
    KOREAN = "ko", "Korean"
    KURDISH = "ku", "Kurdish"
    KYRGYZ = "ky", "Kyrgyz"
    LAO = "lo", "Lao"
    LATIN = "la", "Latin"
    LATVIAN = "lv", "Latvian"
    LITHUANIAN = "lt", "Lithuanian"
    LUXEMBOURGISH = "lb", "Luxembourgish"
    MACEDONIAN = "mk", "Macedonian"
    MALAGASY = "mg", "Malagasy"
    MALAY = "ms", "Malay"
    MALAYALAM = "ml", "Malayalam"
    MALTESE = "mt", "Maltese"
    MAORI = "mi", "Maori"
    MARATHI = "mr", "Marathi"
    MONGOLIAN = "mn", "Mongolian"
    NEPALI = "ne", "Nepali"
    NORWEGIAN = "no", "Norwegian"
    PASHTO = "ps", "Pashto"
    PERSIAN = "fa", "Persian"
    POLISH = "pl", "Polish"
    PUNJABI = "pa", "Punjabi"
    ROMANIAN = "ro", "Romanian"
    RUSSIAN = "ru", "Russian"
    SAMOAN = "sm", "Samoan"
    SERBIAN = "sr", "Serbian"
    SHONA = "sn", "Shona"
    SINDHI = "sd", "Sindhi"
    SINHALA = "si", "Sinhala"
    SLOVAK = "sk", "Slovak"
    SLOVENIAN = "sl", "Slovenian"
    SOMALI = "so", "Somali"
    SPANISH = "es", "Spanish"
    SUNDANESE = "su", "Sundanese"
    SWEDISH = "sv", "Swedish"
    TAGALOG = "tl", "Tagalog"
    TAJIK = "tg", "Tajik"
    TAMIL = "ta", "Tamil"
    TELUGU = "te", "Telugu"
    THAI = "th", "Thai"
    TURKISH = "tr", "Turkish"
    UKRAINIAN = "uk", "Ukrainian"
    URDU = "ur", "Urdu"
    UZBEK = "uz", "Uzbek"
    VIETNAMESE = "vi", "Vietnamese"
    WELSH = "cy", "Welsh"
    XHOSA = "xh", "Xhosa"
    YIDDISH = "yi", "Yiddish"


class Version(models.Model):
    """Version   for  Udereva wa kujihami book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    published_on = models.DateField()
    email =models.EmailField()
    write_name =models.CharField(max_length=255, default='')
    publisher = models.TextField(max_length=255, default='')
    version_number=models.CharField(max_length=20)
    website=models.URLField(max_length=255)
    phone_number=models.PhoneNumberField(_(""))
    version_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    profile = models.ImageField(null=True, upload_to=book_image_file_path)
    photos = GenericRelation("Photo", related_query_name='versions')
class VersionDetail(models.Model):
    """Version  object."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    version =models.ForeignKey(Version, on_delete = models.PROTECT)
    title = models.CharField(max_length=255)
    description = models.CharField(default='')
    physical_address=models.CharField(max_length=255)
    summary =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    """Book Section  for  Udereva wa kujihami book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    version =models.ForeignKey(VersionDetail, on_delete = models.PROTECT)
    section_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    photos = GenericRelation("Photo")
    
    def __str__(self):
        return self.name



class SectionDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    section =  updated_by = models.ForeignKey(Section, on_delete=models.PROTECT)
    title =models.TextField()
    description =models.TextField()
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields= ['section', 'language'],
                name='section_language_unique',
                violation_error_message= "The sections and language must be unique for each input"
            )
        ]

class MainSection(models.Model):
    """Main Section  for  Udereva wa kujihami book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    section =models.ForeignKey(Section, on_delete = models.PROTECT)
    main_section_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photos = GenericRelation("Photo")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
class MainSectionDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    main_section =  models.ForeignKey(MainSection, on_delete=models.PROTECT)
    title =models.TextField()
    description =models.TextField()
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields= ['main_section', 'language'],
                name='main_section_language_unique',
                violation_error_message= "The main section and language must be unique for each input"
            )
        ]
    
class SubSection(models.Model):
    """Sub Section  for  Udereva wa kujihami book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    main_section=models.ForeignKey(MainSection, on_delete = models.PROTECT)
    sub_section_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    photos = GenericRelation("Photo")
class SubSectionDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    sub_section =  models.ForeignKey(SubSection, on_delete=models.PROTECT)
    title =models.TextField()
    description =models.TextField()
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    
    class Meta:
        constraints=[
            models.UniqueConstraint(
                fields= ['sub_section', 'language'],
                name='sub_section_language_unique',
                violation_error_message= "The sub sections and language must be unique for each input"
            )
        ]
    
class Photo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    content_type = models.ForeignKey(ContentType, on_delete= models.PROTECT)
    object_id = models.CharField()
    content_object = GenericForeignKey('content_type', 'object_id')
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    image = models.ImageField(null=True, upload_to=book_image_file_path)
    
class Emphasize(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    stage_for =models.CharField(max_length=255)
    content_type = models.ForeignKey(ContentType, on_delete= models.PROTECT)
    object_id = models.CharField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    photos = GenericRelation("Photo")

class EmphasizeDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    emphasize = models.ForeignKey(Emphasize, on_delete = models.PROTECT)
    emphasize_number = models.SmallIntegerField()
    emphasize_title = models.TextField(max_length =255)
    emphasize_description = models.TextField()
    
    

class Stages(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    stage_for =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='updaters')
    photos = GenericRelation("Photo")

class StagesDetail(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    stage =  models.ForeignKey(Stages, on_delete=models.PROTECT, related_name='stages')
    stage_number = models.SmallIntegerField() 
    stage_name =models.TextField(max_length=255, default='')
    stage_description =models.TextField()
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='updaters')
    
class ReferenceBooks(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    name = models.TextField(max_length=255)
    description= models.TextField(default='')
    website = models.URLField(default='')
    email = models.EmailField(default='')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='updaters')
    photos = GenericRelation("Photo")
    
    
    


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    question_for =models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,related_name='updaters')
    photos = GenericRelation("Photo")

class QuestionDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid5, editable=False)
    question =  models.ForeignKey(Question, on_delete=models.PROTECT)
    question_name =models.TextField(max_length =255)
    question_description =models.TextField(default='')
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default=LanguageChoices.SWAHILI
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='updaters')
