import gi
import sys
gi.require_version('Gtk','4.0')
gi.require_version("Adw",'1')
gi.require_version("GioUnix",'2.0')
from gi.repository import Gtk , Adw


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(self.box1)
        
        self.button= Gtk.Button(label="sanjai")
        self.box1.append(self.button)
        self.button.connect('clicked' , self.hello)
        
    def hello(self,button):
        print("Hi sanjai!")
        
class MyApp(Adw.Application):
   def __init__(self,**kwargs):
       super().__init__(**kwargs)
       self.connect('activate',self.on_activate)
       
   def on_activate(self,app):
       self.win = MainWindow(application=app)
       self.win.present()
       
app = MyApp(application_id="com.gtk-py.main")
app.run(sys.argv)