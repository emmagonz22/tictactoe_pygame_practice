# -*- coding: utf-8 -*-
import pygame as py
class Animation:
    def __init__(self, x, y, action, path,  frame_duration):
        self.action = action
        self.path = path
        self.frame_duration = frame_duration
        self.flip = False
        self.frame = 0
        self.image = ''
        self.x = x
        self.y = y
    #global animation_frames
    animation_frames = {}
    animation_database = {}
    #animation_database[block_animation.action] = block_animation.load_animation() 
    def get_action(self):
        return self.action
    def load_animation(self):
        #global animation_frames
        animation_name = self.path.split('/')[-1]
        animation_frames_data = []
        n=0
        for frame in self.frame_duration:
            animation_frame_id = animation_name + '_' + str(n)
            img_loc = self.path + '/' + animation_frame_id + '.png'
            animation_image = py.image.load(img_loc)
            animation_image.set_colorkey((255,255,255))
            self.animation_frames[animation_frame_id] = animation_image.copy()
            for i in range(frame):
                animation_frames_data.append(animation_frame_id)
            n+=1
        return animation_frames_data
    def add_animation_database(self, add):
        self.animation_database[add] = self.load_animation() 
        
    def animation_update(self):
        self.frame += 1
        if(self.frame >= len(self.animation_database[self.action])):
            self.frame = 0
        image_id = self.animation_database[self.action][self.frame]
        self.image = self.animation_frames[image_id] 
    def render(self, win):
        win.blit(self.image, (self.x,self.y))
        
    def change_action(self, action_var, frame, new_value):
        if(action_var != new_value):
            action_var = new_value
            frame = 0
        return action_var, frame
    def get_animation_frame(self):
        return self.animation_frames
    
    #def render(self, win):