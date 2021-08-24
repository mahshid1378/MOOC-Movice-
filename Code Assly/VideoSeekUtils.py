from youtube_transcript_api import YouTubeTranscriptApi
import os


def test(ip,key):
    s = ""
    if len(ip)==31:
        s = ip[20:]
    elif len(ip)==44:
        s = ip[32:]
    else:
        s = ip[len(ip)-12:]
    
    #print(key)
    st = result(s,key)
    k = "\n".join(st)
    print(k)
    result1(k)
 
def result(video_id,key1):
    res = YouTubeTranscriptApi.get_transcript(video_id)
    
    resSort = []
    
    
    count=1
    for key in range(len(res)):
        d = res[key]
        s = d["text"]
        if type(s) == type(""):
            val = s.find(key1)
            if val != -1:
                 resSort.append(str(d["text"]+"-----"+str(int(d["start"])//60)+"."+str(int(d["start"])%60)+" min"+"\n"))
    
    return resSort
    
def result1(st):
    with open("finalresult.html","w") as opfile:
            opfile.write("""<!doctype html>
        <html lang="en">
         <head>
          <title>Video-Seek</title>
           <style type="text/css">
            body {
                background-color: #FFFFFF;
                font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
                
            }
        	p{
        		color: #1432cc;
        		
        	}
        	h1{
        		color:black;
        	}
        	h3{
        		text-decoration: underline;
        	}
        	#firdiv{
        		background-color:yellow;
        		color:black;
        		margin:2px;
        		width:100%
        	}
        	#secdiv{
        		margin:60px;
        		background-color: cream;
        		color:#e01d1d;
        		width:100%;
        		height:100%
        	}
            #divi{
    		color:#1432cc;
    		font-size:127%
    	    }
            #image{
    		float:right;
    	    }
            </style> 
         </head>
         <body>
        	<div id="firdiv">
        		<h1 align=center>Video-Seek Result</h1>
        	</div>
        	<div id="secdiv">
        		<h3>"""+st+"""</h3>
        	</div>
         </body>
        </html>
        """)        
    os.startfile("finalresult.html")