
import orm, asyncio, sys
from models import User


async def test(loop):
    await orm.create_pool(loop=loop, user='www', password='www', db='awesome')

    u = User(name='Test1', email='test1@example.com', passwd='1234567890', image='about:blank')

    await u.save()

if __name__=='__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)

# 实测代码正确！注意，该程序只能执行一次！创建数据库文件时，一段代码 unique key `idx_email` (`email`), 表示email是唯一的，你再次运行
# 就等于再次保存一个同样的 email ,当然报错了！下面就是报错的提示，还害得我卡了很久！
#  raise errorclass(errno, errval)
#  pymysql.err.IntegrityError: (1062, "Duplicate entry 'test@example.com' for key 'idx_email'")