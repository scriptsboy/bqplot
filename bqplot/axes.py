# Copyright 2015 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""

====
Axes
====

.. currentmodule:: bqplot.axes

.. autosummary::
   :toctree: generate/


   Axis
   ColorAxis
"""
from IPython.html.widgets import Widget
from IPython.utils.traitlets import Int, Unicode, Instance, Enum, Dict, Bool

from .scales import Scale, ColorScale, DateScale, DateColorScale, LogScale
from .traits import NumpyArray


class Axis(Widget):

    """A line axis."""
    icon = 'fa-arrows'
    orientation = Enum(['vertical', 'horizontal'], default_value='horizontal', sync=True)
    side = Enum(['bottom', 'top', 'left', 'right'], default_value='bottom', sync=True)
    label = Unicode(sync=True)
    grid_lines = Enum(['none', 'solid', 'dashed'], default_value='none', sync=True)   # Style of the grid on the X-axis
    tick_format = Unicode(sync=True)
    scale = Instance(Scale, sync=True)
    num_ticks = Int(default_value=None, sync=True, allow_none=True)
    tick_values = NumpyArray(sync=True)
    offset = Dict(dict(), sync=True)
    label_location = Enum(['start', 'end', 'middle'], default_value='middle', sync=True)  # Placement of the label along the axis
    label_color = Unicode(None, sync=True, allow_none=True)
    grid_color = Unicode(None, sync=True, allow_none=True)
    color = Unicode(None, sync=True, allow_none=True)
    label_offset = Unicode(default_value=None, sync=True, allow_none=True)  # Displacement from the axis line. Units allowed are em px and ex.
    # Positive values are away from the figure and negative values are towards
    # the figure with resepect to the axis line.

    visible = Bool(True, sync=True)  # Attribute to control the visibility of the axis
    scale = Instance(Scale, sync=True)
    num_ticks = Int(default_value=None, sync=True, allow_none=True)
    _view_name = Unicode('bqplot.Axis', sync=True)
    _model_name = Unicode('bqplot.AxisModel', sync=True)
    _ipython_display_ = None  # We cannot display an axis outside of a figure.

    def _tick_format_default(self):
        if isinstance(self.scale, DateScale):
            # perhaps we should have a DateAxis subclass instead of this checking
            return '%b-%y'
        elif isinstance(self.scale, LogScale):
            return '.3g'
        else:
            return '.0f'


class ColorAxis(Axis):

    """A colorbar axis."""

    orientation = Enum(['vertical', 'horizontal'], default_value='horizontal', sync=True)
    side = Enum(['bottom', 'top', 'left', 'right'], default_value='bottom', sync=True)
    label = Unicode(sync=True)
    scale = Instance(ColorScale, sync=True)
    tick_format = Unicode(sync=True)
    _view_name = Unicode('bqplot.ColorAxis', sync=True)
    _model_name = Unicode('bqplot.AxisModel', sync=True)

    def _tick_format_default(self):
        if isinstance(self.scale, DateColorScale):
            return '%b-%y'
        else:
            return '.0f'