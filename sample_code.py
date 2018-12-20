#course project


from easygui import *
import glob
state = True
j=0
path = diropenbox(msg=None, title=None, default='./folder path')
message = 'Image Viewer - Using Easygui'
choice = ('Previous', 'Next', 'Exit')
image_set = glob.glob(path + '/*.jpg')                                                          # can take any image extension
choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[0])
while state:
    if choice_select == 'Next':
        if j< (len(image_set)-1):
            j=j+1
            choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[j])
        else:
            j=0
            choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[j])
    if choice_select == 'Previous':
        j-=1
        choice_select = buttonbox(msg=message, title=' ', choices=choice, image=image_set[j])
    if choice_select == 'Exit':
        state = False
