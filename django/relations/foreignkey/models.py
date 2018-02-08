from django.db import models


# verbose_name지정
# admin에 등록
# migration생성 및 적용


class Car(models.Model):
    manufacturer = models.ForeignKey(
        # 순서가 바껴 있어서 Manufacturer를 못찾을 떈 에러가 나므로
        # 문자열로 바꿔놓으면 나중에 찾아서 바꾸어준다.
        'Manufacturer',
        on_delete=models.CASCADE,  # 부모가 사라지면 자식도 사라짐
        verbose_name='제조사',
    )
    name = models.CharField('모델명', max_length=60)

    def __str__(self):
        # 현대 아반떼 <- 와 같이 출력되도록 처리
        return f'{self.manufacturer.name} {self.name}'


class Manufacturer(models.Model):
    name = models.CharField('제조사명', max_length=50)

    def __str__(self):
        return self.name


# 자기저신을 다디앨로 연결할수 있음
# 비어잇어도 상관없고, 연결된 객체가 삭제되면 함꼐 삭제되지 않고
class Person(models.Model):
    name = models.CharField(max_length=60)
    teacher = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,  # 부모가 사라져도 자식은 안사라짐
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Type(models.Model):
    type_number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.type_number} | {self.name}'


class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number:03},{self.name} (self.type.name)'
