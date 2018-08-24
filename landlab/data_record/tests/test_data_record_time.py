# -*- coding: utf-8 -*-
"""
Unit tests for landlab.data_record.data_record.DataRecord
Dimension = time

Last updated 8/24/2018

"""

import pytest
import numpy as np
from landlab import RasterModelGrid

grid = RasterModelGrid((3,3))
shape = (3,3)
time=[0.]
data_vars={'mean_elevation' : (['time'], np.array([100]))}
attrs={'time_units' : 'y'}

def test_dr_time_name(dr_time):
    assert dr_time._name == 'DataRecord'

def test_grid_shape(dr_time):
    assert dr_time._grid.number_of_node_rows == shape[0]
    assert dr_time._grid.number_of_node_columns == shape[1]

def test_permitted_locations(dr_time):
    assert dr_time.permitted_locations == grid.groups

def test_coordinates(dr_time):
    assert len(dr_time.dims) == 1
    assert list(dr_time.time.values) == list(np.array(time))
    assert list(dr_time.time_coordinates) == list(np.array(time))
    # properties:
    assert dr_time.number_of_timesteps == 1
    assert dr_time.earliest_time == 0.
    assert dr_time.latest_time == 0.
    assert np.isnan(dr_time.prior_time)
    # no item_id coord:
    with pytest.raises(AttributeError):
        dr_time.item_id
        dr_time.item_coordinates
        dr_time.number_of_items

def test_variable_names(dr_time):
    assert dr_time.variable_names == ['mean_elevation']