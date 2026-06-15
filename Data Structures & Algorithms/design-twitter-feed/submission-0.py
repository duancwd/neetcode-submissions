class Twitter:

    def __init__(self):
        self.time = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)

        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.following[userId] | {userId}

        for user in users:
            if self.tweets[user]:
                idx = len(self.tweets[user]) - 1
                tmp = self.tweets[user][idx]
                time = tmp[0]
                tweetId = tmp[1]
                heapq.heappush(
                    heap,
                    (-time, tweetId,user,idx)
                )   

        r = []

        while heap and len(r) < 10:
            neg_time, tweetId, user, idx = heapq.heappop(heap)
            r.append(tweetId)

            idx -= 1
            if idx >=0:
                 time, tweetId = self.tweets[user][idx]
                 heapq.heappush(
                    heap,
                    (-time, tweetId, user, idx)
                 )
        return r




        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
