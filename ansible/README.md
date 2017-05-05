## ansible Commands Usage

Ad-Hoc Commnds,
  `ansible testvm -i hosts -m win_ping`

Playbooks,

  `ansible-playbook -i hosts ipconfig.yaml --extra-vars "hosts=testvm"`

Some MOre Example,

  `ansible-playbook -i hosts fetch.yaml --extra-vars "hosts=windows drive=E dest=/home/naanal/somefolder"`
