from collections import defaultdict
import heapq

class Twitter:
    # hashMap for list of posts for each userId
    # hashMap for following [userId -> set of followeeId]
    # heap for recent tweets
    # 
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetId]
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId, tweetId):
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId):
        res = [] # ordered from most recent to least recent
        minHeap = []

        followees = self.followMap[userId] | {userId} # the user follows itself

        for followeeId in followees:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1 # last tweet index
                count, tweetId = self.tweetMap[followeeId][index] # last tweet data [count, tweeetId]
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap) # heapifys based on count [first value of the list that we appended]

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0: # means that the followee has more tweets
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId, followeeId):
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)