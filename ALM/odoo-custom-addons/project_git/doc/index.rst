.. image:: https://www.gnu.org/graphics/lgplv3-147x51.png
   :target: https://www.gnu.org/licenses/lgpl-3.0.en.html
   :alt: License: LGPL-v3

===========
Project Git
===========

This is the base module for integrating Project module with remote Git repositories.
This module by itself only implements common logic among different Git repository managers.
In order to be able to use Project Git, user must install additional module for each
Git repository manager (eg. GitHub, GitLab, BitBucket, etc.)

Models introduced:

- Git Repository
- Git User (As defined in commit definition)
- Git Branch
- Git Commit



Usage
=====

Following steps are needed in order to use this module:

#. Install additional module for Git repository manager that you intent to use.
#. Go to Git > Repositories and create new Repository.
#. Choose Project, and Git repository manager.
#. On save, Webhook Uri and Secret will be generated.
#. Setup Webhook in Git repository manager using previously generated Webhook Uri and Secret.
#. On first commit, system will parse payload from webhook, and create Git Users, Branches and Commits, and also populate previously unknown data on Repository model.

You can link commit to one ore more tasks by including task key in commit message.



Credits
=======


Contributors
------------

* Sladjan Kantar <sladjan.kantar@modoolar.com>
* Petar Najman <petar.najman@modoolar.com>
* Miroslav Nikolić <miroslav.nikolic@modoolar.com>
* Aleksandar Gajić <aleksandar.gajic@modoolar.com>

Maintainer
----------

.. image:: https://www.modoolar.com/modoolar/static/modoolar-logo.png
   :alt: Modoolar
   :target: https://modoolar.com

This module is maintained by Modoolar.

::

   As Odoo Gold partner, our company is specialized in Odoo ERP customization and business solutions development.
   Beside that, we build cool apps on top of Odoo platform.

To contribute to this module, please visit https://modoolar.com
