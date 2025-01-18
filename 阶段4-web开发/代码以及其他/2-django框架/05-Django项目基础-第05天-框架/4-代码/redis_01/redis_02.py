#encoding=utf-8
#1.导入库
from rediscluster import StrictRedisCluster


if __name__ == '__main__':

    #2.组织集群的host和端口
    nodes = [{'host':'192.168.229.148','port':'7000'},
             {'host': '192.168.229.148', 'port': '7001'},
             {'host': '192.168.229.148', 'port': '7002'},]
    try:
        #3.创建集群实例
        src=StrictRedisCluster(startup_nodes=nodes)
    except Exception as e:
        print(e)

    result = src.set('age',15)
    print(result)
