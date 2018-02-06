from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    """
    내가 A를 follow 함
        나는 A의 follower
        A는 나의 followee

    A와 내가 서로 follow함
        나와 A는 friend

    Block기능이 있어야함

    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',  ##+로 지정하면 역참조가 없어짐
    )

    def __str__(self):
        return self.name

    def following(self):
        """
        내가 팔로잉 하고 있는 user목록 을 가져옴

        :return:
        """
        #내가 from_user이며 type이 팔로잉인 Relation의 쿼리셋
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING
        )
        #위에서 정제한 쿼리셋에서 'to-user'값만 리스트로 가져옴(내가 팔로잉하는 유저의 pk리스트)
        following_pk_list = following_relations.values_list('TO_USER', flat=True)
        #Twitter User테이블에서 pk가
        #바로 윗줄에서 만든 following_pk_list (내가 팔로잉 하는 유저의 pk리스트)
        #  에 포함 되는 USER목록을 following_users변수로 할당
        following_users = TwitterUser.objects.filter(pk__in= following_pk_list)
        return following_users


class Relation(models.Model):
    """
    유저간의 관계를 정의하는 모델
    단순히 자신의 MTM이 아닌 중개모델의 역할을 함
    추가적으로 받는 정보는 관계의 타입 (팔로잉 또는 차단 )
    """

    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'

    CHOICES_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단 ')
    )

    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 from_user인 경우의 relation목록을 가져오고싶을경우
        related_name='relations_by_from_user',
    )
    TO_USER = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user인 경우의 relation목록을 가져오고 싶을 경우
        related_name='relations_by_to_user',
    )
    type = models.CharField(max_length=1, choices=CHOICES_TYPE)
