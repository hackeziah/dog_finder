from django.contrib.auth.models import User
from django.db import models
import uuid


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def name_path_file(path, filename):
    import uuid
    uuid_for_filename = uuid.uuid4().hex[:6]
    filename = "{uuid}-{filename}".format(
        uuid=uuid_for_filename,
        filename=filename,
    )
    return '/'.join([path, filename])


def upload_to_image(instance, filename):
    return name_path_file('images/dogs', filename)


class Profile(User):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=168)

    def __str__(self):
        return f'{self.get_full_name()}'


class BreedType(BaseModel):
    class Meta:
        ordering = ('name',)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=62)
    description = models.CharField(max_length=62, null=True, blank=True)

    def __str__(self):
        return f'{self.name}-{self.description}'


class Dog(BaseModel):
    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=62, null=True, blank=True)
    height = models.CharField(max_length=62, null=True, blank=True)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER, max_length=64)
    image = models.ImageField(upload_to=upload_to_image)
    is_done = models.BooleanField(default=False)
    is_found = models.BooleanField(default=False)
    breed_type = models.ForeignKey(to=BreedType, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return f'{self.name}-{self.age}'


class PostLost(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True, blank=True)
    dog = models.ForeignKey(to=Dog, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.dog.name}'


class PostFound(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True, blank=True)
    dog = models.ForeignKey(to=Dog, on_delete=models.SET_NULL, null=True, blank=True)
    found_by = models.CharField(max_length=255, verbose_name="Full Name")
    contact_no = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.dog.name}'


class Message(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_id = models.ForeignKey(to=Profile, on_delete=models.SET_NULL, null=True, blank=True)
    post_lost = models.ForeignKey(to=PostLost, on_delete=models.SET_NULL, null=True, blank=True)
    post_found = models.ForeignKey(to=PostFound, on_delete=models.SET_NULL, null=True, blank=True)
    comment = models.TextField(max_length=255)

    def __str__(self):
        return f'{self.comment}'