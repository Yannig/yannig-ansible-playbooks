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
