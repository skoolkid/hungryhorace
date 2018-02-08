# Copyright 2017, 2018 Richard Dymond (rjdymond@gmail.com)
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.

from skoolkit.graphics import Frame, Udg
from skoolkit.skoolasm import AsmWriter
from skoolkit.skoolhtml import HtmlWriter
from skoolkit.skoolmacro import parse_image_macro, parse_strings

def parse_s(text, index, case):
    end, s = parse_strings(text, index, 1)
    return end, s.lower() if case == 1 else s

class HungryHoraceHtmlWriter(HtmlWriter):
    def init(self):
        self.maze_tiles = [Udg(61, self.snapshot[a:a + 8]) for a in range(31735, 31815, 8)]
        self.maze_tiles[2].attr = 60 # flower
        self.maze_tiles[3].attr = 56 # entrance/exit

    def expand_maze(self, text, index, cwd):
        # MAZEaddr[,scale,locaddr](fname)
        names = ('addr', 'scale', 'locaddr')
        end, crop_rect, fname, frame, alt, (addr, scale, loc_addr) = parse_image_macro(text, index, (2, 0), names)
        frames = [Frame(self._get_maze_udgs(addr, loc_addr), scale, 0, *crop_rect)]
        return end, self.handle_image(frames, fname, cwd, alt, 'ScreenshotImagePath')

    def expand_s(self, text, index, cwd):
        # #S/text/
        return parse_s(text, index, self.case)

    def _get_maze_udgs(self, m_addr, l_addr):
        maze_udgs = [[self.maze_tiles[i] for i in self.snapshot[a:a + 32]] for a in range(m_addr, m_addr + 768, 32)]
        if l_addr:
            for s_addr, attr, loc_addr in (
                    (32519, 58, l_addr),     # Bell
                    (32327, 59, l_addr + 2), # Guard
                    (32103, 57, l_addr + 4)  # Horace
            ):
                sprite_udgs = [Udg(attr, self.snapshot[a:a + 8]) for a in range(s_addr, s_addr + 32, 8)]
                location = self.snapshot[loc_addr] + 256 * self.snapshot[loc_addr + 1]
                x, y = location % 32, location // 2048 * 8 + location // 32 & 31
                maze_udgs[y][x:x + 2] = sprite_udgs[:2]
                maze_udgs[y + 1][x:x + 2] = sprite_udgs[2:]
        return maze_udgs

class HungryHoraceAsmWriter(AsmWriter):
    def expand_s(self, text, index):
        # #S/text/
        return parse_s(text, index, self.case)
