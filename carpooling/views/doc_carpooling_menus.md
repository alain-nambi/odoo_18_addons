
<!--
This XML file defines the menu structure and window actions for the Carpooling module in Odoo.

Root Element:
<odoo> - The root element for Odoo XML files.

Elements:
1. <record id="carpool_action" model="ir.actions.act_window">
    - Defines a window action for the Carpooling module.
    - Fields:
      - name: The name of the action, displayed as "Find Carpool".
      - res_model: The target model for the action, set to "carpooling.carpooling".
      - view_mode: The view mode for the action, set to "form".

2. <menuitem id="root_menu" name="Carpooling" />
    - Defines the root menu item for the Carpooling module.
    - Attributes:
      - id: The unique identifier for the menu item, set to "root_menu".
      - name: The name of the menu item, displayed as "Carpooling".

3. <menuitem id="carpooling_menu" name="Carpools and Poolers" parent="carpooling.root_menu" action="carpool_action" sequence="10" />
    - Defines a submenu item under the root menu.
    - Attributes:
      - id: The unique identifier for the submenu item, set to "carpooling_menu".
      - name: The name of the submenu item, displayed as "Carpools and Poolers".
      - parent: The parent menu item, set to "carpooling.root_menu".
      - action: The linked action, set to "carpool_action".
      - sequence: The order of the menu item, set to "10".
-->