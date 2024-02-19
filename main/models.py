from django.db import models
from django.utils.html import mark_safe


class HeaderText(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'HeaderText'  
        verbose_name_plural = 'HeaderText'  


class FeatureItem(models.Model):

    icon = models.ImageField(upload_to='media')
    title = models.CharField(max_length=30)
    text = models.TextField()

    def img_preview(self):
        return mark_safe(f'<img src="{self.icon.url}" width=60px>')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Feature Item' 
        verbose_name_plural = 'Feature Items'    


class About(models.Model):

    icon = models.ImageField(upload_to='media')
    title = models.CharField(max_length=30)
    text = models.TextField()


    def img_preview(self):
        return mark_safe(f'<img src="{self.icon.url}" width=60px>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'About Company' 
        verbose_name_plural = 'About Company'    


class WorkProcess(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Work Process'
        verbose_name_plural = 'Work Process'    


class WorkProcessItem(models.Model):
    icon = models.ImageField(upload_to='media')
    title = models.CharField(max_length=40)
    text = models.TextField()

    def img_preview(self):
        return mark_safe(f'<img src="{self.icon.url}" width=60px>')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Work Process Item'
        verbose_name_plural = 'Work Process Items'    


class Row(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Row'  
        verbose_name_plural = 'Row'

class Team_content(models.Model):
    icon = models.ImageField(upload_to='media')
    message = models.TextField()
    user_name = models.CharField(max_length=35)
    job = models.CharField(max_length=35)

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = 'Team content'
        verbose_name_plural = 'Team contents'


class Pricing_Plans(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Pricing Plan'
        verbose_name_plural = 'Pricing Plans'


class Price(models.Model):
    pricing_header = models.CharField(max_length=25)
    currency = models.CharField(max_length=10)
    price = models.CharField(max_length=25)
    period = models.CharField(max_length=25)
    active1 = models.CharField(max_length=35)
    active2 = models.CharField(max_length=35)
    active3 = models.CharField(max_length=35)
    active4 = models.CharField(max_length=35)
    active5 = models.CharField(max_length=35)
    active6 = models.CharField(max_length=35)
    main_button = models.CharField(max_length=35)

    def __str__(self):
        return self.pricing_header
    
    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Price'

class Counter(models.Model):
    projects_count = models.CharField(max_length=15)
    projects = models.CharField(max_length=20)
    happy_clients_count = models.CharField(max_length=15)
    happy_clients = models.CharField(max_length=20)
    awards_wins_count = models.CharField(max_length=15)
    awards_wins = models.CharField(max_length=20)
    countries_count = models.CharField(max_length=15)
    countries = models.CharField(max_length=20)

    def __str__(self):
        return self.projects_count
    
    class Meta:
        verbose_name = 'Counter'
        verbose_name_plural = 'Counters'

class Blog(models.Model):
    title = models.CharField(max_length=15)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

class Blog_list(models.Model):
    pictures = models.ImageField(upload_to='media')
    title = models.CharField(max_length=40)
    text = models.TextField()
    read_more = models.CharField(max_length=15)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog list'
        verbose_name_plural = 'Blog lists'



class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'ContactUs'
        verbose_name_plural = 'ContactUs'
    
