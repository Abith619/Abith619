from odoo import http
from odoo.http import request
from odoo.addons.website_slides.controllers.main import WebsiteSlides


class WebsiteSlidesXP(WebsiteSlides):

    @http.route()
    def slide_quiz_submit(self, slide_id, **post):

        # 1️⃣ Run Odoo core logic first
        response = super().slide_quiz_submit(slide_id, **post)

        slide = request.env['slide.slide'].sudo().browse(int(slide_id))
        partner = request.env.user.partner_id

        slide_partner = request.env['slide.slide.partner'].sudo().search([
            ('slide_id', '=', slide.id),
            ('partner_id', '=', partner.id),
        ], limit=1)

        # 2️⃣ Store XP (FIXED)
        if slide_partner and slide.question_ids:
            rewards = [
                slide.quiz_first_attempt_reward,   # 1st try
                slide.quiz_second_attempt_reward,  # 2nd try
                slide.quiz_third_attempt_reward,   # 3rd try
                slide.quiz_fourth_attempt_reward,  # 4th+
            ]

            # 🔥 CRITICAL FIX (subtract 1)
            idx = max(slide_partner.quiz_attempts_count - 1, 0)

            if idx >= len(rewards):
                idx = len(rewards) - 1

            slide_partner.quiz_xp = rewards[idx]

        return response
