import requests

from bs4 import BeautifulSoup

import urllib.request


new_url = "https://www.ptt.cc/bbs/KoreaStar/index"

count = 0
for i in range(1,2):
    
    
    url1  = new_url + str(i) + ".html"
    
    r = requests.get(url1)
    
    soup = BeautifulSoup(r.text,"lxml")
    
    titles = soup.find_all(class_='title')
    
    for j, title in enumerate(titles):
        try:
            link = title.find('a')['href']
    
            if ('https' not in link):
                link = f'https://www.ptt.cc/{link}'
                count +=1
                count1 = ("A"+str(count).zfill(5))
                
                r = requests.get(link)
                
                r.encoding = "utf8"
                
                soup = BeautifulSoup(r.text,"lxml")
                
                tag_div = soup.findAll(class_ = "article-meta-value") # 作者 標題 時間
                print(tag_div[0].text)
                print(tag_div[2].text)
                print(tag_div[3].text)
                
                #---------------------
                content_of_web = soup.find(id='main-content') # 內文
                
                content_of_web = content_of_web.text
                content_of_web = content_of_web.split('\n')
                content_of_web = content_of_web[1:]
                
                content_of_target = []
                for i, content in enumerate(content_of_web):
                    if (content == ''):
                        continue
                    if (content == '--'):
                        if ((content_of_web[i+1][0] == '※') and (content_of_web[i+2][0] == '※')):
                            break
                    content_of_target.append(content)
                
                print("\n".join(content_of_target))
                #---------------------
                
                tag_puch  = soup.findAll(class_ = "f1 hl push-tag") # → 推 噓 總和
                good = 0
                bad = 0
                for puch in  tag_puch:
                    if (puch.text[0] == "→"):
                        good+=1
                        
                    else:
                        bad +=1
                        
                print("→總共有"+str(good)+"次") 
                print("噓總共有"+str(bad)+"次")       
                tag_puch1  = soup.findAll(class_ = "hl push-tag")
                
                great = 0
                for puch1 in tag_puch1:
                    if(puch1.text[0] == "推"):
                        great+=1
                print("推總共有"+str(great)+"次")
                #---------------------       
                
                
                tag_userid = soup.findAll(class_ = "f3 hl push-userid") 
                
                for user in tag_userid:
                    p1=(user.text+",")
                    
                
                tag_content = soup.findAll(class_ = "f3 push-content")
                
                for content1 in tag_content:
                    p2=(content1.text+",")
                
                tag_ipdatetime = soup.findAll(class_ = "push-ipdatetime")
                
                for ipdatetime in tag_ipdatetime:
                    p3=(ipdatetime.text+",")
                    
                t=""
                
                t=(p1+p2+p3)
                
                t =t.replace('\n', '').replace('\t', '')
                
                print(t)
                
                
                
                
                #---------------------
                


        
        except:
            link = '文章已被刪除'
        
        finally:
            title = title.text.replace('\n', '').replace('\t', '')
             
            print(f'第{[count1]}篇文章: {title} - {link}')
            print("----------------------")