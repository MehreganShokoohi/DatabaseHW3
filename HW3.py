class SocialMedia:
    def __init__(self, name):
        self.Apps = name

    def getName(self):
        return self.Apps

class Instagram(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.PostList=[]  
    
    
    def PublishNewPost(self,body):
        if len(body) < 2200 :
            self.PostList.append(body)
        else : print('larg size')


    def GetPosts(self):
        return self.PostList
    
    

class Twitter(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.TweetsList=[]  
    

    def CreateNewTweet(self,body):
        if len(body) < 280 :
            self.TweetsList.append(body)
        else : print('larg size')


    def getTweets(self):
        return self.TweetsList 
    
    