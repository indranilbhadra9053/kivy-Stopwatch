from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty,ListProperty,StringProperty
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window

from kivy.utils import get_color_from_hex
import time

Window.clearcolor = get_color_from_hex('#ceeef7')

class stopwatchapp(App):
	ms=NumericProperty(00)
	sec=NumericProperty(00)
	min=NumericProperty(0)
	speed=NumericProperty(0)
	i=NumericProperty(0)
	e=0
	e_sec=0
	fontcolor=StringProperty("#ffff")
	font_color=StringProperty("#ffff")
	duty=StringProperty("Stop")
	
	
	def increment(self):
		if self.speed==0:
			#This is the main function ...🥰🥰🥰😅😂😂
			self.event=Clock.schedule_interval( lambda dt :(setattr(self,'ms', self.ms+1 if self.ms<99 else 0),(setattr(self,'sec',self.sec+1 if self.sec<59 else 0) if self.ms == 99 else self.sec),(setattr(self,'min',self.min+1 if self.sec==0 else self.min)if self.ms==99 else self.min)),0.0001/10000)
			
			self.fontcolor="#490e67b3"
			self.e=self.event
			#self.e_sec=self.event_sec
			self.duty="Stop"
			self.speed+=1
		
		
		
	def minus(self):
		if self.ms!=0 or self.sec!=0 or self.min!=0:
			self.font_color="#490e67b3"
			Clock.unschedule(self.e)
			
			self.speed=0
			self.i=self.i+1
			if self.i==1:
				self.duty="Clear"
			if self.i==2:
				self.clear()
		
		
		
	def font_color_change(self):
		self.fontcolor="#ffff"
		self.font_color="#ffff"
	def clear(self):
		self.ms=0
		self.sec=0
		self.min=0
		self.duty="Stop"
		self.i=0
		Clock.unschedule(self.e)
	
		
stopwatchapp().run()
