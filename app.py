import pygame
import sys
from blue import ConnectHC06
import speech_recognition

pygame.init()
pygame.display.set_caption("Application Projet Arduino")
pygame.display.set_icon(pygame.image.load('img/arduino.png'))
font = pygame.font.Font('freesansbold.ttf', 16)


class Application(ConnectHC06):
    def __init__(self, width, height, addr, channel):
        ConnectHC06.__init__(self, addr, channel)
        self.width = width
        self.height = height
        self.talking = False
        self.content = ""
        self.current_speed = 5
        self.recognizer = speech_recognition.Recognizer()
        self.screen = pygame.display.set_mode((self.width, self.height))

    def reset_speed(self):
        self.one = pygame.image.load("img/one.png")
        self.two = pygame.image.load("img/two.png")
        self.three = pygame.image.load("img/three.png")
        self.four = pygame.image.load("img/four.png")
        self.five = pygame.image.load("img/five.png")

    def change_speed(self):
        if self.current_speed == 1:
            self.one = self.colorize(self.one, (255, 0, 0))
        elif self.current_speed == 2:
            self.two = self.colorize(self.two, (255, 0, 0))
        elif self.current_speed == 3:
            self.three = self.colorize(self.three, (255, 0, 0))
        elif self.current_speed == 4:
            self.four = self.colorize(self.four, (255, 0, 0))
        elif self.current_speed == 5:
            self.five = self.colorize(self.five, (255, 0, 0))

    def load_images(self):
        self.up = pygame.image.load("img/up.png")
        self.up_rect = self.up.get_rect(center=(150, 80))

        self.down = pygame.image.load("img/down.png")
        self.down_rect = self.down.get_rect(center=(150, 220))

        self.left = pygame.image.load("img/left.png")
        self.left_rect = self.left.get_rect(center=(80, 150))

        self.right = pygame.image.load("img/right.png")
        self.right_rect = self.right.get_rect(center=(220, 150))

        self.circle = pygame.image.load("img/circle.png")
        self.circle_rect = self.circle.get_rect(center=(150, 150))

        self.voice = pygame.image.load("img/voice.png")
        self.voice_rect = self.voice.get_rect(center=(260, 40))

        self.one = pygame.image.load("img/one.png")
        self.one_rect = self.one.get_rect(center=(45, 300))

        self.two = pygame.image.load("img/two.png")
        self.two_rect = self.two.get_rect(center=(115, 300))

        self.three = pygame.image.load("img/three.png")
        self.three_rect = self.three.get_rect(center=(185, 300))

        self.four = pygame.image.load("img/four.png")
        self.four_rect = self.four.get_rect(center=(250, 300))

        self.five = pygame.image.load("img/five.png")
        self.five_rect = self.five.get_rect(center=(315, 300))

        self.blue = pygame.image.load("img/bluetooth.png")
        self.blue_rect = self.five.get_rect(center=(310, 150))

    def colorize(self, image, newColor):
        # copy image object
        image = image.copy()
        # format = (color,0) && rectstyle object = NULL && flags = blend_rgba_add to add the color
        image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
        return image

    def speech(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = self.recognizer.listen(mic, phrase_time_limit=1)
                text = self.recognizer.recognize_google(audio, language="fr").lower()
                self.send("*"+text+"#")
                self.content = "LAST : " + text
        except:
            self.content = "Error..."

    def handle_keydown(self, event):
        if event.key == pygame.K_UP:
            self.up = self.colorize(self.up, (255, 0, 0))
        if event.key == pygame.K_DOWN:
            self.down = self.colorize(self.down, (255, 0, 0))
        if event.key == pygame.K_LEFT:
            self.left = self.colorize(self.left, (255, 0, 0))
        if event.key == pygame.K_RIGHT:
            self.right = self.colorize(self.right, (255, 0, 0))
        if event.key == pygame.K_SPACE:
            self.circle = self.colorize(self.circle, (255, 0, 0))
        if event.key == pygame.K_e:
            self.talking = True
        if event.key == pygame.K_c:
            self.close_connection()
            self.connect()

    def handle_keyup(self, event):
        if event.key == pygame.K_UP:
            self.up = pygame.image.load("img/up.png")
            app.send("a#")
        if event.key == pygame.K_DOWN:
            self.down = pygame.image.load("img/down.png")
            app.send("b#")
        if event.key == pygame.K_LEFT:
            self.left = pygame.image.load("img/left.png")
            app.send("g#")
        if event.key == pygame.K_RIGHT:
            self.right = pygame.image.load("img/right.png")
            app.send("d#")
        if event.key == pygame.K_SPACE:
            self.circle = pygame.image.load("img/circle.png")
            app.send("s#")
        if event.key == pygame.K_1:
            self.reset_speed()
            self.current_speed = 1
            self.send("*"+str(self.current_speed)+"#")
        if event.key == pygame.K_2:
            self.reset_speed()
            self.current_speed = 2
            self.send("*"+str(self.current_speed)+"#")
        if event.key == pygame.K_3:
            self.reset_speed()
            self.current_speed = 3
            self.send("*"+str(self.current_speed)+"#")
        if event.key == pygame.K_4:
            self.reset_speed()
            self.current_speed = 4
            self.send("*"+str(self.current_speed)+"#")
        if event.key == pygame.K_5:
            self.reset_speed()
            self.current_speed = 5
            self.send("*"+str(self.current_speed)+"#")

    def checkp1(self):
        if(self.talking):
            self.voice = self.colorize(self.voice, (255, 0, 0))
            self.content = "Listening..."
            self.text = font.render(self.content, True, (0, 0, 0))
            self.textRect = self.text.get_rect(center=(70, 20))
        else:
            self.text = font.render(self.content, True, (0, 0, 0))
            self.textRect = self.text.get_rect(center=(70, 20))
            self.voice = pygame.image.load("img/voice.png")

    def checkp2(self):
        if(self.talking):
            self.speech()
            self.talking = False

    def draw(self):
        self.screen.fill((220, 220, 220))
        self.screen.blit(self.up, self.up_rect)
        self.screen.blit(self.circle, self.circle_rect)
        self.screen.blit(self.voice, self.voice_rect)
        self.screen.blit(self.down, self.down_rect)
        self.screen.blit(self.left, self.left_rect)
        self.screen.blit(self.right, self.right_rect)
        self.screen.blit(self.one, self.one_rect)
        self.screen.blit(self.two, self.two_rect)
        self.screen.blit(self.three, self.three_rect)
        self.screen.blit(self.four, self.four_rect)
        self.screen.blit(self.five, self.five_rect)
        self.screen.blit(self.blue, self.blue_rect)
        pygame.display.update()


if __name__ == "__main__":
    app = Application(350, 350, "98:D3:71:FD:8A:B2", 1)
    #app.connect()
    app.load_images()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                app.close_connection()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                app.handle_keydown(event)
            if event.type == pygame.KEYUP:
                app.handle_keyup(event)

        app.change_speed()
        app.checkp1()
        app.draw()
        app.checkp2()
