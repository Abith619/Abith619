def migrate(cr, installed_version):
    cr.execute("""
        UPDATE ir_act_server
        SET code = replace(
            code,
            '_scheduler_cleanup_expired_entries',
            'scheduler_cleanup_expired_entries')
        WHERE model_name = 'odoo.infrastructure.client.auth'
          AND code ILIKE '%model._scheduler_cleanup_expired_entries%';
    """)
