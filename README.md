Logrotate
=========

An ansible role to install and configure Logrotate in a Ubuntu machine

Requirements
------------

None

Role Variables
--------------

`name`: The name of the logrotate config file

`paths`: A list of log paths that will be managed by the logrotate config
```
paths:
  - "/foo/bar/test.log"
  - "/foo/bar/dev.log"
```

`frequency`: The frequency the log will be rotated. Possible values: `daily`, `weekly`, `monthly`, or `yearly`.

`minsize`: Log files are rotated when they grow bigger than size bytes, but not before the additionally  specified  time  interval (daily, weekly, monthly, or yearly)
```
minsize: 100M
```

`maxsize`: Log files are rotated when they grow bigger than size bytes even before the  additionally  specified time  interval  (daily, weekly, monthly, or yearly)
```
maxsize: 1G
```

`rotate`: Log  files are rotated count times before being removed or mailed
`rotate: 7`

`extra_scripts`: Extra scripts or config that are not included in the default options of this role


```
extra_scripts: |
  create 644 user group
  postrotate
    <some scripts here>
  endscript
```

Dependencies
------------

None

Example Playbook
----------------

```
- name: Example logrotate
  hosts: all
  roles:
    - role: jobscore.logrotate
  vars:
    logrotate_config:
      - name: Rails logrotate
        paths:
          - "/var/log/rails.log"
        frequency: daily
        minsize: 100M
        rotate: 7
        extra_scripts: |
          create 644 app app
          sharedscripts
          postrotate
            echo "Hello"
          endscript
```

License
-------

GPLv3

Author Information
------------------

[Glauber Batista](https://github.com/GlauberrBatista)
