import gi
import sys
gi.require_version('Gtk','4.0')
gi.require_version("Adw",'1')
gi.require_version("GioUnix",'2.0')
from gi.repository import Gtk , Adw , Gdk , GLib , Gio


css_provider = Gtk.CssProvider()
css_provider.load_from_path("style.css")
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider , Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.box2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box3 = Gtk.Box(orientation= Gtk.Orientation.VERTICAL)
        
       
        
        self.button= Gtk.Button(label="sanjai")
        # self.box1.append(self.button)
        self.button.connect('clicked' , self.hello)
        
        
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
        
        
        f = Gtk.FileFilter()
        f.set_name("Image Files")
        f.add_mime_type("image/jpeg")
        f.add_mime_type("image/png")
        
        filters = Gio.ListStore.new(Gtk.FileFilter)
        filters.append(f)
        
        
        self.open_dialog = Gtk.FileDialog.new()
        self.open_dialog.set_title("select a file")
        self.open_button.connect("clicked", self.show_dialog)
        self.open_dialog.set_filters(filters)
        self.open_dialog.set_default_filter(f)
           
        self.show_info_button = Gtk.Button(label="show info")
        self.show_info_button.connect("clicked",self.show_info_bar)
        self.header.pack_start(self.show_info_button)
        # create new action 
        action = Gio.SimpleAction.new("something",None)
        action.connect("activate", self.do_something)
        
        # action 2
        action2 = Gio.SimpleAction.new("about",None)
        action2.connect("activate", self.show_about)
        
        # create an new menu containing the action 
        menu = Gio.Menu()
        menu.append("Do Something","win.something")
        menu.append("About","win.about")
        
        # create popover 
        self.popover = Gtk.PopoverMenu()
        self.popover.set_menu_model(menu)
        
        # create new menu button 
        self.hamburger = Gtk.MenuButton()
        self.hamburger.set_popover(self.popover)
        self.hamburger.set_icon_name("open-menu-symbolic")
        
        self.banner = Adw.Banner()
        self.banner.set_title("Gtk-py")
        self.banner.set_revealed(False)
        
        # self.info = Gtk.InfoBar()
        # self.info.set_message_type(Gtk.MessageType.INFO)
        # self.info.set_show_close_button(True) # added close button 
        # self.info.set_revealed(False)
        
        self.info_revealer = Gtk.Revealer()
        self.info_revealer.set_reveal_child(False)
        self.info_revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_DOWN)
        self.info_revealer.set_transition_duration(200)
        self.info_revealer.get_child_revealed()
        
        # horizontal box for info content 
        self.info_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=6)
        self.info_box.set_css_classes(["toolbar","infobar"])
        
        
        
        self.info_icon = Gtk.Image.new_from_icon_name("dialog-information-symbolic")
        self.info_box.append(self.info_icon)
        
        
        self.info_label = Gtk.Label(label="This is an info message")
        self.info_label.set_hexpand(True)
        self.info_label.set_halign(Gtk.Align.START)
        
        
        self.info_box.append(self.info_label)
        
        # connect close button
        self.info_close_button = Gtk.Button()
        self.info_close_button.set_icon_name("window-close-symbolic")
        self.info_close_button.add_css_class("flat")
        self.info_close_button.connect("clicked", self.hide_info_bar)
        self.info_box.append(self.info_close_button)
        
        # add  info revealer box
        self.info_revealer.set_child(self.info_box)
        
        # a verical bar to hold the info bar
        self.main_container = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.main_container.append(self.info_revealer)
        
        # add main_container below the InfoBar
        self.main_container.append(self.box1)
        
        # set the main container at child  
        self.set_child(self.main_container)
        
        # Add menu button to headerbar
        self.header.pack_start(self.hamburger)
        self.add_action(action)
        self.add_action(action2)
        
        
        
        
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
        
    def show_dialog(self,widget):
        self.open_dialog.open(self,None,self.open_dialog_open_callback)
        
    
        
    def open_dialog_open_callback(self, dialog, result):
            try:
                file = dialog.open_finish(result)
                if file is not None:
                    print(f"File path is {file.get_path()}")
                    # Show file selection in InfoBar with filename
                    filename = file.get_basename()  # Gets just the filename, not full path
                    self.show_custom_info(f"File selected: {filename}", "info")
                    
                else:
                    # Show message when no file was selected (dialog was cancelled)
                    self.show_custom_info("File selection was cancelled","warning")
                    
            except GLib.Error as error:
                print(f"Error opening file: {error.message}")
                # Show error in InfoBar
                self.show_custom_info(f"Error: {error.message}","error")
                
            
    def do_something(self,action,params):
        print("Doing something")
        
    def show_about(self,action,params):
        self.about = Gtk.AboutDialog()
        self.about.set_transient_for(self) # Make the dialog panel to appen on the panel
        self.about.set_modal(True)   #Make the parent window unresponse when dialog is showing
        
        self.about.set_authors(["sanjai"])
        self.about.set_copyright("Copyright 2025 sanjai")
        self.about.set_license_type(Gtk.License.GPL_3_0)
        self.about.set_website("https://github.com/sanjai-gtk/gtk-py")
        self.about.set_website_label("GitHub")
        self.about.set_version("1.0")
        self.about.set_logo_icon_name("org.gtk-py.com") # The icon will need to be added to appropriate location
                                                         # E.g. /usr/share/icons/hicolor/scalable/apps/org.example.example.svg
        
        self.about.set_visible(True)
      
       # Show about dialog action in InfoBar
        self.custom_info_label("About dialog opened!","info")
        
        
      
    def show_custom_info(self,message,message_type="info"):
        """Show the InfoBar with a message with its types"""
        
        self.info_label.set_text(message)
        self.info_revealer.set_reveal_child(True)
        
        # update the icon based on the message type
        if message_type == "error":
            self.info_icon.set_from_icon_name("dialog-error-symbolic")
            self.info_box.set_css_classes(["error-bar","rounded-box"])
        
        elif message_type == "warning":
            self.info_icon.set_from_icon_name("dialog-warning-symbolic")
            self.info_box.set_css_classes(["warning-bar","rounded-box"])
            
        elif message_type == "info":
            self.info_icon.set_from_icon_name("dialog-information-symbolic")
            self.info_box.set_css_classes(["info-bar","rounded-box"])
            
        elif message_type == "success":
            self.info_icon.set_from_icon_name("dialog-information-symbolic")
            self.info_box.set_css_classes(["success-bar","rounded-box"])
            
        else:
            self.info_icon.set_from_icon_name("dialog-information-symbolic")
            self.info_box.set_css_classes(["info-bar","rounded-box"])
            
        
    def hide_info_bar(self,widget=None):
        """Hide custom infobar """
        self.info_revealer.set_reveal_child(False)
        
    
        
    
    def show_info_bar(self,widget):
       "show infobar component bar with messages" 
       self.banner.set_title("InfoBar is now visible! You can close it with the X button.")
       self.banner.set_revealed(True)
       
       # show using custom info bar
       self.show_custom_info("Custom InfoBar s now visible! you can close it with the X button.","info")
       
        
class MyApp(Adw.Application):
   def __init__(self,**kwargs):
       super().__init__(**kwargs)
       self.connect('activate',self.on_activate)
       self.win = None
   def on_activate(self,app):
       self.win = MainWindow(application=app)
       self.win.present()
       
    
        
       
app = MyApp(application_id="com.gtk-py.main")
app.run(sys.argv)