# -*- coding: utf-8 -*-
"""
/***************************************************************************
 LandslidesSurvey
                                 A QGIS plugin
 Description...
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-08-20
        copyright            : (C) 2019 by Edoardo Pessina
        email                : edoardo2.pessina@mail.polimi.it
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load LandslidesSurvey class from file LandslidesSurvey.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .landslides_survey import LandslidesSurvey
    return LandslidesSurvey(iface)