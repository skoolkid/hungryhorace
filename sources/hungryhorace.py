# Copyright 2017 Richard Dymond (rjdymond@gmail.com)
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
        # MAZEaddr(fname)
        end, crop_rect, fname, frame, alt, (addr,) = parse_image_macro(text, index, names=('addr',))
        frames = [Frame(self._get_maze_udgs(addr), 2, 0, *crop_rect)]
        return end, self.handle_image(frames, fname, cwd, alt, 'ScreenshotImagePath')

    def expand_s(self, text, index, cwd):
        # #S/text/
        return parse_s(text, index, self.case)

    def _get_maze_udgs(self, addr):
        return [[self.maze_tiles[i] for i in self.snapshot[a:a + 32]] for a in range(addr, addr + 768, 32)]

class HungryHoraceAsmWriter(AsmWriter):
    def expand_s(self, text, index):
        # #S/text/
        return parse_s(text, index, self.case)
