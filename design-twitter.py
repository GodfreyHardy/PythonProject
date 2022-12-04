class Twitter:

    def __init__(self):
        self.lt = {}
        self.ft = {}
        self.time = -1
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        tmp = str(self.time)+'#'+str(tweetId)
        if userId not in self.lt:
            self.lt[userId] = []
            self.lt[userId].append(tmp)
        else:
            self.lt[userId].append(tmp)

    def getNewsFeed(self, userId: int):
        ans = []
        if userId in self.lt:
            cur = self.lt[userId][-10:][::-1]
        else:
            cur = []
        if userId in self.ft:
            for keyid in self.ft[userId]:
                res = []
                if keyid in self.lt:
                    opt = self.lt[keyid][-10:][::-1]
                else:
                    opt = []
                i = 0
                j = 0
                #print(cur)
                #print(opt)
                while i<len(cur) and j<len(opt):
                    cur_time = int(cur[i].split('#')[0])
                    opt_time = int(opt[j].split('#')[0])
                    if cur_time > opt_time:
                        res.append(cur[i])
                        i += 1
                    else:
                        res.append(opt[j])
                        j += 1
                res.extend(cur[i:])  # 获取有数据存在的元素
                res.extend(opt[j:])
                res = res[0:10]
                cur = []
                cur.extend(res)
        if len(res)==0:
            res = []
            res.extend(cur)
        for key in res:
            key = key.split('#')
            item = int(key[1])
            ans.append(item)
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.ft:
            self.ft[followerId] = {}
            self.ft[followerId][followeeId] = 1
        else:
            self.ft[followerId][followeeId] = 1

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId  in self.ft:
            if followeeId in self.ft[followerId]:
                self.ft[followerId].pop(followeeId)


if __name__ == '__main__':
    obj = Twitter()
    obj.postTweet(1, 6765)
    # obj.postTweet(5, 671)
    obj.postTweet(3, 2868)
    obj.postTweet(4, 8148)
    obj.postTweet(4, 386)
    obj.postTweet(3, 6673)
    obj.postTweet(3, 7946)
    obj.postTweet(3, 1445)
    obj.postTweet(4, 4822)
    obj.postTweet(1, 3781)
    obj.postTweet(4, 9038)
    obj.postTweet(1, 9643)
    obj.postTweet(3, 5917)
    # obj.postTweet(2, 8847)
    obj.follow(1,3)
    obj.follow(1, 4)
    # obj.follow(4, 2)
    # obj.follow(4,1)
    # obj.follow(3, 2)
    # obj.follow(3, 5)
    # obj.follow(3, 1)
    # obj.follow(2, 3)
    # obj.follow(2, 1)
    # obj.follow(2, 5)
    # obj.follow(5, 1)
    # obj.follow(5, 2)

    print(obj.getNewsFeed(1))
    # print(obj.getNewsFeed(2))
    # print(obj.getNewsFeed(3))
    # print(obj.getNewsFeed(4))
    # print(obj.getNewsFeed(5))

#[5917,9643,9038,3781,4822,1445,7946,6673,386,8148]




