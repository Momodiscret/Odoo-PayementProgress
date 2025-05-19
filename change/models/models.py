from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_paid = fields.Float(
        string="Montant payé",
        compute="_compute_amount_paid", 
        store=True
    )
    apport_paye = fields.Float(string="Apport payé (%)", compute="_compute_apport_paye", store=True)

    @api.depends('payment_state', 'line_ids.amount_residual')
    def _compute_amount_paid(self):
        for move in self:
            if move.is_invoice(include_receipts=True):  # s'assure qu'on est bien sur une facture
                amount_total = move.amount_total
                residual = move.amount_residual
                move.amount_paid = amount_total - residual
            else:
                move.amount_paid = 0.0

    @api.depends('amount_total', 'amount_paid')
    def _compute_apport_paye(self):
        for order in self:
            if order.amount_total:
                order.apport_paye = (order.amount_paid / order.amount_total) * 100
            else:
                order.apport_paye = 0.0

