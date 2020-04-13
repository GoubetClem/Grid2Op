# Copyright (c) 2019-2020, RTE (https://www.rte-france.com)
# See AUTHORS.txt
# This Source Code Form is subject to the terms of the Mozilla Public License, version 2.0.
# If a copy of the Mozilla Public License, version 2.0 was not distributed with this file,
# you can obtain one at http://mozilla.org/MPL/2.0/.
# SPDX-License-Identifier: MPL-2.0
# This file is part of Grid2Op, Grid2Op a testbed platform to model sequential decision making in power systems.

from grid2op.Action.BaseAction import BaseAction


class DontAct(BaseAction):
    """
    This class is model the action where you force someone to do absolutely nothing. It is not the "do nothing"
    action.

    This is not the "do nothing" action. This class will not implement any way to modify the grid. Any attempt to
    modify it will fail.

    """

    def __init__(self, gridobj):
        """
        See the definition of :func:`BaseAction.__init__` and of :class:`BaseAction` for more information. Nothing
        more is done
        in this constructor.

        """
        BaseAction.__init__(self, gridobj)

        self.authorized_keys = set()
        self.attr_list_vect = []

    def update(self, dict_):
        """
        It has the particularity to not use `dict_`

        Parameters
        ----------
        dict_: ``dict``
            A dictionnary, not taken into account for this specific class.

        Returns
        -------

        """
        return self

    def sample(self, space_prng):
        """
        Sampling among the set containing only the do nothing action is rather easy. It returns always the
        "do nothing" action.
        """
        return self
