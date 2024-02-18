from ._anvil_designer import MAINTemplate
from anvil import *
import anvil.server

class MAIN(MAINTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def aboutMe_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(self.aboutCard)

  def reminders_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(self.remindersCard)

  def date_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(self.dateCard)
    today = datetime.date.today()
    self.text_area_1 = today.strftime('%Y-%m-%d')

  def chat_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(self.chatCard)

  def emergency_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(self.emerCard)

  def primary_color_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    output = anvil.server.call('be_my_memory',self.text_box_1.text)
    print(output)
    if output:
      self.label_2.visible = True
      self.label_2.text = output.capitalize()
