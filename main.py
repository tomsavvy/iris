import kivy


SidePanel_AppMenu = {'Home Page':['on_one',None],
                     'Recent Commands':['on_two',None],
                     'In-Built Commands':['on_three',None],
                     'Operational Guide':['on_four',None]
                     }
id_AppMenu_METHOD = 0
id_AppMenu_PANEL = 1

from kivy.app import App
from kivy.garden.navigationDrawer import NavigationDrawer
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar, ActionButton, ActionPrevious
from kivy.properties import  ObjectProperty
from kivy.uix.label import Label

import speech_recognition as sr
# from jnius import cast
# from jnius import autoclass

RootApp = None
r = sr.Recognizer()

with sr.Microphone() as source:
    audio = r.listen(source)
    said = r.recognize_google(audio)

class SidePanel(BoxLayout):
    pass

class GeneralSettings(FloatLayout):
    pass

class MenuItem(Button):
    def __init__(self, **kwargs):
        super(MenuItem, self).__init__( **kwargs)
        self.bind(on_press=self.menuitem_selected)

    def menuitem_selected(self, *args):
        print self.text, SidePanel_AppMenu[self.text], SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        try:
            function_to_call = SidePanel_AppMenu[self.text][id_AppMenu_METHOD]
        except:
            print 'error in configuration of the menu'
            return
        getattr(RootApp, function_to_call)()

class AppActionBar(ActionBar):
    pass

class ActionMenu(ActionPrevious):
    def menu(self):
        print 'Action Menu'
        RootApp.toggle_sidepanel()

class ActionQuit(ActionButton):
    pass
    def menu(self):
        print 'App quit'
        RootApp.stop()


class MainPanel(BoxLayout):
    pass

class AppArea(FloatLayout):
    pass

class PageOne(FloatLayout):
    pass

class PageTwo(FloatLayout):
    pass

class PageThree(FloatLayout):
    pass

class PageFour(FloatLayout):
    pass

class AppButton(Button):

    def get_voice():
        import speech_recognition as sr
        r = sr.Recognizer()
        # with sr.Microphone() as source:
            # audio = r.listen(source)

    # to print the recognized commands
    def to_show(instance, value):
        try:
            print("You said:   " + said, value)

        except sr.UnknownValueError:
            print("Could not really get you. \n Kindly repeat",value)

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e),value)
    
    def bind_to_label(self):
        # to bind on label
        wig1 = Label(text='Say something')
        wig1.bind(on_ref_press = get_voice)
        wig2 = add_widget(Label)
        wig2.bind(on_ref_press = to_show)

class NavDrawer(NavigationDrawer):
    def __init__(self, **kwargs):
        super(NavDrawer, self).__init__( **kwargs)

    def close_sidepanel(self, animate=True):
        if self.state == 'open':
            if animate:
                self.anim_to_state('closed')
            else:
                self.state = 'closed'

class AndroidApp(App):

    def build(self):

        global RootApp
        RootApp = self

        # NavigationDrawer
        self.navigationdrawer = NavDrawer()

        # SidePanel
        side_panel = SidePanel()
        self.navigationdrawer.add_widget(side_panel)

        # MainPanel
        self.main_panel = MainPanel()

        self.navigationdrawer.anim_type = 'slide_above_anim'
        self.navigationdrawer.add_widget(self.main_panel)

        return self.navigationdrawer

    def toggle_sidepanel(self):
        self.navigationdrawer.toggle_state()

    def on_one(self):
        print 'First Page Execution'
        self._switch_main_page('Home Page', PageOne)

    def on_two(self):
        print 'Second Page Execution'
        self._switch_main_page('Recent Commands', PageTwo)
        
    def on_three(self):
        print 'Third Page Execution'
        self._switch_main_page('In-Built Commands',  PageThree)

    def on_four(self):
        print 'Operational Guide'
        self._switch_main_page('Operational Guide',  PageFour)

    def _switch_main_page(self, key,  panel):
        self.navigationdrawer.close_sidepanel()
        if not SidePanel_AppMenu[key][id_AppMenu_PANEL]:
            SidePanel_AppMenu[key][id_AppMenu_PANEL] = panel()
        main_panel = SidePanel_AppMenu[key][id_AppMenu_PANEL]
        self.navigationdrawer.remove_widget(self.main_panel)   
        self.navigationdrawer.add_widget(main_panel)      
        self.main_panel = main_panel

# Iris = autoclass('org.myapp.Iris')
# if said[0:4]=="open":
#     Iris.open(said[5:])
   
if __name__ == '__main__':
    AndroidApp().run()
