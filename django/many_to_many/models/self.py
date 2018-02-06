from django.db import models

__all__ =(
    'FacebookUser',
)

class FacebookUser (models.Model):
    '''
    자기자신을 MTM필드로 갖는모델

    '''
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # name이 이한영이며
        # 친구로 '박보영','아이유'를 가지는경우

        # #### for loop
        # friends_string = ''
        # for friend in self.friend.all():
        #     friends_string += friend.name
        #     friends_string += ','
        # friends_string = friends_string[:-2]

        # #### list comprehension
        #
        # friends_string= ','.join([friend.name for friend in self.friends.all()])

        # #### Manager의 values_list를 사용
        friends_string = ', '.join(self.friends.value_list('name',flat=True))


        return '{self.name} (친구: {friends})'.format(
            name = self.name ,
            friends = friends_string,
        )