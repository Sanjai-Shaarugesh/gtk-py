import gi
import sys
gi.require_version('Gtk','4.0')
gi.require_version("Adw",'1')
gi.require_version("GioUnix",'2.0')
from gi.repository import Gtk , Adw , Gdk


css_provider = Gtk.CssProvider()
css_provider.load_from_path("style.css")
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider , Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        
        # self.set_child(self.box1)
        
        self.button= Gtk.Button(label="sanjai")
        # self.box1.append(self.button)
        self.button.connect('clicked' , self.hello)
        
        self.set_child(self.box1)
        self.box1.append(self.box2)
        self.box1.append(self.box3)
        
        self.box2.append(self.button)
        
        self.check = Gtk.CheckButton(label="And goodbye?")
        self.check.connect('toggled', self.hello)
        self.box2.append(self.check)
        
        
        self.radio1 = Gtk.CheckButton(label="test")
        self.radio2 = Gtk.CheckButton(label="test")
        self.radio3 = Gtk.CheckButton(label="test")
        
        self.radio2.set_group(self.radio1)
        self.radio3.set_group(self.radio1)
        
        self.radio1.connect("toggled",self.radio_toggled)
        self.radio2.connect("toggled",self.radio_toggled)
        self.radio3.connect("toggled",self.radio_toggled)
        
        self.box2.append(self.radio1)
        self.box2.append(self.radio2)
        self.box2.append(self.radio3)
        
        
        self.switch_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        
        self.switch = Gtk.Switch()
        self.switch.set_active(True)
        self.switch.connect("state-set",self.switch_toggled)
        
        self.switch_box.append(self.switch)
        self.box3.append(self.switch_box)
        
        self.slider = Gtk.Scale()
        self.slider.set_digits(0)
        self.slider.set_range(0,10)
        self.slider.set_draw_value(True)
        self.slider.set_value(5)
        self.slider.connect('value-changed',self.slider_changed)
        self.box2.append(self.slider)
        
        
        self.header = Gtk.HeaderBar()
        self.set_titlebar(self.header)
        
        self.open_button = Gtk.Button(label="open")
        self.header.pack_start(self.open_button)
        
        self.open_button.set_icon_name("document-open-symbolic")
        
        self.label = Gtk.Label(label="Gtk-py")
        self.box2.append(self.label)
        self.label.set_css_classes(["label"])
           
        
        self.set_default_size(600,250)
        self.set_title("Gtk-py")
        
        
        
    def switch_toggled(self,widget,state):
            print(f"The switch has been switched {'on' if state else 'off'} ")
        
    def hello(self,widget):
        print("Hi sanjai!")
        
        if self.check.get_active():
            print("Goodbye sanjai!")
            self.close()
            
    def radio_toggled(self,widget):
        if self.radio1.get_active():
            print("Radio 1 is selected")
        elif self.radio2.get_active():
            print("Radio 2 is selected")
        elif self.radio3.get_active():
            print("Radio 3 is selected")
        
    def slider_changed(self,widget):
        print(int(widget.get_value()))
        
class MyApp(Adw.Application):
   def __init__(self,**kwargs):
       super().__init__(**kwargs)
       self.connect('activate',self.on_activate)
       
   def on_activate(self,app):
       self.win = MainWindow(application=app)
       self.win.present()
       
app = MyApp(application_id="com.gtk-py.main")
app.run(sys.argv)
