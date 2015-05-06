# -*- encoding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) Odoo Colombia (Community).
# Co-Authors    David Arnold (devCO)
#               Juan Pablo Aries (devCO)
#               Luis Miguel Varon
#               Hector Ivan Valencia (TIX)
#               Cinxgler Mariaca (IDU-STRT-I+D+I)
#
# Collaborators Nhomar Hernandez (Vauxoo)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields


class res_city(models.Model):
    _name = 'res.country.state.city'
    _description = 'Ciudad'

    name = fields.Char(
        string=u'City',
        required=True,
    )
    state_id = fields.Many2one(
        'res.country.state',
        string=u'State',
    )
    phone_prefix = fields.Char(
        string=u'Phone Prefix',
    )
    statcode = fields.Char(
        string=u'DANE Code',
        size=5,
        help='Code of the Colombian statistical department',
    )
    country_id = fields.Many2one(
        'res.country',
        string=u'Country',
        related='state_id.country_id',
        store=True,
        readonly=True,
    )


class res_city_district(models.Model):
    _name = 'res.country.state.city.district'
    _description = 'Distrito/Localidad/Comuna'

    name = fields.Char(
        string='Name',
        required=True,
    )
    code = fields.Char(
        string='Code',
        size=30,
    )
    city_id = fields.Many2one(
        'res.country.state.city',
        string='City',
    )


class res_city_neighborhood(models.Model):
    _name = 'res.country.state.city.neighborhood'
    _description = 'neighborhood'

    name = fields.Char(
        string='Neighborhood',
        required=True,
    )
    code = fields.Char(
        string='Code',
        size=30,
    )
    city_id = fields.Many2one(
        'res.country.state.city',
        string='City',
        required=True,
    )
    district_id = fields.Many2one(
        'res.country.state.city.district',
        string='Distrito/Localidad/Comuna',
    )
