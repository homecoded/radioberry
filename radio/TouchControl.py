import pygame
import math
import EventEmitter

TOUCH_SWIPE_RIGHT = 'swipe_right'
TOUCH_SWIPE_LEFT = 'swipe_right'
TOUCH_CLICK = 'click'


class TouchControl:
    def __init__(self):
        self.eventEmitter = EventEmitter.EventEmitter()
        self.last_position = (0, 0)
        self.average_position = [0, 0]
        self.sample_length = 0
        print("TouchControl initialized")

    def on(self, touch_event_name, observer):
        self.eventEmitter.add(touch_event_name, observer)

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # start listening
                self.last_position = pygame.mouse.get_pos()
                self.sample_length = 0
                self.average_position = [0, 0]

            if event.type == pygame.MOUSEBUTTONUP:
                # end listening
                current_position = pygame.mouse.get_pos()
                movement_delta = (self.last_position[0] - current_position[0],
                                  self.last_position[1] - current_position[1])
                self.average_position[0] += current_position[0]
                self.average_position[1] += current_position[1]
                self.sample_length += 1

                #determine swipe length
                length = math.sqrt(movement_delta[0]*movement_delta[0] + movement_delta[1]*movement_delta[1])
                if length < 100:
                    print("click")
                    click_position = (self.average_position[0]/self.sample_length, self.average_position[1]/self.sample_length)
                    self.eventEmitter.emit(TOUCH_CLICK, click_position)
                else:
                    # determine swipe position
                    if math.fabs(movement_delta[0]) < math.fabs(movement_delta[1]):
                        if movement_delta[0] < 0:
                            print("swipe down")
                        else:
                            print("swipe up")
                    else:
                        if movement_delta[1] < 0:
                            print("swipe left")
                        else:
                            print("swipe right")


