import tkinter
import random
from PIL import ImageTk, Image


lists = ['เเคนาดา','เเม็กซิโก','เเอฟริกาใต้','เกาหลีเหนือ','เกาหลีใต้','เดนมาร์ก','เนเธอร์เเลนด์','เมียนมา','เวเนซุเอลา','เวียดนาม','โปเเลนด์','โปรตุเกส','ไทย','กรีซ','กัมพูชา','จอร์เจีย','จีน','ชิลี','ญี่ปุ่น','ติมอร์เลสเต','นอร์เวย์','นิวซีเเลนด์','บราซิล','บรูไน','บัลเเกเรีย','บาห์เรน','ปานามา','ปารากวัย','ฝรั่งเศส','มองโกเลีย','มาเลเซีย','มาดากัสการ์','รัสเซีย','ลาว','สเปน','สวิตเซอร์เเลนด์','สวีเดน','สิงคโปร์','อเมริกา','ออสเตรเลีย','ออสเตรีย','อาร์เจนตินา','อิตาลี','อินเดีย','อินโดนีเซีย','อิรัก','อิสราเอล','อิหร่าน','อียิปต์','อุรุกวัย']
score = 0


timeleft = 60


def startGame(event):
	
	if timeleft == 60:
		
		countdown()
		
	nextColour()


def nextColour():

	global score
	global timeleft

	if timeleft > 0:

		e.focus_set()

		if e.get().lower() == lists[1].lower():
			
			score += 1

		e.delete(0, tkinter.END)
		
		random.shuffle(lists)
		imgname = "./imgs/" + lists[1] + ".jpg"
		        
		img2 = ImageTk.PhotoImage(Image.open(imgname))
		panel.configure(image=img2)
		panel.image = img2
		
		scoreLabel.config(text = "Score: " + str(score))


def countdown():

	global timeleft

	if timeleft > 0:

		timeleft -= 1
		
		timeLabel.config(text = "Time left: "
							+ str(timeleft))
								
		timeLabel.after(1000, countdown)

root = tkinter.Tk()

root.title("COLORGAME")

root.geometry("375x200")

instructions = tkinter.Label(root, text = "Type in the colour"
						"of the words, and not the word text!",
									font = ('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text = "Press enter to start",
									font = ('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 12))
				
timeLabel.pack()

label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()

img = ImageTk.PhotoImage(Image.open("./imgs/icon.jpg"))
panel = tkinter.Label(root, image=img)
panel.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()

