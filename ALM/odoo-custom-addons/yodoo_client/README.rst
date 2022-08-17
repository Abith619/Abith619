Yodoo Client
============


.. |badge3| image:: https://img.shields.io/badge/powered%20by-yodoo.systems-00a09d.png
    :target: https://yodoo.systems
    
.. |badge5| image:: https://img.shields.io/badge/maintainer-CR&D-purple.png
    :target: https://crnd.pro/

.. |badge4| image:: https://img.shields.io/badge/docs-Odoo_Infrastructure_Client-yellowgreen.png
    :target: http://review-docs.10.100.34.40.xip.io/review/doc-odoo-infrastructure/11.0/en/odoo_infrastructure_admin/


|badge4| |badge5|

The Yodoo Client application is the client addon for the Yodoo Cockpit.
It allows you to connect Odoo instance to Yodoo Cockpit.

Yodoo Cockpit - Manage your odoo infrastructure via odoo
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. image:: https://crnd.pro/web/image/18846/banner_2_4_gif_animation_cut.gif
  :target: https://crnd.pro/yodoo-cockpit
  :alt: Yodoo Cockpit - Manage your odoo infrastructure via odoo

Take a look at `[Yodoo Cockpit](https://crnd.pro/yodoo-cockpit) <https://crnd.pro/yodoo-cockpit>`__ project, and discover the easiest way to manage your odoo installations.
Just short notes about `[Yodoo Cockpit](https://crnd.pro/yodoo-cockpit) <https://crnd.pro/yodoo-cockpit>`__:

- start new production-ready odoo instance in 1-2 minutes.
- add custom addons to your odoo instances in few clicks.
- out-of-the-box email configuration: just press button and add some records to your DNS, and get a working email
- make your odoo instance available to external world (internet) in 30 seconds (just add single record in your DNS)
- easy way to sell your odoo-based product in SaaS way.
- Yodoo Cockpit could be launched as Infrastructure as a Service (IaaS), thus you even do not need to worry about servers.

If you have any questions, then contact us at `info@crnd.pro <mailto:info@crnd.pro>`__, so we could schedule online-demonstration.


Configuration
'''''''''''''
The configuration has several steps.

1. Set `yodoo_token` to the `odoo.conf` file.
    This is a series of random ascii characters.
    This is the same as the `odoo_instance_token` field on the remote server.
    
    .. code:: 
    
        yodoo_token = Your_random_token

2. Set `admin_access_url` and `admin_access_credentials` to the `odoo.conf` file.
    Enables full administrator access from the remote server via the button.

    .. code::

        admin_access_url = True
        admin_access_credentials = True

    Enables administrator access from the remote server via a temporary login and password.

    .. code::

        admin_access_url = False
        admin_access_credentials = True

    Disabled administrator access from the remote server.

    .. code::

        admin_access_url = False
        admin_access_credentials = False

3. (Optional) set `yodoo_db_filter` to `True` if you want to use header-based database selection.
   In this case `HTTP_X_ODOO_DBFILTER` header will be used to filter databases

4. Set `server_wide_modules` to `odoo.conf` file.

    .. code::

        server_wide_modules = base,web,yodoo_client

5. (Optional) Set `yodoo_auto_install_addons` to coma-separated list of addons,
   that have to be installed on database creation.




Bug Tracker
'''''''''''

Bugs are tracked on `https://crnd.pro/requests <https://crnd.pro/requests>`_.
In case of trouble, please report there.


Level up your service quality
=============================

Level up your service with our `Helpdesk <https://crnd.pro/solutions/helpdesk>`__ / `Service Desk <https://crnd.pro/solutions/service-desk>`__ / `ITSM <https://crnd.pro/itsm>`__ solution.

Just test it at `yodoo.systems <https://yodoo.systems/saas/templates>`__: choose template you like, and start working.

Test all available features of `Bureaucrat ITSM <https://crnd.pro/itsm>`__ with `this template <https://yodoo.systems/saas/template/bureaucrat-itsm-demo-data-95>`__.


Maintainer
==========
.. image:: https://crnd.pro/web/image/3699/300x140/crnd.png

Our web site: https://crnd.pro/

This module is maintained by the Center of Research & Development company.

We can provide you further Odoo Support, Odoo implementation, Odoo customization, Odoo 3rd Party development and integration software, consulting services. Our main goal is to provide the best quality product for you. 

For any questions `contact us <mailto:info@crnd.pro>`__.
