#!/usr/bin/env python3

# Hello, world!
# Written in 2013 by Julian Marchant <onpon4@riseup.net>
#
# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any
# warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication
# along with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

import sge


class Game(sge.Game):

    def event_key_press(self, key, char):
        if key == 'escape':
            self.event_close()

    def event_close(self):
        self.end()


class Room(sge.Room):

    def event_step(self, time_passed, delta_mult):
        sge.game.project_text(font, "Hello, world!", sge.game.width / 2,
                              sge.game.height / 2, color=sge.Color("black"),
                              halign="center", valign="middle")


# Create Game object
Game()

# Create backgrounds
background = sge.Background([], sge.Color("white"))

# Load fonts
font = sge.Font()

# Create rooms
sge.game.start_room = Room(background=background)

if __name__ == '__main__':
    sge.game.start()