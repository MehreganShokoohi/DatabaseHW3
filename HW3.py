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
        else : print('Your post should not be larger than 2200 characters.')


    def GetPosts(self):
        return self.PostList
    
    

class Twitter(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.TweetsList=[]  
    

    def CreateNewTweet(self,body):
        if len(body) < 280 :
            self.TweetsList.append(body)
        else : print('Your tweet should not be larger than 280 characters.')



    def getTweets(self):
        return self.TweetsList 
    
    
    
    
