/*
 * This file defines access control rules for the 'carpooling' module in Odoo.
 * 
 * The file is in CSV format and specifies the permissions for the 'carpooling' model.
 * 
 * Columns:
 * - id: Unique identifier for the access control rule.
 * - name: Name of the access control rule.
 * - model_id:id: The model to which the access control rule applies.
 * - group_id:id: The user group to which the access control rule applies.
 * - perm_read: Permission to read records (1 for allowed, 0 for not allowed).
 * - perm_write: Permission to write records (1 for allowed, 0 for not allowed).
 * - perm_create: Permission to create records (1 for allowed, 0 for not allowed).
 * - perm_unlink: Permission to delete records (1 for allowed, 0 for not allowed).
 * 
 * In this example, the 'access_carpooling_carpooling' rule grants read, write, create, 
 * and delete permissions on the 'carpooling' model to users in the 'base.group_user' group.
 */