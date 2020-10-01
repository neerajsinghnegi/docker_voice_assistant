import time
import pyttsx3 as pyt
from urllib import request
import speech_recognition as sr

def speak(text):
    engine=pyt.init()
    voices=engine.getProperty('voices')
    #engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-70)
    engine.say(text)
    engine.runAndWait()
"""
reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_all_running.py")
data = reqst.read()
html = data.decode("utf-8")
print(html)
"""

r = sr.Recognizer()

while True:
  print("""
                                                Welcome to Docker Menu
                                              __________________________

                                                     Containers
                                                     ----------
                                1 Show Running Containers        2 All Containers
                                3 Launch Container               4 Stop Container Service	
                                5 Start Container Service        6 Delete Container 		
                                7 Delete All Containers	
                                
                                
                                                      Setting
                                                     ----------
                                8 Monitor Docker CPU
                                9 Active Ports
                                
                                                      Images
                                                      --------
                                10 Available Docker Images      11 Create Image
                                12 Remove Image
                                
                                                       Exit""")

  with sr.Microphone() as source:
      print("listening....")
      print('neeraj say....')
      speak('neeraj say....')
      sound = r.listen(source)
    
      text = r.recognize_google(sound)
      print("got it.. " + text)

  #docker run
  if (("run" in text) or ("Run" in text) or ("launch" in text) or ("Launch" in text)) and (("docker" in text) or ("container" in text)):
    
    #container name
    with sr.Microphone() as source:
        print("Give name to the container")
        speak("Give name to the container")
        cont = r.listen(source)
        c_name = r.recognize_google(cont)
        print("setting container..{}".format(c_name))
        #speak("setting container..{}".format(c_name))

    #container image
    with sr.Microphone() as source:
        print("""Select Image
        1. centos:latest
        2. centos:7""")
        speak('Available Images 1 -> centos:latest 2 -> centos:7')

        img = r.listen(source)
        i_name = r.recognize_google(img)
        print("setting containr image..{}".format(i_name))
        speak("setting containr image..{}".format(i_name))

    #choose image
    if (i_name == "1"):
        i_name = "centos:latest"
        speak("launching docker {} container with image {}".format(c_name,i_name))
        reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/iiec.py?x={0}&y={1}".format(c_name,i_name))
        data = reqst.read()
        html = data.decode("utf-8")
        print(html)
        time.sleep(3)

    elif (i_name == "2"):
        i_name = "centos:7"
        speak("launching docker {} container with image {}".format(c_name,i_name))
        reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/iiec.py?x={0}&y={1}".format(c_name,i_name))
        data = reqst.read()
        html = data.decode("utf-8")
        print(html)
        time.sleep(3)
    else:
        print("try again..")
        speak("try again..")

  #docker stop
  elif (("stop" in text) or ("close" in text)) and ("container" in text):
    with sr.Microphone() as source:
  
      print("Tell me which container do you stop..")
      speak("Tell me which container do you stop..")

      cont = r.listen(source)
      c_name = r.recognize_google(cont)
    
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_stop.py?x={0}".format(c_name))
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    print("stopped container..{}".format(c_name))
    speak("stopped container..{}".format(c_name))
    time.sleep(3)

  #docker start
  elif ("start" in text) and ("container" in text):
    with sr.Microphone() as source:
  
      print("Tell me which container do you start..")
      speak("Tell me which container do you start..")

      cont = r.listen(source)
      c_name = r.recognize_google(cont)
    
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_start.py?x={0}".format(c_name))
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    print("started container..{}".format(c_name))
    speak("started container..{}".format(c_name))
    time.sleep(3)

  elif ("show" in text) and (("images" in text) or ("image" in text)):
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_images.py")
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    speak("showing docker images..")
    time.sleep(3)

  #create image
  elif ("create" in text) and (("images" in text) or ("image" in text)):   

    with sr.Microphone() as source:
        print("Which container do you want to create image")
        speak("Which container do you want to create image")
        cont = r.listen(source)
        c_name = r.recognize_google(cont)

    with sr.Microphone() as source:
        print("Give name to your new image..")
        speak("Give name to your new image..")
        img = r.listen(source)
        i_name = r.recognize_google(img)
        i_name = i_name.lower()
        print(i_name)
        print("setting image {0} from {1} container".format(i_name,c_name))
        speak("setting image {0} from {1} container".format(i_name,c_name))

    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_image_create.py?x={0}&y={1}".format(c_name,i_name))
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    speak("created docker image..{0}".format(i_name))
    time.sleep(3)
  
  #docker remove image
  elif (("delete" in text) or ("remove" in text)) and (("image" in text) or ("images" in text)):
    with sr.Microphone() as source:
  
      print("Tell me which image do you want to remove..")
      speak("Tell me which image do you want remove..")

      img = r.listen(source)
      i_name = r.recognize_google(cont)
      i_name = i_name.lower()
    
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_image_remove.py?x={0}".format(i_name))
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    print("removed image..{}".format(i_name))
    speak("removed image..{}".format(i_name))
    time.sleep(3)

  #show running containers
  elif ("show" in text) and (("container" in text) or ("containers" in text)):   
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_all_running.py")
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    speak("showing all running containers..")
    time.sleep(3)

  #show all containers (stopped or removed)
  elif ("all" in text) and (("container" in text) or ("containers" in text)):   
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_all.py")
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    speak("showing all containers..")
    time.sleep(3)

  #show active ports
  elif ("active" in text) and (("port" in text) or ("ports" in text)):   
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_active_ports.py")
    data = reqst.read()
    html = data.decode("utf-8")
    speak("showing all active ports..")
    print(html)
    time.sleep(3)

  #docker remove
  elif (("remove" in text) or ("delete" in text)) and ("container" in text):
    with sr.Microphone() as source:
  
      print("Tell me which container do you remove..")
      speak("Tell me which container do you remove..")

      cont = r.listen(source)
      c_name = r.recognize_google(cont)
    
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_remove.py?x={0}".format(c_name))
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    print("removed container..{}".format(c_name))
    speak("removed container..{}".format(c_name))
    time.sleep(3)

  #docker remove all containers
  elif (("remove" in text) or ("delete" in text)) and ("all" in text) and ("container" in text):
    with sr.Microphone() as source:
  
      print("Tell me which container do you remove..")
      speak("Tell me which container do you remove..")

      cont = r.listen(source)
      c_name = r.recognize_google(cont)
    
    reqst = request.urlopen("http://192.168.43.101/cgi-bin/docker/docker_container_remove.py?x={0}".format(c_name))
    data = reqst.read()
    html = data.decode("utf-8")
    print(html)
    print("removed all containers..")
    speak("removed all containers..")
    time.sleep(3)

  #close assistant
  elif (("close" in text) or ("exit" in text) or ("quit" in text)):
    speak("closing")
    break

  #try again
  else:
    print("try one more time..")
    speak("try one more time..")