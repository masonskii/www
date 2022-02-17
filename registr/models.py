from django.db import models


# Create your models here.
class Role(models.Model):
    role = models.CharField(max_length=20)


class Person(models.Model):
    login = models.CharField(max_length=20, null=False, help_text='basic login information', unique=True)
    password = models.CharField(max_length=32, null=False, help_text='basic login information', unique=True)
    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    ndName = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.DateField()
    roleId = models.ManyToManyField(
        Role,
        on_delete=models.CASCADE,
    )
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    registrationDate = models.DateTimeField(auto_now=True)
    lastEntrance = models.DateTimeField(auto_now=True)


class Department(models.Model):
    title = models.CharField(max_length=50, null=False)


class Specialization(models.Model):
    title = models.CharField(max_length=20, null=False)


class Machine(models.Model):
    title = models.CharField(max_length=30)
    pas = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)
    costPerHour = models.DecimalField(max_digits=19, decimal_places=10)


class FabPro(models.Model):
    title = models.CharField(max_length=30, null=False)
    duration = models.DurationField()
    projects = models.BooleanField(default=False)
    teatherId = models.IntegerField()  # TODO: НИХЕР ТУТ НЕ INTEGERFIELD! УЗНАТЬ У АЛЕКСАНДРА КАКАЯ ЖЕ ХУЙНЯ ТУТ ПРОИСХОДИТ
    machineId = models.ForeignKey(
        Machine,
        null=True,
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(default=False)

class Task(models.Model):
    customerId = models.ForeignKey(

    )
    implementerId = models.ForeignKey(

    )
    title = models.CharField(max_length=20, null=False)


class MachineBooking(models.Model):
    MachineId = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
    )
    customerId = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
    )
    startTime = models.TimeField(

    )
    endTime = models.TimeField(

    )
    bookingData = models.DateField(

    )


class PersonSpecs(models.Model):
    SpecId = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )


class Membership(models.Model):
    DepartmentId = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )


class PersonSkills(models.Model):
    FabProId = models.ForeignKey(
        FabPro,
        on_delete=models.CASCADE,
    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )
    Term = models.IntegerField()


class PersonPasses(models.Model):
    MachineId = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,

    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )


class Email(models.Model):
    email = models.EmailField(max_length=50)
    personId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )


class MobilePhone(models.Model):
    phone = models.CharField(max_length=12)
    personId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )


class Transfer(models.Model):
    senderId = models.ForeignKey(

    )
    recipientId = models.ForeignKey(

    )
    summary = models.DecimalField(
        max_digits=19, decimal_places=10
    )
    tDate = models.DateTimeField()


