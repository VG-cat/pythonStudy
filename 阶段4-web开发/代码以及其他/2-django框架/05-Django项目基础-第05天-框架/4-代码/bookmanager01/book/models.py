from django.db import models

# Create your models here.
"""
1. ORM
    表 --> 类
    字段 --> 属性

2. 模型类需要继承自models.Model

3. 模型类会自动为我们添加(生成)一个主键

4. 属性名=属性类型(选项)

    属性名: 不要使用 python,mysql关键字
            不要使用 连续的下划线(__)
    属性类型: 和mysql的类型类似的
    选项:  charfiled 必须设置 max_length
            varchar(M)

          null   是否为空
          unique 唯一
          default 设置默认值
          verbose_name 主要是 admin后台显示
"""
"""
书籍表:
    id,name,pub_date,readcount,commentcount,is_delete
"""
class BookInfo(models.Model):

    # 属性名=属性类型(选项)
    name=models.CharField(max_length=10,unique=True,verbose_name='名字')
    #发布日期
    pub_date=models.DateField(null=True)
    #阅读量
    readcount=models.IntegerField(default=0)
    #评论量
    commentcount=models.IntegerField(default=0)
    #是否逻辑删除
    is_delete=models.BooleanField(default=False)

    # django 自动为我们添加了一个属性 这个属性就可以通过 书籍查询人物信息
    # peopleinfo_set

    class Meta:
        # 改表名
        db_table='bookinfo'
        # 修改后台admin的显示信息的配置
        verbose_name='admin'


    def __str__(self):
        return self.name


# 准备人物列表信息的模型类
class PeopleInfo(models.Model):
    # 有序字典
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    name = models.CharField(max_length=20, verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    description = models.CharField(max_length=200, null=True, verbose_name='描述信息')

    # 一个黑帮老大 n个小弟 1:n
    # 黑帮老大被判死刑
    # 小弟:   1. 劫狱 不让老大死
    #         2.  小弟自己混
    #          3. 老大死 小弟跟着死

    # 书籍: 人物  1:n
    # 西游记:  孙悟空,白骨精
    # on_delete
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')  # 外键
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name




