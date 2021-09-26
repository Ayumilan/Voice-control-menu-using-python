import os
import speech_recognition as sr
import pyttsx3
import warnings

def basic():
	while True:
		print("Welcome to the Basic Section : ")
		pyttsx3.speak("In Basic section, you can open notepad,control panel, calculator,chrome browser and know about date and time ")
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nBasic-Service is running....\n")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\tBasic-Service ")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING =======")
			audio = r.listen(source)
			print(audio)
			print("processing your requested Basic instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				q = q.lower()
				if ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("calculator" in q) or ("cal" in q))):
					pyttsx3.speak("Opening calculator")
					os.system("calc")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("chrome" in q) or ("browser" in q) or ("google" in q))):
					pyttsx3.speak("opening Chrome ")
					os.system("start chrome")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("control panel" in q) or ("control" in q) or ("panel" in q))):
					pyttsx3.speak("opening control panel")
					os.system("control panel")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("notepad" in q) or ("editor" in q))):
					pyttsx3.speak("opening notepad")
					os.system("notepad")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("show date" in q) or ("date" in q)):
					pyttsx3.speak("Today date is ..")
					os.system("date")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("show time" in q) or ("time" in q)):
					pyttsx3.speak("Current time is ..")
					os.system("time")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This basic-Service Does not exist in the system, we update it later========")
			except:
				print("======== Cannot recog your requested basic-instruction!!!... Kindly say again... ========")

def OTT():
	while True:
		print("Welcome to the OTT Section : ")
		pyttsx3.speak("In OTT section, you can enjoy watching different platfrom like hotstar, sony liv, amazon prime video")
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nOTT-Service is running....\n")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\tOTT-Service ")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING =======")
			audio = r.listen(source)
			print(audio)
			print("processing your requested instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				q = q.lower()
				if ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("hotstar" in q) or ("star" in q))):
					pyttsx3.speak("Opening Hotstar")
					os.system("start chrome /incognito https://www.hotstar.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("sony" in q) or ("sony liv" in q) or ("sonyliv" in q))):
					pyttsx3.speak("opening Sony LIV ")
					os.system("start chrome /incognito https://www.sonyliv.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("prime video" in q) or ("prime" in q) or ("amazon" in q))):
					pyttsx3.speak("opening Amazon prime Video")
					os.system("start chrome /incognito https://www.primevideo.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This basic-Service Does not exist in the system, we update it later========")
			except:
				print("======== Cannot recog your requested basic-instruction!!!... Kindly say again... ========")

def Social():
	while True:
		print("Welcome to the Social Media Section : ")
		pyttsx3.speak("In Social media you can use facebook, twitter, linkedin, Instagram")
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nSocial media-Service is running....\n")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\tSocial Media-Service ")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING =======")
			audio = r.listen(source)
			print(audio)
			print("processing your requested instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				q = q.lower()
				if ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("facebook" in q) or ("fb" in q))):
					pyttsx3.speak("Opening Facebok")
					os.system("start chrome /incognito https://www.facebook.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("twitter" in q) or ("tweet" in q) or ("tweets" in q))):
					pyttsx3.speak("opening Twitter ")
					os.system("start chrome /incognito https://www.twitter.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("link" in q) or ("linkedin" in q) or ("din" in q))):
					pyttsx3.speak("opening linkedin")
					os.system("start chrome /incognito https://www.linkedin.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("run" in q) or ("execute" in q ) or ("launch" in q) or("open" in q)) and (("reel" in q) or ("insta" in q) or ("instagram" in q))):
					pyttsx3.speak("opening Instagram")
					os.system("start chrome /incognito https://www.instagram.com/")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This basic-Service Does not exist in the system, we update it later========")
			except:
				print("======== Cannot recog your requested basic-instruction!!!... Kindly say again... ========")


def K8S():
	while True:
		print("Welcome to the Kubernetes Section : ")
		pyttsx3.speak("In this section you can use kubernetes service to deploy and test ")
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nkubernetes-Service is running....\n")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\tKubernetes-Service is Running")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			
			print("\n======== LISTENING (Service-type is 'K8S') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested Kubernetes instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				q = q.lower()
				print("======== Given Kuberenetes Instruction is ======== \n",q,"\n")
				if ((("start" in q) or ("launch"  in q)) and (("service" in q) or ("minikube" in q))):
					os.system("minikube start")
					pyttsx3.speak("Starting the minikube for this service")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("list" in q) or ("show"  in q)) and (("launched deployment" in q) or ("deploymnet" in q) or (" all deployment" in q) or ("deploy" in q))):
					os.system("kubectl get deployments")
					pyttsx3.speak("Showing all deployments")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("list" in q) or ("show"  in q)) and (("launched pods" in q) or ("pod" in q) or (" all pods" in q) or ("p o d" in q))):
					os.system("kubectl get pods")
					pyttsx3.speak("Showing all pods")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("create" in q) or ("launch"  in q)) and (("deployment" in q) or ("deployments" in q))):
					print("Enter deployment name:")
					d=input()
					print("Enter image name:")
					i=input()
					os.system("kubectl create deployment {} --image {}".format(d,i))
					pyttsx3.speak("Creating deployment")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("describe" in q)) and (("deployment" in q) or ("deployments" in q))):
					print("Enter deployment name:")
					e=input()
					os.system("kubectl describe deployment {}".format(e))
					pyttsx3.speak("Full deatil about the deployment")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("describe" in q)) and (("pod" in q) or ("pods" in q))):
					print("Enter pod name:")
					w=input()
					os.system("kubectl describe pod {}".format(w))
					pyttsx3.speak("Full deatil about the pod")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("scale" in q)) and (("deployment" in q) or ("deployments" in q))):
					print("Enter deployment name:")
					v=input()
					print("Enter no of replica:")
					u=int(input())
					os.system("kubectl scale deployment {} --replicas={}".format(v,u))
					pyttsx3.speak("Scaling the deployment")
					input("\n======== Please, Press Enter to continue ========\n")
				elif ((("expose" in q)) and (("deployment" in q) or ("deployments" in q))):
					print("Enter deployment name:")
					t=input()
					os.system("kubectl expose deployment {} --port=80 --type=NodePort".format(t))
					pyttsx3.speak("Exposing the deployment to port 80 with Nodeport")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("delete all" in q) or ("delete"  in q)):
					os.system("kubectl delete all --all")
					pyttsx3.speak("Deleting all the pods and deployments")
					input("\n======== Please, Press Enter to continue ========\n")
				elif (("exit" in q) or ("quit" in q) or ("stop" in q)):
					os.system("minikube stop")
					pyttsx3.speak("Exiting... the service")
					print("Exiting....")
					break
				
				else:  
					print("======== This K8S-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested K8S-instruction!!!... Kindly say again... ========")

def AWS():
	print("Welcome to the Amazon Web Services Section : ")
	pyttsx3.speak("In this section you can use AWS service on cloud using command line")
	while True:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			pyttsx3.speak("\nAWS-Service is running....\n")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print("\t\tAWS-Service is Running")
			print("----------------------------------------------------------")
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	
			print("\n======== LISTENING (Service-type is 'AWS') ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested AWS instructions....please wait!!!\n")
			try:
				q = r.recognize_google(audio) 
				q = q.lower()
				print("======== Given AWS Instruction is ======== \n",q,"\n")
				if (("version" in q) and (("a ws" in q) or ("aws" in q) or ("aw s" in q) or ("a w s" in q))):
					os.system("aws --version")
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("key" in q) and ("create" in q)):
					print("Enter Key Name:")
					b=input()
					os.system("aws ec2 create-key-pair --key-name {}".format(b))
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("sg" in q) or ("security group" in q)) and ("create" in q)):
					print("Enter Security-Group Name:")
					c=input()
					print("Give Description Here:")
					d=input()
					os.system("aws ec2 create-security-group --group-name {} --description \"{}\" ".format(c,d))
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("instance" in q) or ("Instance" in q)) and ("launch" in q)):
					print("Enter Image-ID")
					e=input()
					print("Enter Instance-Type")
					f=input()
					print("Enter Key-Pair Name")
					g=input()
					print("Enter Security-Group ID:")
					h=input()
					os.system("aws ec2 run-instances --image-id {} --instance-type {} --count 1 --subnet-id subnet-601c1508 --key-name {} --security-group-ids {} ".format(e,f,g,h))
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("ebs" in q) or ("e b s" in q)) and ("create" in q)):
					print("Enter the Zone Name:")
					i=input()
					os.system("aws ec2 create-volume --availability-zone {} --size 1 --volume-type gp2".format(i))
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif ((("ebs" in q) or ("e b s" in q)) and ("attach" in q)):
					print("Enter Instance-ID:")
					j=input()
					print("Enter Volume-ID:")
					k=input()
					os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/sdk".format(j,k))
					input("\n======== Please, Press Enter to continue ========\n")
					
				elif (("exit" in q) or ("Exit" in q) or ("quit" in q) or ("Quit" in q) or ("stop" in q) or ("Stop" in q)):
					pyttsx3.speak("Exiting...")
					print("Exiting....")
					break
				else:  
					print("======== This AWS-Service Does not exist in the system ========")
			
			except:
				print("======== Cannot recog your requested aws-instruction!!!... Kindly say again... ========")

def service():
	try:
		r = sr.Recognizer()
		r.energy_threshold=7000
		with sr.Microphone() as source:
			print("\n======== LISTENING (Services) ========")
			audio = r.listen(source)
			print(audio)
			print("processing your requested services....please wait!!!\n")
			global q
			q = r.recognize_google(audio)
			q=q.lower()
			print(q)   
		return q
				
	except:
		print("======== Failed to detect requested services...Kindly, say again!!! ========")


while True:
	pyttsx3.speak("Welcome to the voice control menu created by AYUSH using python, In this menu there are 5 section ")
	print("----------------------------------------------------------")
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("\tWelcome to the Voice Control Menu ")
	print("----------------------------------------------------------")
	print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
	print("\n1. Basic \n2. Social Media \n3. OTT platform \n4. Kubernetes \n5. AWS")
	service_type=service()
	if service_type is None:
		service_type=[]
	if( ("kubernetes" in service_type) or ("kubernete" in service_type ) or ("kube" in service_type )):
		K8S()
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\tTerminated Kubernetes-Service")
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		
	elif( ("aw s" in service_type) or ("aws" in service_type )  or ("a ws" in service_type) or ("a w s" in service_type) or ("e w s" in service_type)):
		AWS()
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\tTerminated AWS-Service")
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		
	elif( ("ott" in service_type) or ("otp" in service_type )  or ("o t t" in service_type) or ("platform" in service_type)):
		OTT()
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\tTerminated OTT-Service")
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		
	elif( ("social" in service_type) or ("media" in service_type )):
		Social()
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\tTerminated Social media-Service")
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		
	elif( ("basic" in service_type) or ("basics" in service_type )):
		basic()
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\tTerminated Basic-Service")
		print("-----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		
	elif service_type == []:
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print("\t\tDidn't hear any voice , Kindly say!!!!")
		print("----------------------------------------------------------")
		print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

	elif (("exiting" in service_type) or ("exit" in service_type) or ("quit" in service_type) or ("stop" in service_type) or ("kill" in service_type)):
		warnings.filterwarnings("ignore")
		pyttsx3.speak("Exiting From Services ")
		print("======== Exiting From Services ========")
		os.system(exit())
	else: 
		print("======== This Service Does not exist in the system ========")