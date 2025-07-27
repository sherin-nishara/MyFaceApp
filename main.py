import cv2
from kivy.app import App
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture

class FaceApp(App):
    def build(self):
        self.img = Image()
        self.capture = cv2.VideoCapture(0)  
        Clock.schedule_interval(self.update, 1.0 / 30.0)
        return self.img

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            buf = cv2.flip(frame, 0).tobytes()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.img.texture = texture

    def on_stop(self):
        self.capture.release()

if __name__ == '__main__':
    FaceApp().run()
