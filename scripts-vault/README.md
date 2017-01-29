Script vault POC with Ansible
=============================

You can read the original article at the following location (french): https://lesaventuresdeyannigdanslemondeit.blogspot.fr/2017/01/chiffrementdechiffrement-des-mots-de.html

But why we wan't to vault our scripts first?
--------------------------------------------

With Ansible, you often end up with this kind of implementation:

    - name: "Put a template script"
      template:
        src: "template.sh.j2"
        dest: "/tmp/creation.sh"
        mode: "755"
      register: _

    - name: "Execute this script"
      shell: "/tmp/creation.sh"
      when: _.changed|d('no')|bool


Problem: if the script use private data (password, login), you get them in clear text on your machine. The playbook **shell-vault.yml** is an example of implementation to hide sensitive data using 3DES encryption.

Filters
-------

This playbook use 2 custom filters (in **filter_plugins/encrypt.py**):

- des3_vault: encrypt a value using 3DES and a key
- random_key: generate a random key 24 bytes long

The **random_key** filter use a seed to generate a stable random string. In this playbook, I use the machine name as a seed for the random generator. This key is then used by des3_vault to exchange sensitive data. If you don't have the randomized key, it's a little bit harder to retrieve something from the local script.
