# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from openerp.osv import fields, osv

class clv_medicament_therapeutic_class(osv.osv):
    _name = 'clv_medicament.therapeutic_class'

    _columns = {
        'name': fields.char(size=256, string='Therapeutic Class', required=True),
        'code': fields.char(size=256, string='Code'),
        'info': fields.text(string='Info'),
        'active': fields.boolean('Active', 
                                 help="The active field allows you to hide the therapeutic class without removing it."),
        'medicament_ids': fields.one2many('clv_medicament', 'therapeutic_class', 'Medicaments'),
    }
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Therapeutic Class must be unique!'),
        ('code_uniq', 'UNIQUE(code)', 'Code must be unique!'),
    ]

class clv_medicament(osv.osv):
    _inherit = 'clv_medicament'

    _columns = {
        'therapeutic_class': fields.many2one('clv_medicament.therapeutic_class', string='Therapeutic Class', 
                                             help='Medicament Therapeutic Class'),
        }
    