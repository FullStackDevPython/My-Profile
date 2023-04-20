"""
Q1: Create a python script called googlesearch that provides a command line utility to
perform google search. It gives you the top links (search results) of whatever you want to
search on google.
# """
# from googlesearch import search
class Google_Search:
   def __init__(self,name_search):
      self.name = name_search
   def Gsearch(self):
      count = 0
      try :
         from googlesearch import search
      except ImportError:
         print("No Module named 'google' Found")
      for i in search(query=self.name,tld='co.in',lang='en',num=10,stop=10,pause=2):
         count += 1
         print (f'{count}. ', end="")
         print(i + '\n')
if __name__=='__main__':
   varSearch=input("Enter the text to do google search : ")
   print(f"***************Printing the top 10 results link below***************")
   gs = Google_Search(varSearch)
   gs.Gsearch()

   """
   OUTPUT : 
   Enter the text to do google search : Edureka
   ***************Printing the top 10 results link below***************
1. https://www.edureka.co/

2. https://www.youtube.com/channel/UCkw4JCwteGrDHIsyIIKo4tQ

3. https://www.youtube.com/c/edurekaIN/playlists

4. https://www.instagram.com/edureka.co/?hl=en

5. https://apps.apple.com/in/app/edureka/id1033145415

6. https://medium.com/javarevisited/10-best-edureka-courses-and-certifications-to-learn-online-e62262b6c985

7. https://customers.twilio.com/2555/edureka/

8. https://www.classcentral.com/provider/edureka

9. https://www.slideshare.net/EdurekaIN

10. https://www.facebook.com/edurekaIN/reviews
   """