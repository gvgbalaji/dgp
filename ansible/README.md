## ansible Commands Usage

Ad-Hoc Commnds,
  `ansible testvm -i hosts -m win_ping`

Playbooks,

  `ansible-playbook -i hosts ipconfig.yaml --extra-vars "hosts=testvm"`

To Fetch Files from windows,

  `ansible-playbook -i hosts fetch.yaml --extra-vars "hosts=windows drive=E dest=/home/naanal/somefolder"`

To Restore Files to windows,

  `ansible-playbook -i hosts restore.yaml --extra-vars "hosts=windows drive=E src_path=/home/naanal/folder"`
